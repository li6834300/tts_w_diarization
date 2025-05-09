# Text to Audio Transcription with Speaker Diarization

A web application that transcribes audio files and identifies different speakers in the conversation using OpenAI's Whisper model and speaker diarization technologies.

## Languages
- English (This Document)
- [Spanish / Español](docs/languages/README_es.md)
- [Chinese / 中文](docs/languages/README_zh.md)
- [French / Français](docs/languages/README_fr.md)
- [German / Deutsch](docs/languages/README_de.md)

## Features

- Upload audio files (MP3, WAV, OGG, FLAC, M4A)
- Transcribe speech using OpenAI's Whisper model (various sizes available)
- Identify and separate different speakers in the audio
- Download results in multiple formats (TXT, JSON, SRT, VTT)
- Real-time progress tracking
- Clean and modern user interface
- Support for different Whisper model sizes to balance speed and accuracy
- Multilingual interface with support for 18 languages including English, Spanish, French, German, Chinese, Japanese, Korean, Russian, Arabic, Hindi, Portuguese, Italian, Dutch, Turkish, Vietnamese, Thai, Polish, and Swedish

## Demo

![Application Screenshot](docs/screenshot.png)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or newer
- FFmpeg (required for audio processing)
- Git (optional, for cloning the repository)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

Or download and extract the ZIP file from the repository.

### Step 2: Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install required packages

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can create one with the following content:

```
flask
numpy
torch
torchaudio
pyannote.audio
openai-whisper
pydub
webrtcvad
```

Or install the packages directly:

```bash
pip install flask numpy torch torchaudio pyannote.audio openai-whisper pydub webrtcvad
```

### Step 4: Install FFmpeg

#### On macOS (using Homebrew):

```bash
brew install ffmpeg
```

#### On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### On Windows:

1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the files
3. Add the bin folder to your PATH environment variable

### Step 5: Start the application

You can run the application using:

```bash
# Using python
python app_diarize.py

# OR using python3 explicitly (recommended on macOS/Linux)
python3 app_diarize.py
```

If you need to use a different port (for example, if port 5001 is already in use):

```bash
# Edit app_diarize.py and change the port number
# Find this line at the bottom of the file:
# app.run(debug=True, host="0.0.0.0", port=5001)
# Change 5001 to your desired port, for example 5002

# OR you can specify the port directly when running:
python3 -c "import app_diarize; app_diarize.app.run(debug=True, host='0.0.0.0', port=5002)"
```

The application will be available at http://localhost:5001 (or the port you configured).

### Command-line Usage (without web interface)

You can also use the script directly from the command line without starting the web application:

```bash
# Basic usage
python3 whisper_diarize.py --audio /path/to/your/audio/file.mp3 --model base

# Example with more options
python3 whisper_diarize.py --audio /path/to/your/audio/file.mp3 --model large --num_speakers 2
```

Common command-line options:
- `--audio`: Path to the audio file (required)
- `--model`: Whisper model size (tiny, base, small, medium, large) - default is base
- `--num_speakers`: Number of speakers in the audio (default is 2)
- `--output_dir`: Directory to save transcription outputs (default is "transcriptions")

This direct command-line usage is useful for batch processing or when you don't need the web interface.

## Usage

1. Open the application in your web browser
2. Drag and drop an audio file or click "Browse Files" to select one
3. Choose the Whisper model size:
   - Tiny: Fastest but least accurate
   - Base: Good balance for most purposes
   - Small: More accurate but slower
   - Medium: High accuracy, slower processing
   - Large-v2: Most accurate, requires more resources
4. Set the number of speakers in the audio (if known)
5. Click "Transcribe" and wait for processing
6. View the results and download in your preferred format

## Common Issues and Troubleshooting

### "Address already in use" / Port 5000 or 5001 is in use

This occurs when another application is using the port. You can:

1. Change the port in `app_diarize.py`:

```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)  # Change to another port
```

2. On macOS, port 5000 is often used by AirPlay Receiver. You can disable it in System Preferences → General → AirDrop & Handoff.

### FFmpeg not found

Ensure FFmpeg is installed and available in your PATH:

```bash
# Check if FFmpeg is installed
ffmpeg -version
```

If it doesn't show version information, reinstall FFmpeg following the installation instructions above.

### CUDA/GPU issues

If you're trying to use GPU acceleration but encountering errors:

1. Ensure you have a compatible GPU
2. Install the correct version of PyTorch for your CUDA version:

```bash
# For CUDA 11.8
pip install torch==2.0.0+cu118 torchaudio==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

### Import errors for pyannote.audio

If you encounter issues installing or importing pyannote.audio:

```bash
# Try installing from source
pip install git+https://github.com/pyannote/pyannote-audio.git
```

### "No module named 'whisper_diarize'"

Ensure the `whisper_diarize.py` file is in the same directory as `app_diarize.py`.

## Customization

### Changing the maximum upload size

Edit `app_diarize.py` and modify the `MAX_CONTENT_LENGTH` parameter:

```python
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100 MB
```

### Changing the interface appearance

Edit the CSS in `templates/diarize.html` to customize colors, fonts, and layout.

## Internationalization

The application supports 18 languages:
- English
- Spanish (Español)
- French (Français)
- German (Deutsch)
- Chinese (中文)
- Japanese (日本語)
- Korean (한국어)
- Russian (Русский)
- Arabic (العربية)
- Hindi (हिन्दी)
- Portuguese (Português)
- Italian (Italiano)
- Dutch (Nederlands)
- Turkish (Türkçe)
- Vietnamese (Tiếng Việt)
- Thai (ไทย)
- Polish (Polski)
- Swedish (Svenska)

Users can change the language using the language selector in the top-right corner of the interface. All UI elements will be translated to the selected language.

### Adding more languages

To add more languages, edit the `templates/diarize.html` file:

1. Add a new option to the language selector dropdown:
```html
<option value="language-code">Language Name</option>
```

2. Add translations to the `translations` object in the JavaScript section:
```javascript
language-code: {
    title: "Translated Title",
    dragDrop: "Translated drag and drop text",
    // Add all other required translations
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the speech recognition model
- [Pyannote Audio](https://github.com/pyannote/pyannote-audio) for speaker diarization
- Flask for the web framework

## Author

Zhien Li
- GitHub: [li6834300](https://github.com/li6834300)
- LinkedIn: [zhienli277](https://www.linkedin.com/in/zhienli277/) 