# Miragic SDK

A powerful Python SDK for advanced image processing and manipulation. Transform your images with professional-grade AI-powered tools including background removal, image upscaling, and background blur effects.

## 🚀 Features

### 🎭 Background Removal
Remove backgrounds from images with precision using state-of-the-art AI technology. Perfect for product photos, portraits, and any image that needs a clean, transparent background.

### 📈 Image Upscaler
Enhance image quality and resolution with our advanced upscaling algorithms. Transform low-resolution images into crisp, high-quality visuals without losing detail.

### 🌫️ Blur Background
Create professional-looking images with beautiful background blur effects. Ideal for portrait photography, product shots, and artistic compositions.

## 📦 Installation

Install the Miragic SDK using pip:

```bash
pip install miragic-sdk
```

## 🛠️ Quick Start

```python
from miragic_sdk import MiragicSDK

# Initialize the SDK
sdk = MiragicSDK()

# Remove background from an image and return PIL Image
pil_img = sdk.remove_background("input.jpg")
pil_img.save("output.png")

# Upscale an image and return PIL Image
pil_img = sdk.upscale_image("low_res.jpg", scale_factor=2)
pil_img.save("upscaled.png")

# Apply background blur and return PIL Image
pil_img = sdk.blur_background("portrait.jpg", blur_strength=0.8)
pil_img.save("blurred.png")
```

## 📋 Requirements

- Python 3.7+
- Compatible with Windows, macOS, and Linux

## 🆓 Free Tool

Miragic SDK offers free access to powerful image processing capabilities. Get started with professional-grade image manipulation tools at no cost.

## 📚 Documentation

For detailed API documentation and examples, visit our [documentation site](https://docs.miragic.com).

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Website](https://miragic.ai)
- [Documentation](https://miragic.ai/resources/open-api)
- [GitHub Repository](https://github.com/Miragic-AI/miragic-sdk)
- [PyPI Package](https://pypi.org/project/miragic-sdk)

---

**Transform your images with Miragic SDK - The free, powerful image processing toolkit for Python developers.** 
