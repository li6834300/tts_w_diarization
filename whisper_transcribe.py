#!/usr/bin/env python3
import os
import sys
import argparse
from faster_whisper import WhisperModel
import json

def transcribe_audio(audio_path, model_name="base", output_dir="transcriptions"):
    """
    Transcribe audio using Whisper AI (faster-whisper implementation)
    
    Args:
        audio_path: Path to the audio file
        model_name: Whisper model to use (tiny, base, small, medium, large-v2)
        output_dir: Directory to save the output files
    """
    print(f"Loading model: {model_name}")
    # Use CPU for device if no GPU available
    model = WhisperModel(model_name, device="cpu", compute_type="float32")
    
    print(f"Transcribing: {audio_path}")
    # Run the transcription
    segments, info = model.transcribe(audio_path, beam_size=5)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get filename without extension
    base_name = os.path.basename(audio_path)
    file_name = os.path.splitext(base_name)[0]
    
    # Process and save in different formats
    # Collect segments for processing
    segment_list = []
    full_text = ""
    
    print("Processing segments...")
    for segment in segments:
        full_text += segment.text + " "
        segment_dict = {
            "id": segment.id,
            "seek": segment.seek,
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
            "tokens": segment.tokens,
            "temperature": segment.temperature,
            "avg_logprob": segment.avg_logprob,
            "compression_ratio": segment.compression_ratio,
            "no_speech_prob": segment.no_speech_prob
        }
        segment_list.append(segment_dict)
    
    # Save transcription in different formats
    # 1. Save plain text
    txt_path = f"{output_dir}/{file_name}.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(full_text.strip())
    print(f"Saved: {txt_path}")
    
    # 2. Save JSON with all information
    json_path = f"{output_dir}/{file_name}.json"
    json_data = {
        "text": full_text.strip(),
        "segments": segment_list,
        "language": info.language,
        "language_probability": info.language_probability
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {json_path}")
    
    # 3. Save SRT (SubRip) format
    srt_path = f"{output_dir}/{file_name}.srt"
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segment_list, start=1):
            # Format timestamp as hh:mm:ss,mmm
            start_time = format_timestamp(segment["start"])
            end_time = format_timestamp(segment["end"])
            f.write(f"{i}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{segment['text'].strip()}\n\n")
    print(f"Saved: {srt_path}")
    
    # 4. Save VTT (WebVTT) format
    vtt_path = f"{output_dir}/{file_name}.vtt"
    with open(vtt_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for i, segment in enumerate(segment_list, start=1):
            start_time = format_timestamp(segment["start"], vtt=True)
            end_time = format_timestamp(segment["end"], vtt=True)
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{segment['text'].strip()}\n\n")
    print(f"Saved: {vtt_path}")
    
    # 5. Save TSV format
    tsv_path = f"{output_dir}/{file_name}.tsv"
    with open(tsv_path, "w", encoding="utf-8") as f:
        f.write("start\tend\ttext\n")
        for segment in segment_list:
            f.write(f"{segment['start']:.2f}\t{segment['end']:.2f}\t{segment['text'].strip()}\n")
    print(f"Saved: {tsv_path}")
    
    return full_text.strip()

def format_timestamp(seconds, vtt=False):
    """
    Format timestamp as hh:mm:ss,mmm for SRT or hh:mm:ss.mmm for VTT
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    if vtt:
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"
    else:
        return f"{hours:02d}:{minutes:02d}:{int(secs):02d},{int((secs - int(secs))*1000):03d}"

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio using Whisper AI")
    parser.add_argument("--audio", type=str, help="Path to the audio file")
    parser.add_argument("--model", type=str, default="base", 
                        choices=["tiny", "base", "small", "medium", "large-v1", "large-v2", "large-v3"],
                        help="Whisper model to use")
    parser.add_argument("--output", type=str, default="transcriptions",
                        help="Directory to save the output files")
    
    args = parser.parse_args()
    
    if not args.audio:
        parser.print_help()
        return
    
    if not os.path.exists(args.audio):
        print(f"Error: Audio file not found: {args.audio}")
        return
    
    text = transcribe_audio(args.audio, args.model, args.output)
    print("\nTranscription:")
    print(text)

if __name__ == "__main__":
    main() 