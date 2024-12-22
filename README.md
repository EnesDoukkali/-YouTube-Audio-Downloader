# 🎵 YouTube Audio Downloader

**A sleek and user-friendly desktop application for downloading high-quality MP3 audio from YouTube videos.**

## 📖 Description

The **YouTube Audio Downloader** is a Python-based desktop application with an intuitive **Graphical User Interface (GUI)** built using **Tkinter**. It leverages **yt-dlp** and **ffmpeg** to download and convert audio files from YouTube videos into **MP3 format** with customizable audio quality options.

## 🚀 Features

✅ **Intuitive GUI:** Clean and easy-to-navigate graphical interface  
✅ **Audio Quality Selection:** Choose between `320 kbps`, `192 kbps`, or `128 kbps`  
✅ **Dynamic UI:** Fully responsive layout for resizing and fullscreen modes  
✅ **Progress Tracking:** Real-time progress updates with a responsive progress bar  
✅ **Save Location:** Choose custom folders for storing downloads  
✅ **Error Handling:** Informative error messages for invalid URLs or dependencies  
✅ **Cross-Platform:** Designed for **Windows**, but adaptable to other systems  
✅ **Standalone Build:** Can be packaged into an `.exe` for distribution

## 🛠️ Technologies Used

- **Python 3.11+**
- **Tkinter** – GUI library
- **yt-dlp** – YouTube downloading library
- **ffmpeg** – Audio processing library

## 📥 Installation Guide

### ✅ 1. Prerequisites

Make sure you have the following installed:

- [**Python 3.11+**](https://www.python.org/downloads/)
- [**ffmpeg**](https://ffmpeg.org/download.html)
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp)

### ✅ 2. Install Dependencies

After cloning the repository, navigate to the project directory and install dependencies:

```bash
pip install yt-dlp
```

### ✅ 3. Install ffmpeg

**Windows:**
1. Download the ffmpeg executable from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Unzip it and add the bin folder to your System PATH

**Linux (Debian/Ubuntu):**
```bash
sudo apt install ffmpeg
```

**MacOS:**
```bash
brew install ffmpeg
```

Verify Installation:
```bash
ffmpeg -version
```

### ✅ 4. Run the Application

After installing dependencies, run the Python script:
```bash
python app.py
```

## 📂 Project Structure

```plaintext
/youtube-audio-downloader
│
├── app.py          # Main Python application
├── yt-dlp.exe      # yt-dlp executable (optional)
├── ffmpeg.exe      # ffmpeg executable (optional)
├── LICENSE         # License information
├── README.md       # Documentation
└── assets/         # Icons, logos, and other assets
```

## 📝 Usage Instructions

1. Enter a YouTube URL: Paste a valid YouTube video URL into the input field
2. Select Audio Quality: Choose between 320 kbps, 192 kbps, or 128 kbps
3. Choose Save Location: Select your desired folder for saving audio files
4. Start Download: Click on the "🎧 Start Download" button
5. Monitor Progress: Track the real-time progress via the progress bar
6. Complete: A success message confirms the audio download

## 📦 Packaging into an Executable

### For Windows Users

1. Install pyinstaller if not already installed:
```bash
pip install pyinstaller
```

2. Build the .exe file:
```bash
pyinstaller --onefile --noconsole app.py
```

Find your executable in the `/dist` directory.

### For Linux and macOS Users

You can also use pyinstaller to create a standalone binary:
```bash
pyinstaller --onefile --noconsole app.py
```

## 🐞 Troubleshooting

### Common Issues:

- **yt-dlp not found:**
  - Ensure yt-dlp is installed via `pip install yt-dlp` and added to your PATH

- **ffmpeg not found:**
  - Make sure ffmpeg is installed and accessible from the terminal

- **Progress Bar Not Updating:**
  - Restart the application and ensure dependencies are correctly configured

- **Invalid URL Error:**
  - Double-check the YouTube URL format

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch:
```bash
git checkout -b feature-branch
```
3. Make changes and commit:
```bash
git commit -am 'Add new feature'
```
4. Push to your branch:
```bash
git push origin feature-branch
```
5. Open a Pull Request on GitHub

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact

- Developer: [Enes Doukkali]
- Email: [enes_doukkali@hotmail.com]
- GitHub: [https://github.com/your-username](https://github.com/EnesDoukkali)

## ⭐ Support the Project

- Give it a ⭐ on GitHub!
- Share it with your friends and colleagues
- Contribute new features or bug fixes

🎧 Enjoy downloading your favorite YouTube audio tracks with ease! 🚀✨
