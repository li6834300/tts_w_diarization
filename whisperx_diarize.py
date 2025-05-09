#!/usr/bin/env python3
import os
import sys
import json
import argparse
from pyannote.audio.pipelines import VoiceActivityDetection, SpeakerDiarization
from pydub import AudioSegment
import tempfile
import logging
import torch
import datetime

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

def transcribe_and_diarize(audio_path, output_dir="transcriptions", speaker_model="pyannote/speaker-diarization-3.1"):
    """
    Transcribe audio and identify speakers using pyannote.audio
    
    Args:
        audio_path: Path to the audio file
        output_dir: Directory to save the output files
        speaker_model: Model to use for speaker diarization
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
        # Initialize speaker diarization pipeline
        logger.info(f"Loading diarization model: {speaker_model}")
        pipeline = SpeakerDiarization.from_pretrained(
            speaker_model,
            use_auth_token=True
        )
        
        # Run diarization
        logger.info("Running speaker diarization")
        diarization = pipeline(wav_path)
        
        # Process diarization results
        speaker_segments = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            speaker_segments.append({
                "speaker": speaker,
                "start": turn.start,
                "end": turn.end
            })
            
        # Sort segments by start time
        speaker_segments.sort(key=lambda x: x["start"])
        
        # Process and save transcription with speaker labels
        
        # 1. Save JSON with speaker information
        json_path = f"{output_dir}/{file_name}_diarized.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(speaker_segments, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved: {json_path}")
        
        # 2. Save text format with speaker labels
        txt_path = f"{output_dir}/{file_name}_diarized.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            current_speaker = None
            for segment in speaker_segments:
                speaker = segment["speaker"]
                start_time = format_timestamp(segment["start"])
                end_time = format_timestamp(segment["end"])
                
                if speaker != current_speaker:
                    f.write(f"\n[{speaker}] ({start_time} - {end_time})\n")
                    current_speaker = speaker
                else:
                    f.write(f"({start_time} - {end_time}) ")
                
        logger.info(f"Saved: {txt_path}")
                
        # 3. Save SRT format with speaker information
        srt_path = f"{output_dir}/{file_name}_diarized.srt"
        with open(srt_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(speaker_segments, start=1):
                start_time = format_timestamp(segment["start"], srt=True)
                end_time = format_timestamp(segment["end"], srt=True)
                f.write(f"{i}\n")
                f.write(f"{start_time} --> {end_time}\n")
                f.write(f"[{segment['speaker']}]\n\n")
        logger.info(f"Saved: {srt_path}")
        
        return speaker_segments
        
    finally:
        # Clean up temporary WAV file if we created one
        if not audio_path.lower().endswith('.wav') and 'wav_path' in locals():
            logger.info(f"Removing temporary WAV file: {wav_path}")
            os.remove(wav_path)

def format_timestamp(seconds, srt=False):
    """Format timestamp for display or SRT format."""
    time_obj = datetime.datetime.utcfromtimestamp(seconds)
    if srt:
        return time_obj.strftime('%H:%M:%S,%f')[:-3]
    else:
        return time_obj.strftime('%H:%M:%S')

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio with speaker diarization")
    parser.add_argument("--audio", type=str, required=True, help="Path to the audio file")
    parser.add_argument("--output", type=str, default="transcriptions", help="Directory to save the output files")
    parser.add_argument("--speaker-model", type=str, default="pyannote/speaker-diarization-3.1", 
                      help="Speaker diarization model to use")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.audio):
        logger.error(f"Error: Audio file not found: {args.audio}")
        return
    
    try:
        transcribe_and_diarize(args.audio, args.output, args.speaker_model)
        logger.info("Transcription and diarization completed successfully")
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 