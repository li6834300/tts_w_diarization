# Audio Transcription Tool with Speaker Diarization

[English](README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md)

A web application that automatically transcribes audio files and identifies different speakers in conversations using OpenAI's Whisper model and speaker diarization technologies.

## Features

- **Modern User Interface:**
  * Clean, intuitive web interface with drag-and-drop file uploads
  * Real-time progress tracking during transcription processing
  * Responsive design that works on various devices
  * Support for 18 languages in the user interface

- **Powerful Transcription Engine:**
  * Integration with OpenAI's Whisper speech recognition models
  * Multiple model sizes (tiny, base, small, medium, large) to balance speed and accuracy
  * Speaker diarization to identify and separate different speakers in the conversation
  * Support for various audio formats (MP3, WAV, OGG, FLAC, M4A)

- **Flexible Output Options:**
  * Download transcriptions in multiple formats (TXT, JSON, SRT, VTT)
  * Timestamped transcripts with speaker identification
  * Clean formatting for easy reading and post-processing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Run the application:
```bash
python app_diarize.py
```

The application will be available at `http://localhost:5001`

## Usage

1. Open your web browser and navigate to `http://localhost:5001`
2. Upload an audio file using the drag-and-drop interface or file selector
3. Select the desired model size and number of speakers
4. Wait for the transcription to complete
5. Download the results in your preferred format

## Troubleshooting

- If port 5001 is already in use, you can modify the port in `app_diarize.py`
- For large audio files, consider using a smaller model size for faster processing
- Ensure you have sufficient disk space for temporary files

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Zhien Li 