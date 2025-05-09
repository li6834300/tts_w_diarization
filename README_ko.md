# 화자 분리 기능이 있는 오디오 변환 도구

[English](README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

OpenAI의 Whisper 모델과 화자 분리 기술을 사용하여 오디오 파일을 자동으로 변환하고 대화에서 다른 화자를 식별하는 웹 애플리케이션입니다.

## 기능

- **현대적인 사용자 인터페이스:**
  * 드래그 앤 드롭 파일 업로드가 가능한 깔끔하고 직관적인 웹 인터페이스
  * 변환 처리 중 실시간 진행 상황 추적
  * 다양한 기기에서 작동하는 반응형 디자인
  * 18개 언어의 사용자 인터페이스 지원

- **강력한 변환 엔진:**
  * OpenAI의 Whisper 음성 인식 모델 통합
  * 속도와 정확도의 균형을 위한 다양한 모델 크기 (tiny, base, small, medium, large)
  * 대화에서 다른 화자를 식별하고 분리하는 화자 분리 기능
  * 다양한 오디오 형식 지원 (MP3, WAV, OGG, FLAC, M4A)

- **유연한 출력 옵션:**
  * 여러 형식으로 변환 결과 다운로드 (TXT, JSON, SRT, VTT)
  * 화자 식별이 포함된 타임스탬프 변환
  * 읽기 쉽고 후처리가 용이한 깔끔한 형식

## 설치

1. 저장소 복제:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. 의존성 설치:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. 애플리케이션 실행:
```bash
python app_diarize.py
```

애플리케이션은 `http://localhost:5001`에서 사용할 수 있습니다

## 사용 방법

1. 웹 브라우저를 열고 `http://localhost:5001`로 이동
2. 드래그 앤 드롭 인터페이스 또는 파일 선택기를 사용하여 오디오 파일 업로드
3. 원하는 모델 크기와 화자 수 선택
4. 변환이 완료될 때까지 대기
5. 원하는 형식으로 결과 다운로드

## 문제 해결

- 포트 5001이 이미 사용 중인 경우 `app_diarize.py`에서 포트를 수정할 수 있습니다
- 큰 오디오 파일의 경우 더 빠른 처리를 위해 작은 모델 크기 사용을 고려하세요
- 임시 파일을 위한 충분한 디스크 공간이 있는지 확인하세요

## 라이선스

이 프로젝트는 MIT 라이선스 하에 제공됩니다 - 자세한 내용은 LICENSE 파일을 참조하세요.

## 작성자

이지은 