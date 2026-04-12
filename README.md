
# NeuraBarAI

A keyboard-driven desktop assistant that enables fast command execution, browser automation, and on-screen text extraction using OCR — all without leaving your workflow.
NeuraBar transforms passive screen content into actionable intelligence by combining OCR, automation, and AI-driven summarization into a unified command interface

---

## ✨ Overview

NeuraBar is designed to reduce context switching by allowing users to perform common tasks directly from a lightweight command interface.

With a single hotkey, users can:

```
Open websites
Perform searches
Extract text from screen regions
Summarize content using AI
Listen to results via text-to-speech

```
---

## 🚀 Features
What Makes This Different ?

Combines command launcher + OCR + AI in one tool
Works globally with a keyboard shortcut
Zero context switching
Transforms screen content → actionable intelligence

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

🧠 AI-Powered Enhancements

Text Summarization
Extracted text can be summarized into clear bullet points using AI
Reduces reading time and improves productivity

🔊 Text-to-Speech (TTS)

Summarized content can be read aloud instantly
Implemented using asynchronous threading
Prevents UI freezing
Enables hands-free interaction

### 📸 Screenshot + OCR (Text Extraction)

* Select any region on screen
* Extract text using Tesseract OCR
* Automatically copied to clipboard
* Instant system notification on success

---

### 🗂 Automatic Screenshot Storage

Screenshots are saved with timestamp-based naming in a structured format:

<img width="1391" height="718" alt="image" src="https://github.com/user-attachments/assets/6108db3b-0c00-49c7-a9d4-44007af1c42e" />


---

### 🧠 Command History

* Displays last 2 recent commands
* Click to autofill
* Lightweight and non-intrusive

<img width="982" height="415" alt="image" src="https://github.com/user-attachments/assets/a65cb975-73be-4ace-b93d-ea1eec94aa11" />


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

Upon executing the "Extract Command" :

<img width="1614" height="864" alt="image" src="https://github.com/user-attachments/assets/4e1710fb-76b6-41b8-8dc6-14e9d8b40ade" />


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
