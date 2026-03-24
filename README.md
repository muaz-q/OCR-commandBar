# CommandBar AI

A keyboard-driven desktop assistant that enables fast command execution, browser automation, and on-screen text extraction using OCR — all without leaving your workflow.

---

## ✨ Overview

CommandBar AI is designed to reduce context switching by allowing users to perform common tasks directly from a lightweight command interface.

With a single hotkey, users can:

* Open websites
* Perform searches
* Extract text from screen regions
* Manage recent commands

---

## 🚀 Features

### ⚡ Global Command Bar

* Trigger using: `Ctrl + \`
* Minimal, distraction-free UI
* Keyboard-first interaction

---

### 🌐 Smart Browser Automation

* Open websites using simple commands:

  ```
  yt → YouTube
  gh → GitHub
  open linkedin
  ```
* Intelligent fallback:

  ```
  machine learning roadmap → Google search
  ```

---

### 📸 Screenshot + OCR (Text Extraction)

* Select any region on screen
* Extract text using Tesseract OCR
* Automatically copied to clipboard
* Instant system notification on success

---

### 🗂 Automatic Screenshot Storage

Screenshots are saved with timestamp-based naming in a structured format:

```
screenshots/
    2026/
        March/
            screenshot_YYYY-MM-DD_HH-MM-SS.png
```

---

### 🧠 Command History

* Displays last 2 recent commands
* Click to autofill
* Lightweight and non-intrusive

---

### 🔔 System Notifications

* Native OS notifications using `plyer`
* Confirms successful operations (e.g., OCR copy)

---

### ⚙️ Config-Based Architecture

* Websites stored in `config.json`
* Easy to modify and extend without changing code

---

## 🛠 Tech Stack

* **Python**
* **Tkinter** — UI
* **PyAutoGUI** — screen capture
* **Pytesseract** — OCR
* **Keyboard** — global hotkeys
* **Plyer** — system notifications

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/commandbar-ai.git
cd commandbar-ai
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install Tesseract OCR

Download from:
https://github.com/tesseract-ocr/tesseract

---

### 4. Add Tesseract to PATH

Add the following directory to your system environment variables:

```
C:\Program Files\Tesseract-OCR\
```

Verify installation:

```bash
tesseract --version
```

---

### 5. Run the application

```bash
python main.py
```

---

## 🎯 Usage

### Hotkeys

```
Ctrl + \  → Open Command Bar  
Ctrl + Q  → Exit Program
```

---

### Example Commands

```
yt
open github
search python decorators
extract
```

---

## 📂 Project Structure

```
commandbar-ai/
│
├── main.py
├── config.json
├── history.txt
├── screenshots/
│
└── README.md
```

---

## 💡 Design Highlights

* Separation of concerns using external config
* Keyboard-first UX for speed and efficiency
* Lightweight architecture with minimal dependencies
* Robust handling of OCR and file storage

---

## 🔮 Future Improvements

* AI-based command understanding (Ollama integration)
* OCR summarization
* Visual search from screenshots
* Dynamic suggestions and autocomplete
* Plugin-based extensibility

---

## 📌 Author

**Muaz**

---

## 📣 Notes

This project was built with a focus on:

* usability
* performance
* real-world applicability

Feedback and suggestions are welcome.
