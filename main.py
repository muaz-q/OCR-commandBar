import os
import google.generativeai as genai
import json
from datetime import datetime
import webbrowser
import tkinter as tk
import keyboard
import pyautogui
import pytesseract
import pyperclip
from plyer import notification
from dotenv import load_dotenv
import pyttsx3 
import threading
import re 

#handling the api key

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key :
    raise ValueError("api key was not found")
genai.configure(api_key=api_key)

app_root = tk.Tk()
app_root.withdraw() 

# Tesseract path
try:
    pytesseract.get_tesseract_version()
except Exception:
    print("⚠️ Tesseract not found. Check PATH or installation.")

#command bar

def save_to_history(command):
    if os.path.exists("history.txt"):
        with open("history.txt", "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f.readlines()]

        if command in lines:
            return

    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(command + "\n")


def load_history():
    if not os.path.exists("history.txt"):
        return []

    with open("history.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    return [line.strip() for line in lines if line.strip()][-2:][::-1]

def show_command_bar():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="#0f172a")
    root.attributes("-alpha", 0.97)

    width = 700
    height = 250
    screen_width = root.winfo_screenwidth()
    x = (screen_width // 2) - (width // 2)
    y = 120

    root.geometry(f"{width}x{height}+{x}+{y}")

    # Main container
    main_frame = tk.Frame(root, bg="#1e293b")
    main_frame.pack(fill="both", expand=True, padx=15, pady=15)

    # Entry box
    entry = tk.Entry(
        main_frame,
        font=("Segoe UI", 16),
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        bd=0
    )
    entry.pack(fill="x", padx=15, pady=10)

    # Placeholder
    entry.insert(0, "Type a command...")
    entry.config(fg="#94a3b8")

    def on_focus_in(e):
        if entry.get() == "Type a command...":
            entry.delete(0, tk.END)
            entry.config(fg="white")

    entry.bind("<FocusIn>", on_focus_in)

    # Suggestion panel
    suggestion_frame = tk.Frame(main_frame, bg="#1e293b")
    suggestion_frame.pack(fill="both", expand=True, padx=10, pady=5)

    history = load_history()

    # Title
    tk.Label(
        suggestion_frame,
        text="Recent",
        fg="#94a3b8",
        bg="#1e293b",
        font=("Segoe UI", 10)
    ).pack(anchor="w", padx=10)

    if not history:
        tk.Label(
            suggestion_frame,
            text="No recent commands",
            fg="#64748b",
            bg="#1e293b",
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=10)

    for text in history:
        item = tk.Label(
            suggestion_frame,
            text=text,
            fg="white",
            bg="#1e293b",
            font=("Segoe UI", 12),
            anchor="w",
            padx=10,
            pady=5
        )
        item.pack(fill="x", pady=2)

        item.bind("<Enter>", lambda e: e.widget.config(bg="#334155"))
        item.bind("<Leave>", lambda e: e.widget.config(bg="#1e293b"))

        def on_click(e, cmd=text):
            entry.delete(0, tk.END)
            entry.insert(0, cmd)

        item.bind("<Button-1>", on_click)

    root.after(10, lambda: entry.focus())

    root.bind_all("<Escape>", lambda e: root.destroy())

    def handle_enter(event):
        command = entry.get().lower().strip()

        if command in ["bye", "exit", "quit"]:
            root.destroy()
            return

        if command and command != "type a command...":
            save_to_history(command)

        # 🔥 FIXED BLOCK
        if "extract" in command:
            root.destroy()

            if "summarise" in command:
                extract_text_from_region(mode="summarise")
            else:
                extract_text_from_region(mode="normal")

            return  # 🔥 IMPORTANT FIX

        handle_command(command)
        root.destroy()

    entry.bind("<Return>", handle_enter)

    root.mainloop()

# commands

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print("⚠️ Error loading config.json:", e)
        return {"sites": {}}

shortcuts = {
    "yt": "youtube",
    "wifi": "pesu",
    "gh": "github",
    "chrome": "google",
}

config = load_config()
sites = config.get("sites", {})

def handle_command(command):
    command = command.lower().strip()

    if command in shortcuts:
        command = shortcuts[command]

    if command.startswith("open"):
        site = command.replace("open", "").strip()

        if site in sites:
            webbrowser.open(sites[site])
        else:
            print("Site not found")

    elif command.startswith("search"):
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")

    else:
        for site in sites:
            if command == site or site in command:
                webbrowser.open(sites[site])
                return

        if command.endswith((".com", ".net", ".org", ".io")):
            webbrowser.open(f"https://{command}")
            return

        webbrowser.open(f"https://www.google.com/search?q={command}")

# snipping tool

def select_region():
    region = {}

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    root.config(bg="black")

    canvas = tk.Canvas(root, cursor="cross", bg="black")
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.create_text(
        root.winfo_screenwidth() // 2,
        50,
        text="Drag to select area for text extraction",
        fill="white",
        font=("Segoe UI", 16)
    )

    start_x = start_y = 0
    rect = None

    def on_mouse_down(event):
        nonlocal start_x, start_y, rect
        start_x, start_y = event.x, event.y
        rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="green", width=4.5)

    def on_mouse_move(event):
        if rect:
            canvas.coords(rect, start_x, start_y, event.x, event.y)

    def on_mouse_up(event):
        region["x1"], region["y1"] = start_x, start_y
        region["x2"], region["y2"] = event.x, event.y
        root.quit()

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_move)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    root.mainloop()
    root.destroy()

    return region

# file system

# this is use to name the screenshots based of their intent
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text[:20]  

def save_screenshot(image , tag="capture" , context =""):
    base_folder = "screenshots"

    now = datetime.now()
    year = str(now.year)
    month = now.strftime("%B")

    folder_path = os.path.join(base_folder, year, month)
    os.makedirs(folder_path, exist_ok=True)

    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    context_clean = clean_text(context) if context else ""

    if context_clean :
        filename = f"{tag}_{context_clean}_{timestamp}.png"
    else :
        filename = f"{tag}_{timestamp}.png"
    
    file_path = os.path.join(folder_path, filename)

    image.save(file_path)
    print(f"Saved at: {file_path}")

# OCR + AI

def extract_text_from_region(mode= "normal"):
    region = select_region()

    if not region or "x1" not in region:
        print("No region selected")
        return

    x1, y1 = region["x1"], region["y1"]
    x2, y2 = region["x2"], region["y2"]

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    if width == 0 or height == 0:
        print("Invalid region")
        return

    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    save_screenshot(screenshot)

    screenshot = screenshot.convert("L")

    text = pytesseract.image_to_string(screenshot)

    if not text.strip():
        print("No text detected")
        return

    if mode == "summarise":
        summary = summarize_text(text)
        show_summary_popup(summary)
        return

    pyperclip.copy(text)
    show_toast("Text copied!")

    print("\nExtracted Text:\n")
    print(text)

def show_toast(message="Copied to clipboard"):
    notification.notify(
        title="CommandBar",
        message=message,
        timeout=2
    )


# reading the text section
engine =  pyttsx3.init()

def speak_text(text):
    try : 
        engine.stop()
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        engine.say(text)
        engine.runAndWait()
    except Exception as e : 
        print("TTS Error:",e)

# prevent ui from freezing
def speak_async(text):
    threading.Thread(target=speak_text, args=(text,), daemon=True).start()

def summarize_text(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        text = text[:3000]

        prompt = f"""
        Summarize the following text into 3-4 clear bullet points:

        {text}
        """

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Error generating summary: {str(e)}"

def show_summary_popup(summary):
    win = tk.Tk()
    win.title("AI Summary")
    win.geometry("1500x1300")
    win.configure(bg="#0f172a")

    title = tk.Label(
        win,
        text="AI Summary",
        font=("Segoe UI", 14, "bold"),
        bg="#0f172a",
        fg="white"
    )
    title.pack(pady=(10, 5))

    text_box = tk.Text(
        win,
        wrap="word",
        font=("Segoe UI", 12),
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        bd=0
    )
    text_box.insert("1.0", summary)
    text_box.config(state="disabled")
    text_box.pack(expand=True, fill="both", padx=15, pady=10)

    def copy_summary():
        pyperclip.copy(summary)
        show_toast("Summary copied!")

    copy_btn = tk.Button(
        win,
        text="Copy",
        command=copy_summary,
        bg="#334155",
        fg="white",
        bd=0,
        padx=10,
        pady=5
    )

    def speak_summary():
        speak_async(summary)

    speak_btn = tk.Button(
        win,
        text="🔊 Read Aloud",
        command=speak_summary,
        bg="#334155",
        fg="white",
        bd=0,
        padx=10,
        pady=5
    )

    def stop_speaking():
        engine.stop()

    stop_btn = tk.Button(
        win,
        text="⏹ Stop",
        command=stop_speaking,
        bg="#334155",
        fg="white",
        bd=0,
        padx=10,
        pady=5
    )

    btn_frame = tk.Frame(win, bg="#0f172a")
    btn_frame.pack(pady=10)

    copy_btn.pack(in_=btn_frame, side="left", padx=5)
    speak_btn.pack(in_=btn_frame, side="left", padx=5)
    stop_btn.pack(in_=btn_frame, side="left", padx=5)

    win.bind("<Escape>", lambda e: win.destroy())
    win.mainloop()

# main

is_open = False

def exit_program():
    print("Program terminated (Ctrl + Q pressed)")
    keyboard.unhook_all()
    os._exit(0)

def launch_bar():
    global is_open
    if is_open:
        return

    is_open = True
    show_command_bar()
    is_open = False

keyboard.add_hotkey("ctrl+\\", launch_bar)
keyboard.add_hotkey("ctrl+q", exit_program)

print("Running... Press Ctrl + \\ to open | Ctrl + Q to exit")
keyboard.wait()