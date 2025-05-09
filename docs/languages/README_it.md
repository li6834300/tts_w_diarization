# Strumento di Trascrizione Audio con Diarizzazione dei Parlanti

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Un'applicazione web che trascrive automaticamente i file audio e identifica diversi parlanti nelle conversazioni utilizzando il modello Whisper di OpenAI e tecnologie di diarizzazione.

## Caratteristiche

- **Interfaccia Utente Moderna:**
  * Interfaccia web pulita e intuitiva con caricamento file drag-and-drop
  * Monitoraggio in tempo reale del progresso durante l'elaborazione della trascrizione
  * Design responsive che funziona su vari dispositivi
  * Supporto per 18 lingue nell'interfaccia utente

- **Potente Motore di Trascrizione:**
  * Integrazione con i modelli di riconoscimento vocale Whisper di OpenAI
  * Dimensioni multiple del modello (tiny, base, small, medium, large) per bilanciare velocità e precisione
  * Diarizzazione per identificare e separare diversi parlanti nella conversazione
  * Supporto per vari formati audio (MP3, WAV, OGG, FLAC, M4A)

- **Opzioni di Output Flessibili:**
  * Download delle trascrizioni in più formati (TXT, JSON, SRT, VTT)
  * Trascrizioni con timestamp e identificazione dei parlanti
  * Formattazione pulita per facile lettura e post-elaborazione

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Installa le dipendenze:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Esegui l'applicazione:
```bash
python app_diarize.py
```

L'applicazione sarà disponibile su `http://localhost:5001`

## Utilizzo

1. Apri il tuo browser web e vai su `http://localhost:5001`
2. Carica un file audio utilizzando l'interfaccia drag-and-drop o il selettore di file
3. Seleziona la dimensione del modello e il numero desiderato di parlanti
4. Attendi il completamento della trascrizione
5. Scarica i risultati nel formato preferito

## Risoluzione dei Problemi

- Se la porta 5001 è già in uso, puoi modificare la porta in `app_diarize.py`
- Per file audio di grandi dimensioni, considera l'uso di una dimensione del modello più piccola per un'elaborazione più rapida
- Assicurati di avere spazio su disco sufficiente per i file temporanei

## Licenza

Questo progetto è concesso in licenza sotto la Licenza MIT - vedi il file LICENSE per i dettagli.

## Autore

Zhien Li 