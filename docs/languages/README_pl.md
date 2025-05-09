# Narzędzie do Transkrypcji Audio z Identyfikacją Mówców

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Aplikacja internetowa, która automatycznie transkrybuje pliki audio i identyfikuje różnych mówców w rozmowach przy użyciu modelu Whisper od OpenAI i technologii diaryzacji.

## Funkcje

- **Nowoczesny Interfejs Użytkownika:**
  * Czysty i intuicyjny interfejs internetowy z możliwością przeciągania i upuszczania plików
  * Śledzenie postępu w czasie rzeczywistym podczas przetwarzania transkrypcji
  * Responsywny design działający na różnych urządzeniach
  * Wsparcie dla 18 języków w interfejsie użytkownika

- **Potężny Silnik Transkrypcji:**
  * Integracja z modelami rozpoznawania mowy Whisper od OpenAI
  * Wiele rozmiarów modeli (tiny, base, small, medium, large) dla zbalansowania prędkości i dokładności
  * Diaryzacja do identyfikacji i rozdzielania różnych mówców w rozmowie
  * Wsparcie dla różnych formatów audio (MP3, WAV, OGG, FLAC, M4A)

- **Elastyczne Opcje Wyjściowe:**
  * Pobieranie transkrypcji w wielu formatach (TXT, JSON, SRT, VTT)
  * Transkrypcje ze znacznikami czasu i identyfikacją mówców
  * Czysty format dla łatwego czytania i przetwarzania

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Uruchom aplikację:
```bash
python app_diarize.py
```

Aplikacja będzie dostępna pod adresem `http://localhost:5001`

## Użycie

1. Otwórz przeglądarkę internetową i przejdź do `http://localhost:5001`
2. Prześlij plik audio używając interfejsu przeciągania i upuszczania lub selektora plików
3. Wybierz rozmiar modelu i żądaną liczbę mówców
4. Poczekaj na zakończenie transkrypcji
5. Pobierz wyniki w preferowanym formacie

## Rozwiązywanie Problemów

- Jeśli port 5001 jest już używany, możesz zmienić port w `app_diarize.py`
- Dla dużych plików audio rozważ użycie mniejszego rozmiaru modelu dla szybszego przetwarzania
- Upewnij się, że masz wystarczająco dużo miejsca na dysku dla plików tymczasowych

## Licencja

Ten projekt jest objęty licencją MIT - zobacz plik LICENSE, aby uzyskać szczegóły.

## Autor

Zhien Li 