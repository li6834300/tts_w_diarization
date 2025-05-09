# 带说话人识别的音频转录工具

[English](../../README.md) | [中文](README_zh.md) | [Nederlands](README_nl.md) | [Español](README_es.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md) | [Português](README_pt.md) | [Italiano](README_it.md) | [Türkçe](README_tr.md) | [Tiếng Việt](README_vi.md) | [ไทย](README_th.md) | [Polski](README_pl.md) | [Svenska](README_sv.md)

一个使用 OpenAI 的 Whisper 模型和说话人识别技术自动转录音频文件并识别不同说话人的网络应用程序。

## 功能特点

- **现代化用户界面：**
  * 简洁直观的网页界面，支持拖放文件上传
  * 转录处理过程中实时进度跟踪
  * 响应式设计，适配各种设备
  * 支持18种语言的用户界面

- **强大的转录引擎：**
  * 集成 OpenAI 的 Whisper 语音识别模型
  * 多种模型大小（tiny、base、small、medium、large）以平衡速度和准确性
  * 说话人识别功能，可识别和区分对话中的不同说话人
  * 支持多种音频格式（MP3、WAV、OGG、FLAC、M4A）

- **灵活的输出选项：**
  * 支持多种格式下载转录结果（TXT、JSON、SRT、VTT）
  * 带时间戳的转录文本，包含说话人识别
  * 清晰的格式，便于阅读和后处理

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/li6834300/tts_w_diarization.git
cd tts_w_diarization
```

2. 安装依赖：
```bash
pip install -r requirements.txt
pip install -r requirements_whisperx.txt
```

3. 运行应用：
```bash
python app_diarize.py
```

应用将在 `http://localhost:5001` 上运行

## 使用方法

1. 打开网页浏览器，访问 `http://localhost:5001`
2. 使用拖放界面或文件选择器上传音频文件
3. 选择所需的模型大小和说话人数量
4. 等待转录完成
5. 以首选格式下载结果

## 故障排除

- 如果端口5001已被占用，可以在 `app_diarize.py` 中修改端口
- 对于大型音频文件，建议使用较小的模型大小以加快处理速度
- 确保有足够的磁盘空间用于临时文件

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 作者

李志恩 