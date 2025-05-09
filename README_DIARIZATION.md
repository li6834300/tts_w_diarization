# Whisper with Speaker Diarization

This tool provides a simplified speaker diarization (identifying who is speaking when) capability to Whisper transcriptions.

## Features

- Transcribe audio using faster-whisper
- Add simplified speaker segmentation
- Combine transcription with speaker information
- Output in multiple formats (TXT, JSON, SRT, VTT)

## Current Implementation

This version uses a simplified time-based approach for speaker segmentation:

- The audio is transcribed using faster-whisper
- Speakers are alternated every 10 seconds (SPEAKER_00, SPEAKER_01)
- Transcription segments are mapped to speakers based on time overlaps
- Results are saved in multiple formats

**Note:** This is a simpler alternative to full speaker diarization since there were compatibility issues with the pyannote.audio library.

## Usage

### Speaker Diarization Script

```bash
python whisper_diarize.py --audio path/to/audio.mp3 --model base
```

Options:
- `--audio`: Path to the audio file (required)
- `--model`: Whisper model to use (default: base)
- `--output`: Directory to save the output files (default: transcriptions)

### Output Files

The script generates several output files:

1. `filename_diarized.txt`: Plain text with speaker labels
2. `filename_diarized.json`: JSON with detailed information including timestamps and speaker labels
3. `filename_diarized.srt`: SubRip subtitle format with speaker information
4. `filename_diarized.vtt`: WebVTT subtitle format with speaker information

## Requirements

- Python 3.7+
- faster-whisper
- pydub
- ffmpeg (must be installed on your system) 