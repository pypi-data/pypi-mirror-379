# AkumaSubtitler 🎥✍️

**The ultimate tool for adding professional subtitles to your videos effortlessly.**

![AkumaSubtitler Logo](https://github.com/akumanomi1988/AkumaSubtitler/blob/main/Designer.png?raw=true)

![Status](https://img.shields.io/badge/STATUS-IN%20DEVELOPMENT-green)
![GitHub Stars](https://img.shields.io/github/stars/Akumanomi1988/AkumaSubtitler?style=social)
![License](https://img.shields.io/github/license/Akumanomi1988/AkumaSubtitler)

---

## Table of Contents 📑

- [Features](#features-✨)
- [Installation](#installation-📦)
- [Quick Start](#quick-start-🚀)
- [Customization Options](#customization-options-🎨)
  - [Subtitle Styling (`SubStyle` Class)](#subtitle-styling-substyle-class)
  - [Audio Mixing](#audio-mixing)
- [Whisper Models](#whisper-models-🧠)
- [Advanced Usage](#advanced-usage-🔧)
  - [Register Custom Effects](#register-custom-effects)
  - [Batch Processing](#batch-processing)
- [System Requirements](#system-requirements-💻)
- [Contributing](#contributing-🤝)
- [License](#license-📄)
- [Support](#support-🆘)
- [Links](#links-🔗)

---

## Features ✨

- 🎙 **AI-Powered Subtitles**: Automatically generate subtitles using OpenAI’s Whisper.
- 🎨 **Custom Styling**: Full control over subtitle appearance, including fonts, colors, and positioning.
- 🔊 **Audio Mixing**: Seamlessly blend original audio with new narration tracks.
- ⚡ **Fast Processing**: Hardware-accelerated video processing with FFmpeg.
- 🌐 **Multi-Source Support**: Works with local files and remote URLs.
- 🔧 **Extensible Framework**: Easily add custom effects and styles to suit your needs.

---

## Installation 📦

Install AkumaSubtitler using pip:

```bash
pip install akumasubtitler
```

> [!NOTE]
> **Python Requirement**: AkumaSubtitler requires Python **3.10+**. Make sure you have the correct version installed.

---

## Quick Start 🚀

Here’s how to get started with AkumaSubtitler:

```python
from akuma import AkumaSubtitler

# Initialize the subtitler
akuma = AkumaSubtitler()

# Basic usage with auto-generated subtitles
akuma.forge_video(
    video_path="input_video.mp4",
    output_path="output_video.mp4"
)
```

For advanced usage with custom styling:

```python
from akuma import AkumaSubtitler, SubStyle

# Initialize the subtitler
akuma = AkumaSubtitler()

# Define a custom subtitle style
custom_style = SubStyle(
    font_name="Arial",
    font_size=28,
    primary_color="#FF4500",  # Orange-red
    border=3
)

# Apply the custom style to the video
akuma.forge_video(
    video_path="input.mp4",
    output_path="styled_output.mp4",
    audio_path="narration.mp3",
    style=custom_style
)
```

---

## Customization Options 🎨

### Subtitle Styling (`SubStyle` Class)

Modify subtitle appearance:

```python
from akuma import SubStyle

# Example of a custom style
custom_style = SubStyle(
    font_name="Impact",
    font_size=24,
    primary_color="yellow",
    border=3,
    alignment="center",
    margin_v=50  # Vertical position
)
```

### Audio Mixing

Adjust audio levels when adding narration:

```python
akuma.forge_video(
    video_path="input.mp4",
    output_path="output.mp4",
    audio_path="narration.mp3",
    original_audio_volume=0.3,  # 30% original audio
    new_audio_volume=0.7        # 70% new narration
)
```

---

## Whisper Models 🧠

Choose the right Whisper model for your needs:

| Model Size | Speed | Accuracy | Use Case                     |
|------------|-------|----------|------------------------------|
| `tiny`     | ⚡ Fast | Low      | Quick drafts                 |
| `base`     | 🚀 Fast | Medium   | General-purpose (default)    |

> [!WARNING]
> Larger models provide better accuracy but require significantly more processing power.

---

## Advanced Usage 🔧

### Register Custom Effects

You can define custom effects and apply them to your videos:

```python
from akuma import AkumaSubtitler

@AkumaSubtitler.register_effect("custom_effect")
def custom_effect(image, progress, config):
    # Your custom effect logic here
    return transformed_image
```

### Batch Processing

If you need to process multiple videos:

```python
videos = ["video1.mp4", "video2.mp4", "video3.mp4"]

for video in videos:
    akuma.forge_video(video_path=video, output_path=f"subbed_{video}")
```

---

## System Requirements 💻

- **Python**: 3.10+
- **FFmpeg**: Required for video processing.
- **GPU Support**: Recommended for faster Whisper processing (CUDA-enabled).

> [!TIP]
> **GPU Acceleration**: If you have a compatible GPU, enable CUDA for significant speed improvements.

---

## Contributing 🤝

We welcome contributions! Here’s how you can help:

1. **Report Issues**: Found a bug? Open an issue [here](https://github.com/Akumanomi1988/AkumaSubtitler/issues).
2. **Submit Features**: Have an idea? Share it in the discussions.
3. **Code Contributions**: Fork the repo and submit a pull request.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Support 🆘

For help or questions, please:
- Open an issue on [GitHub](https://github.com/Akumanomi1988/AkumaSubtitler/issues).
- Join our [Discussions](https://github.com/Akumanomi1988/AkumaSubtitler/discussions).

---

## Links 🔗

- **GitHub Repository**: [AkumaSubtitler](https://github.com/Akumanomi1988/AkumaSubtitler)
- **PyPI Package**: [akumasubtitler](https://pypi.org/project/akumasubtitler/)

---
