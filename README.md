# 🎙️ Voice AI Dashboard (Offline)

A complete offline Voice AI system built using Python.

---

## 📌 Project Overview

This repository contains three modules:

- 🗣 Speech → Text  
- 🔊 Text → Speech  
- 🎤 Speech → Speech  

All systems run completely offline without any API.

---

# 1️⃣ Speech to Text (STT)

## 🔹 What It Does

Converts spoken voice into text.

**Example:**

You say:

```bash
What is Apple?
```

System displays:

```bash
Apple is a fruit.
```

## ⚙️ How It Works

1. Microphone captures audio  
2. Vosk processes speech  
3. Speech converts into text  
4. Text appears on screen  

---

# 2️⃣ Text to Speech (TTS)

## 🔹 What It Does

Converts text into spoken voice.

**Example:**

You type:

```bash
What is a computer?
```

System speaks the answer.

## ⚙️ How It Works

1. User enters text  
2. pyttsx3 generates voice  
3. Speaker outputs sound  

---

# 3️⃣ Speech to Speech (S2S)

## 🔹 What It Does

You speak → System understands → System replies in voice.

⚠ No text visible.

---

## 🧠 Architecture Flow

```
Speech Input
     ↓
Speech Recognition
     ↓
AI Processing
     ↓
Text-to-Speech
     ↓
Voice Output
```

---

# 📂 Folder Structure

```
NLP/
│── speech_to_text/
│── text_to_speech/
│── speech_to_speech/
│── README.md
```

---

# 🚀 How To Run

```bash
git clone https://github.com/YOUR_USERNAME/NLP.git
cd NLP
pip install -r requirements.txt
python3 app.py
```

---

# 💻 Requirements

- Python 3.8+
- Microphone
- Speaker
- Linux / Windows / Mac

---

# 👩‍💻 Author

Priyanka Swamy
