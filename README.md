# WhatsApp Sticker Generator

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-green.svg)
![Version](https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000)
![Stargazers](https://img.shields.io/github/stars/yusufadji/whatsapp-sticker-generator)
![Forks](https://img.shields.io/github/forks/yusufadji/whatsapp-sticker-generator)

## 🌟 Overview
This project automates the creation of **WhatsApp stickers** from video frames using Python. It converts frames into **WebP format** and optimizes them to meet WhatsApp's size requirements.

## ✨ Features
- **Convert image frames to WebP format** using [Google WebP](https://developers.google.com/speed/webp/download).
- **Generate animated WhatsApp stickers** automatically.
- **Adjust compression quality dynamically** to ensure stickers are under **500 KB**.
- **Easy cleanup** for new sticker creation.

## ⚙️ Requirements
- [Python 3.x](https://www.python.org/downloads/)
- [Google WebP library](https://developers.google.com/speed/webp/download)

## 📝 Installation
### 1. Install Python
Ensure you have Python 3.x installed. Download it from [Python's official website](https://www.python.org/downloads/).

### 2. Install WebP Library
#### 💻 Windows
1. Download **WebP precompiled binaries** from [Google WebP Download](https://developers.google.com/speed/webp/download).
2. Extract the files and add the path to your system environment variables.

#### 💻 Linux
For Debian-based (Ubuntu, Debian):
```sh
sudo apt update && sudo apt install webp
```
For Arch Linux:
```sh
sudo pacman -S libwebp
```

#### 💻 macOS
```sh
brew install webp
```

### 3. Clone the Repository
```sh
git clone https://github.com/yusufadji/whatsapp-sticker-generator.git
cd whatsapp-sticker-generator
```

## 🗂️ Project Structure
```
.
├── aniwebpmaker.py   # Creates animated WebP from converted frames
├── auto.py           # Automates compression and animation process
├── clean.py          # Cleans workspace directories
├── compressor.py     # Converts images to WebP format
├── init.py           # Initializes required directories
├── README.md         # Documentation
```
After running `init.py`, the structure includes:
```
.
├── dst   # Stores final WebP sticker files
├── orig  # Contains original input frames
├── src   # Stores converted WebP frames
```

## 📝 Usage
### 1. Initialize Directories
Run the following command to create necessary directories:
```sh
python init.py
```

### 2. Automate the Sticker Creation Process
Run the following command to automatically compress images and create stickers:
```sh
python auto.py
```
The script will adjust **compression quality** dynamically until the final WebP file meets WhatsApp's **size limit (500 KB)**.

### 3. Clean the Workspace
To reset and prepare for new sticker creation, run:
```sh
python clean.py
```

## 📑 Notes
- If `auto.py` fails to reach the size limit even at the lowest compression setting, **manually reduce the number of frames** in `orig/` and rerun the script.

## ⚖️ License
This project is licensed under the [MIT License](https://github.com/yusufadji/whatsapp-sticker-generator/blob/master/LICENSE).

## 👤 Author
Developed by [Yusuf Bhaskara Adji](https://github.com/yusufadji). Feel free to contribute or report issues!

