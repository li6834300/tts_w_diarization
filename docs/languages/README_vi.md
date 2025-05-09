# Công Cụ Chuyển Đổi Âm Thanh với Nhận Diện Người Nói

[English](../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

Ứng dụng web tự động chuyển đổi các tệp âm thanh và xác định các người nói khác nhau trong cuộc hội thoại bằng cách sử dụng mô hình Whisper của OpenAI và công nghệ nhận diện người nói.

## Tính Năng

- **Giao Diện Người Dùng Hiện Đại:**
  * Giao diện web sạch sẽ và trực quan với tính năng tải lên tệp kéo và thả
  * Theo dõi tiến trình thời gian thực trong quá trình xử lý chuyển đổi
  * Thiết kế đáp ứng hoạt động trên nhiều thiết bị
  * Hỗ trợ 18 ngôn ngữ trong giao diện người dùng

- **Công Cụ Chuyển Đổi Mạnh Mẽ:**
  * Tích hợp với các mô hình nhận dạng giọng nói Whisper của OpenAI
  * Nhiều kích thước mô hình (tiny, base, small, medium, large) để cân bằng tốc độ và độ chính xác
  * Nhận diện người nói để xác định và phân tách các người nói khác nhau trong cuộc hội thoại
  * Hỗ trợ nhiều định dạng âm thanh (MP3, WAV, OGG, FLAC, M4A)

- **Tùy Chọn Đầu Ra Linh Hoạt:**
  * Tải xuống bản chuyển đổi ở nhiều định dạng (TXT, JSON, SRT, VTT)
  * Bản chuyển đổi có dấu thời gian và nhận diện người nói
  * Định dạng sạch sẽ để dễ đọc và xử lý sau

## Cài Đặt

1. Sao chép kho lưu trữ:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. Cài đặt các phụ thuộc:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. Chạy ứng dụng:
```bash
python app_diarize.py
```

Ứng dụng sẽ có sẵn tại `http://localhost:5001`

## Sử Dụng

1. Mở trình duyệt web và truy cập `http://localhost:5001`
2. Tải lên tệp âm thanh bằng giao diện kéo và thả hoặc bộ chọn tệp
3. Chọn kích thước mô hình và số lượng người nói mong muốn
4. Đợi quá trình chuyển đổi hoàn tất
5. Tải xuống kết quả ở định dạng bạn muốn

## Xử Lý Sự Cố

- Nếu cổng 5001 đã được sử dụng, bạn có thể thay đổi cổng trong `app_diarize.py`
- Đối với tệp âm thanh lớn, hãy cân nhắc sử dụng kích thước mô hình nhỏ hơn để xử lý nhanh hơn
- Đảm bảo có đủ dung lượng ổ đĩa cho các tệp tạm thời

## Giấy Phép

Dự án này được cấp phép theo Giấy phép MIT - xem tệp LICENSE để biết thêm chi tiết.

## Tác Giả

Zhien Li 