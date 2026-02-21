# 🎙️ Voice AI Dashboard (Offline)

A complete offline Voice AI system built using Python.

This repository contains three modules:

- 🗣 Speech → Text  
- 🔊 Text → Speech  
- 🎤 Speech → Speech  

---

## 📌 Project Overview

This project demonstrates how voice systems work without using any API.

All systems run locally and do not require internet.

---

# 1️⃣ Speech to Text (STT)

## ✅ What It Does

Converts spoken voice into text.

### Example:

You say:

```bash
What is Apple?
```

System displays:

```bash
Apple is a fruit...
```

## ⚙️ How It Works

- Microphone captures audio  
- Audio processed using Vosk  
- Speech converted into text  
- Text displayed on dashboard  

## 🛠 Tech Stack

- Python  
- Vosk (Offline Speech Recognition)  
- Gradio  

## 📂 Folder Structure

```
speech_to_text/
│── app.py
│── requirements.txt
│── vosk-model/
```

---

# 2️⃣ Text to Speech (TTS)

## ✅ What It Does

Converts written text into spoken voice.

### Example:

You type:

```bash
What is a computer?
```

System speaks the answer.

## ⚙️ How It Works

- User enters text  
- Text processed  
- Voice generated using pyttsx3  

## 🛠 Tech Stack

- Python  
- pyttsx3  
- Gradio  

## 📂 Folder Structure

```
text_to_speech/
│── app.py
│── tts_engine.py
│── requirements.txt
```

---

# 3️⃣ Speech to Speech (S2S)

## ✅ What It Does

You speak → System understands → AI generates answer → System responds in voice.

⚠ No text is visible on the screen.

---

## 🧠 Architecture Flow

```
Speech Input
      ↓
Speech Recognition (Vosk)
      ↓
AI Model Processing
      ↓
Text Response
      ↓
Text-to-Speech
      ↓
Voice Output
```

## 🛠 Tech Stack

- Python  
- Vosk  
- Local AI Model  
- pyttsx3  
- Gradio  

## 📂 Folder Structure

```
speech_to_speech/
│── app.py
│── model.py
│── tts_engine.py
│── vosk-model/
│── requirements.txt
```

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NLP.git
cd NLP
```

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Any Module

Example:

```bash
cd speech_to_text
python3 app.py
```

---

# 🔥 Features

- ✅ 100% Offline  
- ✅ No API Required  
- ✅ Real-Time Processing  
- ✅ Beginner Friendly  
- ✅ Modular Structure  

---

# 🧠 Simple Concept

Speech to Speech =

Hear → Understand → Think → Speak  

It combines:

- Speech to Text  
- AI Processing  
- Text to Speech  

---

# 💻 Requirements

- Python 3.8+  
- Microphone  
- Linux / Windows / Mac  

---

# 👩‍💻 Author

Priyanka Swamy
