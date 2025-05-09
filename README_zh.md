# 带有说话者分离的语音转文字工具

一个网络应用程序，使用OpenAI的Whisper模型和说话者分离技术来转录音频文件并识别对话中的不同说话者。

## 功能特点

- 上传音频文件（MP3、WAV、OGG、FLAC、M4A）
- 使用OpenAI的Whisper模型转录语音（提供多种模型大小）
- 识别并区分音频中的不同说话者
- 以多种格式下载结果（TXT、JSON、SRT、VTT）
- 实时进度跟踪
- 清晰现代的用户界面
- 支持不同Whisper模型大小，平衡速度和准确性
- 多语言界面，支持18种语言，包括英语、西班牙语、法语、德语、中文、日语、韩语、俄语、阿拉伯语、印地语、葡萄牙语、意大利语、荷兰语、土耳其语、越南语、泰语、波兰语和瑞典语

## 演示

![应用截图](docs/screenshot.png)

## 前提条件

开始之前，请确保已安装以下内容：

- Python 3.8或更新版本
- FFmpeg（音频处理所需）
- Git（可选，用于克隆仓库）

## 安装

### 步骤1：克隆仓库

```bash
git clone https://github.com/yourusername/tts_w_diarization.git
cd tts_w_diarization
```

或从仓库下载并解压ZIP文件。

### 步骤2：创建虚拟环境（推荐）

```bash
python -m venv venv

# Windows系统
venv\Scripts\activate

# macOS/Linux系统
source venv/bin/activate
```

### 步骤3：安装所需包

```bash
pip install -r requirements.txt
```

如果没有`requirements.txt`文件，可以创建一个包含以下内容的文件：

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

或直接安装这些包：

```bash
pip install flask numpy torch torchaudio pyannote.audio openai-whisper pydub webrtcvad
```

### 步骤4：安装FFmpeg

#### 在macOS上（使用Homebrew）：

```bash
brew install ffmpeg
```

#### 在Ubuntu/Debian上：

```bash
sudo apt update
sudo apt install ffmpeg
```

#### 在Windows上：

1. 从[ffmpeg.org](https://ffmpeg.org/download.html)下载FFmpeg
2. 解压文件
3. 将bin文件夹添加到PATH环境变量

### 步骤5：启动应用程序

```bash
python app_diarize.py
```

应用程序将在http://localhost:5001（或您配置的端口）上可用。

## 使用方法

1. 在网络浏览器中打开应用程序
2. 拖放音频文件或点击"浏览文件"选择一个
3. 选择Whisper模型大小：
   - Tiny：最快但精度最低
   - Base：适合大多数用途的良好平衡
   - Small：更准确但更慢
   - Medium：高精度，处理更慢
   - Large-v2：最准确，需要更多资源
4. 设置音频中的说话者数量（如果已知）
5. 点击"转录"并等待处理
6. 查看结果并以您喜欢的格式下载

## 常见问题和故障排除

### "Address already in use" / 端口5000或5001正在使用中

这发生在另一个应用程序正在使用该端口时。您可以：

1. 在`app_diarize.py`中更改端口：

```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)  # 更改为另一个端口
```

2. 在macOS上，端口5000经常被AirPlay接收器使用。您可以在系统偏好设置→通用→隔空投送和接力中禁用它。

### 找不到FFmpeg

确保FFmpeg已安装并在您的PATH中可用：

```bash
# 检查FFmpeg是否安装
ffmpeg -version
```

如果没有显示版本信息，请按照上述安装说明重新安装FFmpeg。

### CUDA/GPU问题

如果您尝试使用GPU加速但遇到错误：

1. 确保您有兼容的GPU
2. 为您的CUDA版本安装正确版本的PyTorch：

```bash
# 对于CUDA 11.8
pip install torch==2.0.0+cu118 torchaudio==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```

### pyannote.audio的导入错误

如果您在安装或导入pyannote.audio时遇到问题：

```bash
# 尝试从源代码安装
pip install git+https://github.com/pyannote/pyannote-audio.git
```

### "No module named 'whisper_diarize'"

确保`whisper_diarize.py`文件与`app_diarize.py`在同一目录中。

## 自定义

### 更改最大上传大小

编辑`app_diarize.py`并修改`MAX_CONTENT_LENGTH`参数：

```python
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100 MB
```

### 更改界面外观

编辑`templates/diarize.html`中的CSS来自定义颜色、字体和布局。

## 国际化

应用程序支持18种语言：
- 英语（English）
- 西班牙语（Español）
- 法语（Français）
- 德语（Deutsch）
- 中文
- 日语（日本語）
- 韩语（한국어）
- 俄语（Русский）
- 阿拉伯语（العربية）
- 印地语（हिन्दी）
- 葡萄牙语（Português）
- 意大利语（Italiano）
- 荷兰语（Nederlands）
- 土耳其语（Türkçe）
- 越南语（Tiếng Việt）
- 泰语（ไทย）
- 波兰语（Polski）
- 瑞典语（Svenska）

用户可以使用界面右上角的语言选择器更改语言。所有UI元素将翻译为所选语言。

### 添加更多语言

要添加更多语言，编辑`templates/diarize.html`文件：

1. 向语言选择器下拉菜单添加新选项：
```html
<option value="language-code">语言名称</option>
```

2. 向JavaScript部分的`translations`对象添加翻译：
```javascript
language-code: {
    title: "翻译后的标题",
    dragDrop: "翻译后的拖放文本",
    // 添加所有其他必需的翻译
}
```

## 许可证

本项目采用MIT许可证 - 详情请参阅LICENSE文件。

## 致谢

- [OpenAI Whisper](https://github.com/openai/whisper)提供语音识别模型
- [Pyannote Audio](https://github.com/pyannote/pyannote-audio)提供说话者分离
- Flask提供Web框架

## 作者

Zhien Li
- GitHub: [li6834300](https://github.com/li6834300)
- LinkedIn: [zhienli277](https://www.linkedin.com/in/zhienli277/) 