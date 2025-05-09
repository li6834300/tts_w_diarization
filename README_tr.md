# Konuşmacı Tanıma Özellikli Ses Yazıya Çevirme Aracı

[English](README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

OpenAI'nin Whisper modeli ve konuşmacı tanıma teknolojilerini kullanarak ses dosyalarını otomatik olarak yazıya çeviren ve konuşmalardaki farklı konuşmacıları tanımlayan bir web uygulaması.

## Özellikler

- **Modern Kullanıcı Arayüzü:**
  * Sürükle-bırak dosya yükleme özellikli temiz ve sezgisel web arayüzü
  * Yazıya çevirme işlemi sırasında gerçek zamanlı ilerleme takibi
  * Çeşitli cihazlarda çalışan duyarlı tasarım
  * 18 dilde kullanıcı arayüzü desteği

- **Güçlü Yazıya Çevirme Motoru:**
  * OpenAI'nin Whisper konuşma tanıma modelleriyle entegrasyon
  * Hız ve doğruluk dengesi için çoklu model boyutları (tiny, base, small, medium, large)
  * Konuşmadaki farklı konuşmacıları tanımlamak ve ayırmak için konuşmacı tanıma
  * Çeşitli ses formatları desteği (MP3, WAV, OGG, FLAC, M4A)

- **Esnek Çıktı Seçenekleri:**
  * Birden fazla formatta yazıya çevirme indirme (TXT, JSON, SRT, VTT)
  * Konuşmacı tanıma özellikli zaman damgalı yazıya çevirme
  * Kolay okuma ve sonrası işleme için temiz format

## Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Uygulamayı çalıştırın:
```bash
python app_diarize.py
```

Uygulama `http://localhost:5001` adresinde kullanılabilir olacak

## Kullanım

1. Web tarayıcınızı açın ve `http://localhost:5001` adresine gidin
2. Sürükle-bırak arayüzü veya dosya seçici kullanarak bir ses dosyası yükleyin
3. İstediğiniz model boyutunu ve konuşmacı sayısını seçin
4. Yazıya çevirme işleminin tamamlanmasını bekleyin
5. Sonuçları tercih ettiğiniz formatta indirin

## Sorun Giderme

- Port 5001 zaten kullanımdaysa, `app_diarize.py` dosyasında portu değiştirebilirsiniz
- Büyük ses dosyaları için daha hızlı işleme için daha küçük bir model boyutu kullanmayı düşünün
- Geçici dosyalar için yeterli disk alanınız olduğundan emin olun

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

## Yazar

Zhien Li 