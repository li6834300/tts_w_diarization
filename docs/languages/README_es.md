# Herramienta de Transcripción de Audio con Diarización de Hablantes

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Una aplicación web que transcribe automáticamente archivos de audio e identifica diferentes hablantes en conversaciones utilizando el modelo Whisper de OpenAI y tecnologías de diarización.

## Características

- **Interfaz de Usuario Moderna:**
  * Interfaz web limpia e intuitiva con carga de archivos por arrastrar y soltar
  * Seguimiento en tiempo real del progreso durante el procesamiento de la transcripción
  * Diseño responsivo que funciona en varios dispositivos
  * Soporte para 18 idiomas en la interfaz de usuario

- **Potente Motor de Transcripción:**
  * Integración con modelos de reconocimiento de voz Whisper de OpenAI
  * Múltiples tamaños de modelo (tiny, base, small, medium, large) para equilibrar velocidad y precisión
  * Diarización para identificar y separar diferentes hablantes en la conversación
  * Soporte para varios formatos de audio (MP3, WAV, OGG, FLAC, M4A)

- **Opciones de Salida Flexibles:**
  * Descarga de transcripciones en múltiples formatos (TXT, JSON, SRT, VTT)
  * Transcripciones con marcas de tiempo e identificación de hablantes
  * Formato limpio para fácil lectura y post-procesamiento

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Ejecutar la aplicación:
```bash
python app_diarize.py
```

La aplicación estará disponible en `http://localhost:5001`

## Uso

1. Abra su navegador web y navegue a `http://localhost:5001`
2. Suba un archivo de audio usando la interfaz de arrastrar y soltar o el selector de archivos
3. Seleccione el tamaño del modelo y el número de hablantes deseados
4. Espere a que se complete la transcripción
5. Descargue los resultados en su formato preferido

## Solución de Problemas

- Si el puerto 5001 ya está en uso, puede modificar el puerto en `app_diarize.py`
- Para archivos de audio grandes, considere usar un tamaño de modelo más pequeño para un procesamiento más rápido
- Asegúrese de tener suficiente espacio en disco para archivos temporales

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE para más detalles.

## Autor

Zhien Li 