# NeuraBar AI

> A Spotlight-like command bar for Windows that lets you search, open apps, and extract text from anywhere on your screen using OCR — all with a single shortcut.

---

## ✨ Overview

NeuraBar AI is designed to reduce context switching by allowing users to perform common tasks directly from a lightweight command interface.

## 🔥 What Makes This Different

- Combines command launcher + OCR in one tool
- Works globally with keyboard shortcut
- Zero context switching
---

## 🚀 Features

### ⚡ Global Command Bar

* Trigger using: `Ctrl + \`
* Minimal, distraction-free UI
* Keyboard-first interaction

 On pressing "ctrl + \ " 
 
<img width="2081" height="1356" alt="image" src="https://github.com/user-attachments/assets/0f77c919-3c51-4e08-826a-e52cedc3b817" />


Running the `extract` command allows you to select any region on your screen. Once the text is extracted, you receive a notification and the content is automatically copied to your clipboard.

This is ideal for quickly capturing text without saving or sharing full screenshots.

<img width="2027" height="1231" alt="image" src="https://github.com/user-attachments/assets/d2d30666-c765-47ec-a4f5-d04675449ffb" />




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

