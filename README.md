# 📖 PDF Speech Reader

A simple Python script that extracts text from a PDF file and reads it aloud using text-to-speech.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

> ⚠️ **DISCLAIMER: This is a small personal project and is still a work in progress. There are known bugs and limitations. Use at your own discretion.**

---

## 🚀 Features

- Extracts text from PDF files
- Converts text to speech using pyttsx3
- Handles multi-page PDFs
- Displays page-by-page text preview in console
- Skips empty or unreadable pages

---

## 🐛 Known Issues & Limitations

- **Text Extraction Limitations**: PyPDF2 may not extract text from scanned PDFs or images (OCR not supported)
- **Speech Engine Bugs**: pyttsx3 can sometimes fail to initialize or crash on certain systems
- **Long PDFs**: Processing very large files may cause performance issues or memory errors
- **Formatting Loss**: Text formatting (bold, italics, tables, etc.) is lost during extraction
- **Special Characters**: Some Unicode characters may not be spoken correctly
- **Voice Selection**: Voice quality varies across different operating systems
- **No Pause/Resume**: Currently lacks controls for pausing or resuming speech
- **No GUI**: Command-line only interface

---

## 📋 Requirements

```bash
pip install pyttsx3 PyPDF2
```

---

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/PDF-Speech-Reader.git
cd PDF-Speech-Reader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

1. Update the file path in the script:
```python
book = open('Your PDF File Path', 'rb')
```

2. Run the script:
```bash
python pdf_speech_reader.py
```

---

## 🔧 How It Works

1. Opens the PDF file in binary mode
2. Extracts text from each page using PyPDF2
3. Collects all text into a single string
4. Initializes the pyttsx3 speech engine
5. Speaks the combined text using `engine.say()` and `engine.runAndWait()`

---

## 🧪 Testing

The script has been tested with:
- Small PDFs (under 10 pages)
- English language text
- Windows 10/11 and Linux (Ubuntu)
- PyPDF2 version 3.0.0+

---

## 🚧 Future Improvements

- [ ] Add OCR support for scanned PDFs (using Tesseract)
- [ ] Implement GUI interface (Tkinter or PyQt)
- [ ] Add pause, resume, and stop controls
- [ ] Support for multiple voice options
- [ ] Save speech as audio file (MP3/WAV)
- [ ] Adjustable speech rate and volume
- [ ] Bookmark/resume functionality
- [ ] Support for multiple languages
- [ ] Batch processing for multiple PDFs
- [ ] PDF metadata extraction (title, author, etc.)

---

## 📝 Notes for Contributors

This is a learning project and contributions are welcome! However, please note:
- The code is intentionally simple for educational purposes
- Major refactoring might be needed for production use
- Test your changes on different operating systems 

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙏 Acknowledgments

- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF parsing
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech functionality

---

## 👤 Author

**Erfan Shahbazzadeh**
- GitHub: [@ErfanShahbazzadeh](https://github.com/ErfanShahbazzadeh)
