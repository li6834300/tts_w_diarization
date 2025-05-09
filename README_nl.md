# Audio Transcriptie Tool met Sprekerherkenning

[English](README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md)

Een webapplicatie die automatisch audiobestanden transcribeert en verschillende sprekers in gesprekken identificeert met behulp van OpenAI's Whisper-model en sprekerherkenningstechnologieën.

## Functies

- **Modern Gebruikersinterface:**
  * Schone, intuïtieve webinterface met drag-and-drop bestandsuploads
  * Real-time voortgangsregistratie tijdens transcriptieverwerking
  * Responsief ontwerp dat werkt op verschillende apparaten
  * Ondersteuning voor 18 talen in de gebruikersinterface

- **Krachtige Transcriptie-engine:**
  * Integratie met OpenAI's Whisper spraakherkenningsmodellen
  * Meerdere modelgroottes (tiny, base, small, medium, large) om snelheid en nauwkeurigheid in balans te brengen
  * Sprekerherkenning om verschillende sprekers in het gesprek te identificeren en te scheiden
  * Ondersteuning voor verschillende audioformaten (MP3, WAV, OGG, FLAC, M4A)

- **Flexibele Uitvoeropties:**
  * Download transcripties in meerdere formaten (TXT, JSON, SRT, VTT)
  * Getimede transcripties met sprekeridentificatie
  * Nette opmaak voor eenvoudig lezen en nabewerking

## Installatie

1. Kloon de repository:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Installeer afhankelijkheden:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Start de applicatie:
```bash
python app_diarize.py
```

De applicatie is beschikbaar op `http://localhost:5001`

## Gebruik

1. Open uw webbrowser en ga naar `http://localhost:5001`
2. Upload een audiobestand via de drag-and-drop interface of bestandskeuze
3. Selecteer de gewenste modelgrootte en aantal sprekers
4. Wacht tot de transcriptie is voltooid
5. Download de resultaten in uw voorkeursformaat

## Probleemoplossing

- Als poort 5001 al in gebruik is, kunt u de poort in `app_diarize.py` wijzigen
- Voor grote audiobestanden kunt u overwegen een kleiner model te gebruiken voor snellere verwerking
- Zorg voor voldoende schijfruimte voor tijdelijke bestanden

## Licentie

Dit project is gelicenseerd onder de MIT-licentie - zie het LICENSE-bestand voor details.

## Auteur

Zhien Li 