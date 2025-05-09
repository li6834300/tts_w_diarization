# Transcripción de Audio con Identificación de Hablantes

Una aplicación web que transcribe archivos de audio e identifica diferentes hablantes en la conversación utilizando el modelo Whisper de OpenAI y tecnologías de diarización de hablantes.

## Características

- Carga de archivos de audio (MP3, WAV, OGG, FLAC, M4A)
- Transcripción de voz utilizando el modelo Whisper de OpenAI (varios tamaños disponibles)
- Identificación y separación de diferentes hablantes en el audio
- Descarga de resultados en múltiples formatos (TXT, JSON, SRT, VTT)
- Seguimiento de progreso en tiempo real
- Interfaz de usuario limpia y moderna
- Soporte para diferentes tamaños de modelo Whisper para equilibrar velocidad y precisión
- Interfaz multilingüe con soporte para 18 idiomas incluyendo inglés, español, francés, alemán, chino, japonés, coreano, ruso, árabe, hindi, portugués, italiano, holandés, turco, vietnamita, tailandés, polaco y sueco

## Demostración

![Captura de pantalla de la aplicación](docs/screenshot.png)

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.8 o más reciente
- FFmpeg (requerido para el procesamiento de audio)
- Git (opcional, para clonar el repositorio)

## Instalación

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

O descarga y extrae el archivo ZIP del repositorio.

### Paso 2: Crear un entorno virtual (recomendado)

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### Paso 3: Instalar paquetes requeridos

```bash
pip install -r requirements.txt
```

Si no tienes un archivo `requirements.txt`, puedes crear uno con el siguiente contenido:

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

O instala los paquetes directamente:

```bash
pip install flask numpy torch torchaudio pyannote.audio openai-whisper pydub webrtcvad
```

### Paso 4: Instalar FFmpeg

#### En macOS (usando Homebrew):

```bash
brew install ffmpeg
```

#### En Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### En Windows:

1. Descarga FFmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extrae los archivos
3. Añade la carpeta bin a tu variable de entorno PATH

### Paso 5: Iniciar la aplicación

Puedes ejecutar la aplicación usando:

```bash
# Usando python
python app_diarize.py

# O usando python3 explícitamente (recomendado en macOS/Linux)
python3 app_diarize.py
```

Si necesitas usar un puerto diferente (por ejemplo, si el puerto 5001 ya está en uso):

```bash
# Edita app_diarize.py y cambia el número de puerto
# Encuentra esta línea al final del archivo:
# app.run(debug=True, host="0.0.0.0", port=5001)
# Cambia 5001 por el puerto deseado, por ejemplo 5002

# O puedes especificar el puerto directamente al ejecutar:
python3 -c "import app_diarize; app_diarize.app.run(debug=True, host='0.0.0.0', port=5002)"
```

La aplicación estará disponible en http://localhost:5001 (o el puerto que hayas configurado).

### Uso por línea de comandos (sin interfaz web)

También puedes usar el script directamente desde la línea de comandos sin iniciar la aplicación web:

```bash
# Uso básico
python3 whisper_diarize.py --audio /ruta/a/tu/archivo/audio.mp3 --model base

# Ejemplo con más opciones
python3 whisper_diarize.py --audio /ruta/a/tu/archivo/audio.mp3 --model large --num_speakers 2
```

Opciones comunes de línea de comandos:
- `--audio`: Ruta al archivo de audio (requerido)
- `--model`: Tamaño del modelo Whisper (tiny, base, small, medium, large) - por defecto es base
- `--num_speakers`: Número de hablantes en el audio (por defecto es 2)
- `--output_dir`: Directorio para guardar las salidas de transcripción (por defecto es "transcriptions")

Este uso directo por línea de comandos es útil para el procesamiento por lotes o cuando no necesitas la interfaz web.

## Uso

1. Abre la aplicación en tu navegador web
2. Arrastra y suelta un archivo de audio o haz clic en "Explorar archivos" para seleccionar uno
3. Elige el tamaño del modelo Whisper:
   - Tiny: El más rápido pero menos preciso
   - Base: Buen equilibrio para la mayoría de propósitos
   - Small: Más preciso pero más lento
   - Medium: Alta precisión, procesamiento más lento
   - Large-v2: El más preciso, requiere más recursos
4. Establece el número de hablantes en el audio (si se conoce)
5. Haz clic en "Transcribir" y espera el procesamiento
6. Visualiza los resultados y descárgalos en tu formato preferido

## Problemas comunes y solución de problemas

### "Address already in use" / El puerto 5000 o 5001 está en uso

Esto ocurre cuando otra aplicación está utilizando el puerto. Puedes:

1. Cambiar el puerto en `app_diarize.py`:

```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)  # Cambiar a otro puerto
```

2. En macOS, el puerto 5000 a menudo es utilizado por AirPlay Receiver. Puedes desactivarlo en Preferencias del Sistema → General → AirDrop y Handoff.

### FFmpeg no encontrado

Asegúrate de que FFmpeg esté instalado y disponible en tu PATH:

```bash
# Comprobar si FFmpeg está instalado
ffmpeg -version
```

Si no muestra información de la versión, reinstala FFmpeg siguiendo las instrucciones de instalación anteriores.

### Problemas con CUDA/GPU

Si estás intentando usar aceleración GPU pero encuentras errores:

1. Asegúrate de tener una GPU compatible
2. Instala la versión correcta de PyTorch para tu versión de CUDA:

```bash
# Para CUDA 11.8
pip install torch==2.0.0+cu118 torchaudio==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

### Errores de importación para pyannote.audio

Si encuentras problemas al instalar o importar pyannote.audio:

```bash
# Intenta instalar desde la fuente
pip install git+https://github.com/pyannote/pyannote-audio.git
```

### "No module named 'whisper_diarize'"

Asegúrate de que el archivo `whisper_diarize.py` esté en el mismo directorio que `app_diarize.py`.

## Personalización

### Cambiar el tamaño máximo de carga

Edita `app_diarize.py` y modifica el parámetro `MAX_CONTENT_LENGTH`:

```python
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100 MB
```

### Cambiar la apariencia de la interfaz

Edita el CSS en `templates/diarize.html` para personalizar colores, fuentes y diseño.

## Internacionalización

La aplicación soporta 18 idiomas:
- Inglés (English)
- Español
- Francés (Français)
- Alemán (Deutsch)
- Chino (中文)
- Japonés (日本語)
- Coreano (한국어)
- Ruso (Русский)
- Árabe (العربية)
- Hindi (हिन्दी)
- Portugués (Português)
- Italiano (Italiano)
- Holandés (Nederlands)
- Turco (Türkçe)
- Vietnamita (Tiếng Việt)
- Tailandés (ไทย)
- Polaco (Polski)
- Sueco (Svenska)

Los usuarios pueden cambiar el idioma usando el selector de idioma en la esquina superior derecha de la interfaz. Todos los elementos de la interfaz se traducirán al idioma seleccionado.

### Añadir más idiomas

Para añadir más idiomas, edita el archivo `templates/diarize.html`:

1. Añade una nueva opción al desplegable del selector de idioma:
```html
<option value="codigo-idioma">Nombre del Idioma</option>
```

2. Añade traducciones al objeto `translations` en la sección JavaScript:
```javascript
codigo-idioma: {
    title: "Título Traducido",
    dragDrop: "Texto traducido para arrastrar y soltar",
    // Añade todas las demás traducciones requeridas
}
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## Agradecimientos

- [OpenAI Whisper](https://github.com/openai/whisper) por el modelo de reconocimiento de voz
- [Pyannote Audio](https://github.com/pyannote/pyannote-audio) por la diarización de hablantes
- Flask por el framework web

## Autor

Zhien Li
- GitHub: [li6834300](https://github.com/li6834300)
- LinkedIn: [zhienli277](https://www.linkedin.com/in/zhienli277/) 