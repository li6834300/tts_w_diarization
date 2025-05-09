# Outil de Transcription Audio avec Diarisation des Locuteurs

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Une application web qui transcrit automatiquement les fichiers audio et identifie différents locuteurs dans les conversations en utilisant le modèle Whisper d'OpenAI et les technologies de diarisation.

## Fonctionnalités

- **Interface Utilisateur Moderne:**
  * Interface web épurée et intuitive avec téléchargement de fichiers par glisser-déposer
  * Suivi en temps réel de la progression pendant le traitement de la transcription
  * Conception responsive qui fonctionne sur divers appareils
  * Support de 18 langues dans l'interface utilisateur

- **Moteur de Transcription Puissant:**
  * Intégration des modèles de reconnaissance vocale Whisper d'OpenAI
  * Plusieurs tailles de modèles (tiny, base, small, medium, large) pour équilibrer vitesse et précision
  * Diarisation pour identifier et séparer différents locuteurs dans la conversation
  * Support de divers formats audio (MP3, WAV, OGG, FLAC, M4A)

- **Options de Sortie Flexibles:**
  * Téléchargement des transcriptions dans plusieurs formats (TXT, JSON, SRT, VTT)
  * Transcriptions horodatées avec identification des locuteurs
  * Formatage propre pour une lecture et un post-traitement faciles

## Installation

1. Cloner le dépôt:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Installer les dépendances:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Exécuter l'application:
```bash
python app_diarize.py
```

L'application sera disponible sur `http://localhost:5001`

## Utilisation

1. Ouvrez votre navigateur web et accédez à `http://localhost:5001`
2. Téléchargez un fichier audio en utilisant l'interface glisser-déposer ou le sélecteur de fichiers
3. Sélectionnez la taille du modèle et le nombre de locuteurs souhaités
4. Attendez que la transcription soit terminée
5. Téléchargez les résultats dans votre format préféré

## Dépannage

- Si le port 5001 est déjà utilisé, vous pouvez modifier le port dans `app_diarize.py`
- Pour les fichiers audio volumineux, envisagez d'utiliser une taille de modèle plus petite pour un traitement plus rapide
- Assurez-vous d'avoir suffisamment d'espace disque pour les fichiers temporaires

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## Auteur

Zhien Li 