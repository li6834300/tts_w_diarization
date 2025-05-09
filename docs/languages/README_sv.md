# Ljudtranskriberingsverktyg med Talaridentifiering

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Ett webbprogram som automatiskt transkriberar ljudfiler och identifierar olika talare i konversationer med hjälp av OpenAIs Whisper-modell och talaridentifieringsteknik.

## Funktioner

- **Modernt Användargränssnitt:**
  * Rent och intuitivt webbgränssnitt med drag-and-drop-funktionalitet
  * Realtidsuppföljning av transkriberingsprocessen
  * Responsiv design som fungerar på olika enheter
  * Stöd för 18 språk i användargränssnittet

- **Kraftfull Transkriberingsmotor:**
  * Integration med OpenAIs Whisper-taligenkänningsmodeller
  * Flera modellstorlekar (tiny, base, small, medium, large) för balans mellan hastighet och noggrannhet
  * Talaridentifiering för att identifiera och separera olika talare i konversationen
  * Stöd för olika ljudformat (MP3, WAV, OGG, FLAC, M4A)

- **Flexibla Utdataalternativ:**
  * Ladda ner transkriberingar i flera format (TXT, JSON, SRT, VTT)
  * Transkriberingar med tidsstämplar och talaridentifiering
  * Rent format för enkel läsning och bearbetning

## Installation

1. Klona repot:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Installera beroenden:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Starta applikationen:
```bash
python app_diarize.py
```

Applikationen kommer att vara tillgänglig på `http://localhost:5001`

## Användning

1. Öppna en webbläsare och gå till `http://localhost:5001`
2. Ladda upp en ljudfil med hjälp av drag-and-drop-gränssnittet eller filväljaren
3. Välj modellstorlek och önskat antal talare
4. Vänta på att transkriberingen slutförs
5. Ladda ner resultaten i önskat format

## Felsökning

- Om port 5001 redan används kan du ändra porten i `app_diarize.py`
- För stora ljudfiler, överväg att använda en mindre modellstorlek för snabbare bearbetning
- Se till att du har tillräckligt med diskutrymme för temporära filer

## Licens

Detta projekt är licensierat under MIT-licensen - se LICENSE-filen för detaljer.

## Författare

Zhien Li 