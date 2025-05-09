# Transcription Audio avec Identification des Locuteurs

Une application web qui transcrit les fichiers audio et identifie différents locuteurs dans la conversation en utilisant le modèle Whisper d'OpenAI et les technologies de diarisation des locuteurs.

## Fonctionnalités

- Téléchargement de fichiers audio (MP3, WAV, OGG, FLAC, M4A)
- Transcription de la parole à l'aide du modèle Whisper d'OpenAI (différentes tailles disponibles)
- Identification et séparation des différents locuteurs dans l'audio
- Téléchargement des résultats dans plusieurs formats (TXT, JSON, SRT, VTT)
- Suivi de la progression en temps réel
- Interface utilisateur propre et moderne
- Prise en charge de différentes tailles de modèle Whisper pour équilibrer vitesse et précision
- Interface multilingue avec prise en charge de 18 langues, dont l'anglais, l'espagnol, le français, l'allemand, le chinois, le japonais, le coréen, le russe, l'arabe, l'hindi, le portugais, l'italien, le néerlandais, le turc, le vietnamien, le thaï, le polonais et le suédois

## Démonstration

![Capture d'écran de l'application](docs/screenshot.png)

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants:

- Python 3.8 ou plus récent
- FFmpeg (requis pour le traitement audio)
- Git (facultatif, pour cloner le dépôt)

## Installation

### Étape 1: Cloner le dépôt

```bash
git clone https://github.com/yourusername/tts_w_diarization.git
cd tts_w_diarization
```

Ou téléchargez et extrayez le fichier ZIP du dépôt.

### Étape 2: Créer un environnement virtuel (recommandé)

```bash
python -m venv venv

# Sur Windows
venv\Scripts\activate

# Sur macOS/Linux
source venv/bin/activate
```

### Étape 3: Installer les packages requis

```bash
pip install -r requirements.txt
```

Si vous n'avez pas de fichier `requirements.txt`, vous pouvez en créer un avec le contenu suivant:

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

Ou installez les packages directement:

```bash
pip install flask numpy torch torchaudio pyannote.audio openai-whisper pydub webrtcvad
```

### Étape 4: Installer FFmpeg

#### Sur macOS (avec Homebrew):

```bash
brew install ffmpeg
```

#### Sur Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### Sur Windows:

1. Téléchargez FFmpeg depuis [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extrayez les fichiers
3. Ajoutez le dossier bin à votre variable d'environnement PATH

### Étape 5: Démarrer l'application

```bash
python app_diarize.py
```

L'application sera disponible à l'adresse http://localhost:5001 (ou le port que vous avez configuré).

## Utilisation

1. Ouvrez l'application dans votre navigateur web
2. Faites glisser-déposer un fichier audio ou cliquez sur "Parcourir les fichiers" pour en sélectionner un
3. Choisissez la taille du modèle Whisper:
   - Tiny: Le plus rapide mais le moins précis
   - Base: Bon équilibre pour la plupart des usages
   - Small: Plus précis mais plus lent
   - Medium: Haute précision, traitement plus lent
   - Large-v2: Le plus précis, nécessite plus de ressources
4. Définissez le nombre de locuteurs dans l'audio (si connu)
5. Cliquez sur "Transcrire" et attendez le traitement
6. Consultez les résultats et téléchargez-les dans votre format préféré

## Problèmes courants et dépannage

### "Address already in use" / Le port 5000 ou 5001 est déjà utilisé

Cela se produit lorsqu'une autre application utilise le port. Vous pouvez:

1. Changer le port dans `app_diarize.py`:

```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)  # Changer pour un autre port
```

2. Sur macOS, le port 5000 est souvent utilisé par AirPlay Receiver. Vous pouvez le désactiver dans Préférences Système → Général → AirDrop et Handoff.

### FFmpeg introuvable

Assurez-vous que FFmpeg est installé et disponible dans votre PATH:

```bash
# Vérifier si FFmpeg est installé
ffmpeg -version
```

S'il n'affiche pas les informations de version, réinstallez FFmpeg en suivant les instructions d'installation ci-dessus.

### Problèmes CUDA/GPU

Si vous essayez d'utiliser l'accélération GPU mais rencontrez des erreurs:

1. Assurez-vous d'avoir un GPU compatible
2. Installez la version correcte de PyTorch pour votre version de CUDA:

```bash
# Pour CUDA 11.8
pip install torch==2.0.0+cu118 torchaudio==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

### Erreurs d'importation pour pyannote.audio

Si vous rencontrez des problèmes lors de l'installation ou de l'importation de pyannote.audio:

```bash
# Essayez d'installer à partir de la source
pip install git+https://github.com/pyannote/pyannote-audio.git
```

### "No module named 'whisper_diarize'"

Assurez-vous que le fichier `whisper_diarize.py` est dans le même répertoire que `app_diarize.py`.

## Personnalisation

### Modifier la taille maximale de téléchargement

Modifiez `app_diarize.py` et changez le paramètre `MAX_CONTENT_LENGTH`:

```python
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100 MB
```

### Modifier l'apparence de l'interface

Modifiez le CSS dans `templates/diarize.html` pour personnaliser les couleurs, les polices et la mise en page.

## Internationalisation

L'application prend en charge 18 langues:
- Anglais (English)
- Espagnol (Español)
- Français
- Allemand (Deutsch)
- Chinois (中文)
- Japonais (日本語)
- Coréen (한국어)
- Russe (Русский)
- Arabe (العربية)
- Hindi (हिन्दी)
- Portugais (Português)
- Italien (Italiano)
- Néerlandais (Nederlands)
- Turc (Türkçe)
- Vietnamien (Tiếng Việt)
- Thaï (ไทย)
- Polonais (Polski)
- Suédois (Svenska)

Les utilisateurs peuvent changer de langue à l'aide du sélecteur de langue situé dans le coin supérieur droit de l'interface. Tous les éléments de l'interface seront traduits dans la langue sélectionnée.

### Ajouter d'autres langues

Pour ajouter d'autres langues, modifiez le fichier `templates/diarize.html`:

1. Ajoutez une nouvelle option au menu déroulant du sélecteur de langue:
```html
<option value="code-langue">Nom de la Langue</option>
```

2. Ajoutez des traductions à l'objet `translations` dans la section JavaScript:
```javascript
code-langue: {
    title: "Titre Traduit",
    dragDrop: "Texte traduit pour glisser-déposer",
    // Ajoutez toutes les autres traductions requises
}
```

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## Remerciements

- [OpenAI Whisper](https://github.com/openai/whisper) pour le modèle de reconnaissance vocale
- [Pyannote Audio](https://github.com/pyannote/pyannote-audio) pour la diarisation des locuteurs
- Flask pour le framework web

## Auteur

Zhien Li
- GitHub: [li6834300](https://github.com/li6834300)
- LinkedIn: [zhienli277](https://www.linkedin.com/in/zhienli277/) 