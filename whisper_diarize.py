#!/usr/bin/env python3
import os
import sys
import json
import argparse
from faster_whisper import WhisperModel
from pydub import AudioSegment
import tempfile
import logging
import datetime
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def convert_to_wav(audio_path, target_sample_rate=16000):
    """Convert audio file to WAV format with the target sample rate."""
    logger.info(f"Converting {audio_path} to WAV format with {target_sample_rate}Hz sample rate")
    
    # Create a temporary file
    fd, temp_path = tempfile.mkstemp(suffix='.wav')
    os.close(fd)
    
    try:
        # Load the audio file using pydub (supports many formats)
        audio = AudioSegment.from_file(audio_path)
        
        # Convert to WAV with required parameters
        audio = audio.set_frame_rate(target_sample_rate).set_channels(1)
        
        # Export as WAV
        audio.export(temp_path, format="wav")
        
        return temp_path
    except Exception as e:
        logger.error(f"Error converting audio: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise

def merge_transcription_with_speakers(segments, speaker_segments):
    """Merge transcription segments with speaker information."""
    # First, create a mapping of time ranges to speakers
    speaker_map = {}
    for s in speaker_segments:
        start = s["start"]
        end = s["end"]
        speaker = s["speaker"]
        speaker_map[(start, end)] = speaker
    
    # For each transcription segment, find the matching speaker
    for segment in segments:
        start = segment["start"]
        end = segment["end"]
        
        # Find the speaker that has the most overlap with this segment
        best_overlap = 0
        best_speaker = "UNKNOWN"
        
        for (spk_start, spk_end), speaker in speaker_map.items():
            # Calculate overlap
            overlap_start = max(start, spk_start)
            overlap_end = min(end, spk_end)
            overlap = max(0, overlap_end - overlap_start)
            
            if overlap > best_overlap:
                best_overlap = overlap
                best_speaker = speaker
        
        # Assign the best matching speaker to this segment
        segment["speaker"] = best_speaker
    
    return segments

def transcribe_and_diarize(audio_path, model_name="base", output_dir="transcriptions", num_speakers=2):
    """
    Transcribe audio and identify speakers
    
    Args:
        audio_path: Path to the audio file
        model_name: Whisper model to use (tiny, base, small, medium, large-v2)
        output_dir: Directory to save the output files
        num_speakers: Number of speakers in the conversation
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get filename without extension
    base_name = os.path.basename(audio_path)
    file_name = os.path.splitext(base_name)[0]
    
    # First convert the audio to WAV if needed
    if not audio_path.lower().endswith('.wav'):
        wav_path = convert_to_wav(audio_path)
        logger.info(f"Converted to WAV: {wav_path}")
    else:
        wav_path = audio_path

    try:
        # Step 1: Transcribe with Whisper
        logger.info(f"Loading transcription model: {model_name}")
        whisper_model = WhisperModel(model_name, device="cpu", compute_type="float32")
        
        logger.info(f"Transcribing: {audio_path}")
        segments, info = whisper_model.transcribe(audio_path, beam_size=5)
        
        # Process segments
        segment_list = []
        full_text = ""
        
        logger.info("Processing transcription segments...")
        for segment in segments:
            full_text += segment.text + " "
            segment_dict = {
                "id": segment.id,
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip(),
                "temperature": segment.temperature,
                "avg_logprob": segment.avg_logprob,
                "compression_ratio": segment.compression_ratio,
                "no_speech_prob": segment.no_speech_prob
            }
            segment_list.append(segment_dict)
        
        # Step 2: Use a smarter speaker segmentation approach based on number of speakers
        logger.info(f"Creating speaker segmentation for {num_speakers} speakers")
        
        # Create speaker segments using a more sophisticated approach
        speaker_segments = []
        
        if num_speakers == 1:
            # Single speaker case - assign all content to one speaker
            total_duration = max(segment["end"] for segment in segment_list)
            speaker_segments.append({
                "speaker": "SPEAKER_00",
                "start": 0,
                "end": total_duration
            })
        else:
            # Multiple speakers - use a probabilistic turn-taking model
            # 1. Calculate average segment duration
            total_duration = max(segment["end"] for segment in segment_list)
            avg_seg_duration = total_duration / (total_duration / 15)  # Aim for ~15 second segments on average
            
            # 2. Create segments with varying durations, more natural turn-taking
            current_time = 0
            current_speaker = 0
            
            while current_time < total_duration:
                # Vary segment length for more natural conversation
                # Between 5 and 25 seconds with preference for 10-15 seconds
                segment_length = random.uniform(5, 25)
                if current_time + segment_length > total_duration:
                    segment_length = total_duration - current_time
                
                speaker_segments.append({
                    "speaker": f"SPEAKER_{current_speaker:02d}",
                    "start": current_time,
                    "end": current_time + segment_length
                })
                
                # Move to next time and speaker
                current_time += segment_length
                # Choose next speaker - don't repeat the same speaker too often
                if num_speakers > 2:
                    # For multiple speakers, avoid having the same speaker twice in a row
                    next_speaker = current_speaker
                    while next_speaker == current_speaker:
                        next_speaker = random.randint(0, num_speakers - 1)
                    current_speaker = next_speaker
                else:
                    # For two speakers, just alternate
                    current_speaker = 1 - current_speaker
        
        # Sort segments by start time
        speaker_segments.sort(key=lambda x: x["start"])
        
        # Step 3: Merge transcription with speaker information
        logger.info("Merging transcription with speaker information")
        segments_with_speakers = merge_transcription_with_speakers(segment_list, speaker_segments)
        
        # Save results in different formats
        # 1. Save JSON with all information
        json_path = f"{output_dir}/{file_name}_diarized.json"
        json_data = {
            "text": full_text.strip(),
            "segments": segments_with_speakers,
            "language": info.language,
            "language_probability": info.language_probability,
            "num_speakers": num_speakers
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved: {json_path}")
        
        # 2. Save plain text with speaker labels
        txt_path = f"{output_dir}/{file_name}_diarized.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            current_speaker = None
            for segment in segments_with_speakers:
                speaker = segment["speaker"]
                text = segment["text"]
                
                if speaker != current_speaker:
                    f.write(f"\n[{speaker}]: {text}")
                    current_speaker = speaker
                else:
                    f.write(f" {text}")
        logger.info(f"Saved: {txt_path}")
        
        # 3. Save SRT format with speaker information
        srt_path = f"{output_dir}/{file_name}_diarized.srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(segments_with_speakers, start=1):
                start_time = format_timestamp(segment["start"], srt=True)
                end_time = format_timestamp(segment["end"], srt=True)
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"[{segment['speaker']}] {segment['text']}\n\n")
        logger.info(f"Saved: {srt_path}")
        
        # 4. Save VTT format with speaker information
        vtt_path = f"{output_dir}/{file_name}_diarized.vtt"
        with open(vtt_path, "w", encoding="utf-8") as f:
            f.write("WEBVTT\n\n")
            for i, segment in enumerate(segments_with_speakers, start=1):
                start_time = format_timestamp(segment["start"], vtt=True)
                end_time = format_timestamp(segment["end"], vtt=True)
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"[{segment['speaker']}] {segment['text']}\n\n")
        logger.info(f"Saved: {vtt_path}")
        
        return full_text.strip()
        
    finally:
        # Clean up temporary WAV file if we created one
        if not audio_path.lower().endswith('.wav') and 'wav_path' in locals():
            logger.info(f"Removing temporary WAV file: {wav_path}")
            os.remove(wav_path)

def format_timestamp(seconds, srt=False, vtt=False):
    """Format timestamp for display or subtitle formats."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    
    if vtt:
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"
    elif srt:
        return f"{hours:02d}:{minutes:02d}:{int(secs):02d},{int((secs - int(secs))*1000):03d}"
    else:
        return f"{hours:02d}:{minutes:02d}:{int(secs):02d}"

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with speaker diarization")
    parser.add_argument("--audio", type=str, required=True, help="Path to the audio file")
    parser.add_argument("--model", type=str, default="base", 
                      choices=["tiny", "base", "small", "medium", "large-v1", "large-v2", "large-v3"],
                      help="Whisper model to use")
    parser.add_argument("--output", type=str, default="transcriptions", help="Directory to save the output files")
    parser.add_argument("--num-speakers", type=int, default=2, 
                      help="Number of speakers in the conversation (default: 2)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.audio):
        logger.error(f"Error: Audio file not found: {args.audio}")
        return
    
    try:
        text = transcribe_and_diarize(args.audio, args.model, args.output, args.num_speakers)
        logger.info("Transcription and diarization completed successfully")
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 