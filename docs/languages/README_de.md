# Audio-Transkription mit Sprechererkennung

Eine Webanwendung, die Audiodateien transkribiert und verschiedene Sprecher im Gespräch identifiziert, unter Verwendung von OpenAIs Whisper-Modell und Sprecherdiarisierungstechnologien.

## Funktionen

- Hochladen von Audiodateien (MP3, WAV, OGG, FLAC, M4A)
- Transkription von Sprache mit OpenAIs Whisper-Modell (verschiedene Größen verfügbar)
- Identifizierung und Trennung verschiedener Sprecher in der Audiodatei
- Herunterladen der Ergebnisse in mehreren Formaten (TXT, JSON, SRT, VTT)
- Echtzeit-Fortschrittsverfolgung
- Übersichtliche und moderne Benutzeroberfläche
- Unterstützung für verschiedene Whisper-Modellgrößen zur Ausbalancierung von Geschwindigkeit und Genauigkeit
- Mehrsprachige Oberfläche mit Unterstützung für 18 Sprachen, darunter Englisch, Spanisch, Französisch, Deutsch, Chinesisch, Japanisch, Koreanisch, Russisch, Arabisch, Hindi, Portugiesisch, Italienisch, Niederländisch, Türkisch, Vietnamesisch, Thai, Polnisch und Schwedisch

## Demonstration

![Screenshot der Anwendung](docs/screenshot.png)

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes installiert haben:

- Python 3.8 oder neuer
- FFmpeg (erforderlich für die Audioverarbeitung)
- Git (optional, zum Klonen des Repositories)

## Installation

### Schritt 1: Repository klonen

```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

Oder laden Sie die ZIP-Datei herunter und extrahieren Sie sie.

### Schritt 2: Virtuelle Umgebung erstellen (empfohlen)

```bash
python -m venv venv

# Unter Windows
venv\Scripts\activate

# Unter macOS/Linux
source venv/bin/activate
```

### Schritt 3: Erforderliche Pakete installieren

```bash
pip install -r requirements.txt
```

Wenn Sie keine `requirements.txt`-Datei haben, können Sie eine mit folgendem Inhalt erstellen:

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

Oder installieren Sie die Pakete direkt:

```bash
pip install flask numpy torch torchaudio pyannote.audio openai-whisper pydub webrtcvad
```

### Schritt 4: FFmpeg installieren

#### Unter macOS (mit Homebrew):

```bash
brew install ffmpeg
```

#### Unter Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### Unter Windows:

1. Laden Sie FFmpeg von [ffmpeg.org](https://ffmpeg.org/download.html) herunter
2. Extrahieren Sie die Dateien
3. Fügen Sie den bin-Ordner zu Ihrer PATH-Umgebungsvariable hinzu

### Schritt 5: Anwendung starten

Sie können die Anwendung wie folgt ausführen:

```bash
# Mit python
python app_diarize.py

# ODER explizit mit python3 (empfohlen unter macOS/Linux)
python3 app_diarize.py
```

Wenn Sie einen anderen Port verwenden müssen (zum Beispiel, wenn Port 5001 bereits verwendet wird):

```bash
# Bearbeiten Sie app_diarize.py und ändern Sie die Portnummer
# Suchen Sie diese Zeile am Ende der Datei:
# app.run(debug=True, host="0.0.0.0", port=5001)
# Ändern Sie 5001 zu Ihrem gewünschten Port, zum Beispiel 5002

# ODER Sie können den Port direkt beim Ausführen angeben:
python3 -c "import app_diarize; app_diarize.app.run(debug=True, host='0.0.0.0', port=5002)"
```

Die Anwendung ist unter http://localhost:5001 (oder dem von Ihnen konfigurierten Port) verfügbar.

## Verwendung

1. Öffnen Sie die Anwendung in Ihrem Webbrowser
2. Ziehen Sie eine Audiodatei per Drag & Drop in das Feld oder klicken Sie auf "Dateien durchsuchen", um eine auszuwählen
3. Wählen Sie die Whisper-Modellgröße:
   - Tiny: Am schnellsten, aber am wenigsten genau
   - Base: Gute Balance für die meisten Zwecke
   - Small: Genauer, aber langsamer
   - Medium: Hohe Genauigkeit, langsamere Verarbeitung
   - Large-v2: Am genauesten, erfordert mehr Ressourcen
4. Legen Sie die Anzahl der Sprecher in der Audiodatei fest (falls bekannt)
5. Klicken Sie auf "Transkribieren" und warten Sie auf die Verarbeitung
6. Sehen Sie sich die Ergebnisse an und laden Sie sie in Ihrem bevorzugten Format herunter

## Häufige Probleme und Fehlerbehebung

### "Address already in use" / Port 5000 oder 5001 wird bereits verwendet

Dies tritt auf, wenn eine andere Anwendung den Port verwendet. Sie können:

1. Den Port in `app_diarize.py` ändern:

```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)  # Zu einem anderen Port wechseln
```

2. Unter macOS wird Port 5000 häufig vom AirPlay-Receiver verwendet. Sie können ihn in den Systemeinstellungen → Allgemein → AirDrop & Handoff deaktivieren.

### FFmpeg nicht gefunden

Stellen Sie sicher, dass FFmpeg installiert ist und in Ihrem PATH verfügbar ist:

```bash
# Überprüfen, ob FFmpeg installiert ist
ffmpeg -version
```

Wenn keine Versionsinformationen angezeigt werden, installieren Sie FFmpeg gemäß den obigen Installationsanweisungen neu.

### CUDA/GPU-Probleme

Wenn Sie versuchen, GPU-Beschleunigung zu verwenden, aber auf Fehler stoßen:

1. Stellen Sie sicher, dass Sie eine kompatible GPU haben
2. Installieren Sie die richtige Version von PyTorch für Ihre CUDA-Version:

```bash
# Für CUDA 11.8
pip install torch==2.0.0+cu118 torchaudio==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

### Importfehler für pyannote.audio

Wenn Sie Probleme beim Installieren oder Importieren von pyannote.audio haben:

```bash
# Versuchen Sie die Installation aus dem Quellcode
pip install git+https://github.com/pyannote/pyannote-audio.git
```

### "No module named 'whisper_diarize'"

Stellen Sie sicher, dass sich die Datei `whisper_diarize.py` im selben Verzeichnis wie `app_diarize.py` befindet.

## Anpassung

### Änderung der maximalen Upload-Größe

Bearbeiten Sie `app_diarize.py` und ändern Sie den Parameter `MAX_CONTENT_LENGTH`:

```python
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100 MB
```

### Änderung des Erscheinungsbilds der Oberfläche

Bearbeiten Sie das CSS in `templates/diarize.html`, um Farben, Schriftarten und Layout anzupassen.

## Internationalisierung

Die Anwendung unterstützt 18 Sprachen:
- Englisch (English)
- Spanisch (Español)
- Französisch (Français)
- Deutsch
- Chinesisch (中文)
- Japanisch (日本語)
- Koreanisch (한국어)
- Russisch (Русский)
- Arabisch (العربية)
- Hindi (हिन्दी)
- Portugiesisch (Português)
- Italienisch (Italiano)
- Niederländisch (Nederlands)
- Türkisch (Türkçe)
- Vietnamesisch (Tiếng Việt)
- Thai (ไทย)
- Polnisch (Polski)
- Schwedisch (Svenska)

Benutzer können die Sprache über den Sprachauswähler in der oberen rechten Ecke der Oberfläche ändern. Alle UI-Elemente werden in die ausgewählte Sprache übersetzt.

### Hinzufügen weiterer Sprachen

Um weitere Sprachen hinzuzufügen, bearbeiten Sie die Datei `templates/diarize.html`:

1. Fügen Sie dem Dropdown-Menü der Sprachauswahl eine neue Option hinzu:
```html
<option value="sprach-code">Sprachname</option>
```

2. Fügen Sie Übersetzungen zum Objekt `translations` im JavaScript-Abschnitt hinzu:
```javascript
sprach-code: {
    title: "Übersetzter Titel",
    dragDrop: "Übersetzter Drag-and-Drop-Text",
    // Alle anderen erforderlichen Übersetzungen hinzufügen
}
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz - Details finden Sie in der LICENSE-Datei.

## Danksagungen

- [OpenAI Whisper](https://github.com/openai/whisper) für das Spracherkennungsmodell
- [Pyannote Audio](https://github.com/pyannote/pyannote-audio) für die Sprecherdiarisierung
- Flask für das Web-Framework

## Autor

Zhien Li
- GitHub: [li6834300](https://github.com/li6834300)
- LinkedIn: [zhienli277](https://www.linkedin.com/in/zhienli277/) 