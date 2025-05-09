# Ferramenta de Transcrição de Áudio com Diarização de Locutores

[English](../../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Uma aplicação web que transcreve automaticamente arquivos de áudio e identifica diferentes locutores em conversas usando o modelo Whisper da OpenAI e tecnologias de diarização.

## Recursos

- **Interface de Usuário Moderna:**
  * Interface web limpa e intuitiva com upload de arquivos por arrastar e soltar
  * Acompanhamento em tempo real do progresso durante o processamento da transcrição
  * Design responsivo que funciona em vários dispositivos
  * Suporte para 18 idiomas na interface do usuário

- **Motor de Transcrição Poderoso:**
  * Integração com modelos de reconhecimento de fala Whisper da OpenAI
  * Múltiplos tamanhos de modelo (tiny, base, small, medium, large) para equilibrar velocidade e precisão
  * Diarização para identificar e separar diferentes locutores na conversa
  * Suporte para vários formatos de áudio (MP3, WAV, OGG, FLAC, M4A)

- **Opções de Saída Flexíveis:**
  * Download de transcrições em múltiplos formatos (TXT, JSON, SRT, VTT)
  * Transcrições com marcação de tempo e identificação de locutores
  * Formatação limpa para fácil leitura e pós-processamento

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Execute a aplicação:
```bash
python app_diarize.py
```

A aplicação estará disponível em `http://localhost:5001`

## Uso

1. Abra seu navegador web e acesse `http://localhost:5001`
2. Faça upload de um arquivo de áudio usando a interface de arrastar e soltar ou o seletor de arquivos
3. Selecione o tamanho do modelo e o número desejado de locutores
4. Aguarde a conclusão da transcrição
5. Baixe os resultados no seu formato preferido

## Solução de Problemas

- Se a porta 5001 já estiver em uso, você pode modificar a porta em `app_diarize.py`
- Para arquivos de áudio grandes, considere usar um tamanho de modelo menor para processamento mais rápido
- Certifique-se de ter espaço suficiente em disco para arquivos temporários

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Autor

Zhien Li 