# เครื่องมือถอดความเสียงพร้อมการระบุตัวผู้พูด

[English](../../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

แอปพลิเคชันเว็บที่ถอดความไฟล์เสียงโดยอัตโนมัติและระบุผู้พูดที่แตกต่างกันในการสนทนาโดยใช้โมเดล Whisper ของ OpenAI และเทคโนโลยีการระบุตัวผู้พูด

## คุณสมบัติ

- **ส่วนติดต่อผู้ใช้ที่ทันสมัย:**
  * ส่วนติดต่อเว็บที่สะอาดและใช้งานง่ายพร้อมการอัปโหลดไฟล์แบบลากและวาง
  * การติดตามความคืบหน้าแบบเรียลไทม์ระหว่างการประมวลผลการถอดความ
  * การออกแบบที่ตอบสนองทำงานบนอุปกรณ์ต่างๆ
  * รองรับ 18 ภาษาในส่วนติดต่อผู้ใช้

- **เครื่องมือถอดความที่ทรงพลัง:**
  * การผสานกับโมเดลการจดจำเสียงพูด Whisper ของ OpenAI
  * ขนาดโมเดลหลายขนาด (tiny, base, small, medium, large) เพื่อสมดุลระหว่างความเร็วและความแม่นยำ
  * การระบุตัวผู้พูดเพื่อแยกแยะและแยกผู้พูดที่แตกต่างกันในการสนทนา
  * รองรับรูปแบบเสียงที่หลากหลาย (MP3, WAV, OGG, FLAC, M4A)

- **ตัวเลือกการส่งออกที่ยืดหยุ่น:**
  * ดาวน์โหลดการถอดความในหลายรูปแบบ (TXT, JSON, SRT, VTT)
  * การถอดความพร้อมการระบุเวลาและตัวผู้พูด
  * การจัดรูปแบบที่สะอาดสำหรับการอ่านและการประมวลผลหลังที่ง่าย

## การติดตั้ง

1. โคลนที่เก็บ:
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. ติดตั้งการพึ่งพา:
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. รันแอปพลิเคชัน:
```bash
python app_diarize.py
```

แอปพลิเคชันจะพร้อมใช้งานที่ `http://localhost:5001`

## การใช้งาน

1. เปิดเว็บเบราว์เซอร์และไปที่ `http://localhost:5001`
2. อัปโหลดไฟล์เสียงโดยใช้ส่วนติดต่อแบบลากและวางหรือตัวเลือกไฟล์
3. เลือกขนาดโมเดลและจำนวนผู้พูดที่ต้องการ
4. รอให้การถอดความเสร็จสมบูรณ์
5. ดาวน์โหลดผลลัพธ์ในรูปแบบที่คุณต้องการ

## การแก้ไขปัญหา

- หากพอร์ต 5001 ถูกใช้งานอยู่แล้ว คุณสามารถเปลี่ยนพอร์ตใน `app_diarize.py`
- สำหรับไฟล์เสียงขนาดใหญ่ ให้พิจารณาใช้ขนาดโมเดลที่เล็กลงเพื่อการประมวลผลที่เร็วขึ้น
- ตรวจสอบให้แน่ใจว่ามีพื้นที่ดิสก์เพียงพอสำหรับไฟล์ชั่วคราว

## ลิขสิทธิ์

โปรเจกต์นี้ได้รับอนุญาตภายใต้ลิขสิทธิ์ MIT - ดูไฟล์ LICENSE สำหรับรายละเอียด

## ผู้เขียน

Zhien Li 