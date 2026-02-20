import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import threading
import re
from datetime import datetime

# ----------------- Initialize TTS Engine -----------------
engine = pyttsx3.init()

# ----------------- NLP Command Parser -----------------
def parse_command(text):
    text = text.lower()

    number_match = re.search(r'\d+', text)
    distance = int(number_match.group()) if number_match else None

    if "forward" in text:
        return f"MOVE_FORWARD {distance if distance else ''}"
    elif "backward" in text:
        return f"MOVE_BACKWARD {distance if distance else ''}"
    elif "left" in text:
        return "TURN_LEFT"
    elif "right" in text:
        return "TURN_RIGHT"
    else:
        return "UNKNOWN_COMMAND"

# ----------------- Main Dashboard Class -----------------
class VoiceDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("NLP / STT / TTS Dashboard")
        self.root.geometry("750x520")
        self.root.configure(bg="#1e1e2f")

        # ---------------- Title ----------------
        title = tk.Label(
            root,
            text="NLP / STT / TTS Dashboard",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=15)

        # ---------------- Status Frame ----------------
        status_frame = tk.Frame(root, bg="#2c2c3e", padx=20, pady=10)
        status_frame.pack(fill="x", padx=20)

        self.status_label = tk.Label(
            status_frame,
            text="System State: IDLE",
            font=("Segoe UI", 12, "bold"),
            bg="#2c2c3e",
            fg="#00ffcc"
        )
        self.status_label.pack()

        # ---------------- Command Frame ----------------
        command_frame = tk.Frame(root, bg="#252537", padx=20, pady=15)
        command_frame.pack(fill="x", padx=20, pady=15)

        tk.Label(
            command_frame,
            text="Current Recognized Command",
            font=("Segoe UI", 13, "bold"),
            bg="#252537",
            fg="white"
        ).pack()

        self.command_display = tk.Label(
            command_frame,
            text="None",
            font=("Segoe UI", 14),
            fg="#4da6ff",
            bg="#252537"
        )
        self.command_display.pack(pady=8)

        # ---------------- Log Frame ----------------
        log_frame = tk.Frame(root, bg="#2c2c3e", padx=15, pady=10)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(
            log_frame,
            text="TTS Output Log",
            font=("Segoe UI", 13, "bold"),
            bg="#2c2c3e",
            fg="white"
        ).pack(anchor="w")

        self.tts_log = scrolledtext.ScrolledText(
            log_frame,
            height=10,
            bg="#1a1a26",
            fg="#00ff99",
            insertbackground="white",
            font=("Consolas", 10),
            relief="flat"
        )
        self.tts_log.pack(fill="both", expand=True, pady=5)

        # ---------------- Button ----------------
        self.listen_button = tk.Button(
            root,
            text="Start Listening",
            command=self.start_listening,
            font=("Segoe UI", 12, "bold"),
            bg="#4da6ff",
            fg="white",
            activebackground="#3399ff",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.listen_button.pack(pady=15)

    # ----------------- Start Listening Thread -----------------
    def start_listening(self):
        threading.Thread(target=self.listen_voice).start()

    # ----------------- Voice Listening Logic -----------------
    def listen_voice(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.update_status("LISTENING")
            audio = recognizer.listen(source)

            try:
                self.update_status("PROCESSING")
                text = recognizer.recognize_google(audio)

                # Parse NLP
                command = parse_command(text)

                # Update Dashboard
                self.command_display.config(text=command)

                # Speak Response
                response = f"Command received: {command}"
                self.speak(response)

            except:
                self.command_display.config(text="Could not understand")

            self.update_status("IDLE")

    # ----------------- TTS Function -----------------
    def speak(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"

        self.tts_log.insert(tk.END, log_entry)
        self.tts_log.see(tk.END)

        engine.say(message)
        engine.runAndWait()

    # ----------------- Update System Status -----------------
    def update_status(self, state):
        colors = {
            "IDLE": "#00ffcc",
            "LISTENING": "#ffcc00",
            "PROCESSING": "#ff6666"
        }
        color = colors.get(state, "white")
        self.status_label.config(text=f"System State: {state}", fg=color)

# ----------------- Run Application -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceDashboard(root)
    root.mainloop()
