import pyttsx3

engine = pyttsx3.init()

# Optimize for low RAM
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
