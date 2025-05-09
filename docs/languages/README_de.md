# Audio-Transkriptionstool mit Sprechererkennung

[English](../../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Eine Webanwendung, die Audiodateien automatisch transkribiert und verschiedene Sprecher in Gesprächen mit Hilfe des OpenAI Whisper-Modells und Sprechererkennungstechnologien identifiziert.

## Funktionen

- **Moderne Benutzeroberfläche:**
  * Saubere, intuitive Weboberfläche mit Drag-and-Drop-Datei-Upload
  * Echtzeit-Fortschrittsverfolgung während der Transkriptionsverarbeitung
  * Responsives Design, das auf verschiedenen Geräten funktioniert
  * Unterstützung für 18 Sprachen in der Benutzeroberfläche

- **Leistungsstarke Transkriptions-Engine:**
  * Integration mit OpenAI's Whisper Spracherkennungsmodellen
  * Mehrere Modellgrößen (tiny, base, small, medium, large) für optimale Balance zwischen Geschwindigkeit und Genauigkeit
  * Sprechererkennung zur Identifizierung und Trennung verschiedener Sprecher im Gespräch
  * Unterstützung für verschiedene Audioformate (MP3, WAV, OGG, FLAC, M4A)

- **Flexible Ausgabeoptionen:**
  * Download von Transkriptionen in mehreren Formaten (TXT, JSON, SRT, VTT)
  * Zeitstempel-Transkriptionen mit Sprecheridentifikation
  * Übersichtliche Formatierung für einfaches Lesen und Nachbearbeitung

## Installation

1. Repository klonen:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Anwendung starten:
```bash
python app_diarize.py
```

Die Anwendung ist unter `http://localhost:5001` verfügbar

## Verwendung

1. Öffnen Sie Ihren Webbrowser und navigieren Sie zu `http://localhost:5001`
2. Laden Sie eine Audiodatei über die Drag-and-Drop-Oberfläche oder den Dateiauswahl-Dialog hoch
3. Wählen Sie die gewünschte Modellgröße und Anzahl der Sprecher
4. Warten Sie auf den Abschluss der Transkription
5. Laden Sie die Ergebnisse in Ihrem bevorzugten Format herunter

## Fehlerbehebung

- Wenn Port 5001 bereits in Verwendung ist, können Sie den Port in `app_diarize.py` ändern
- Für große Audiodateien empfiehlt sich die Verwendung einer kleineren Modellgröße für schnellere Verarbeitung
- Stellen Sie sicher, dass ausreichend Festplattenspeicher für temporäre Dateien verfügbar ist

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe LICENSE-Datei für Details.

## Autor

Zhien Li 