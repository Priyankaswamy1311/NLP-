import gradio as gr
from stt_engine import listen
from nlp_engine import generate_answer
from tts_engine import speak

def speech_to_speech():
    # Step 1: Listen
    question = listen()

    # Step 2: Generate answer
    answer = generate_answer(question)

    # Step 3: Speak answer
    speak(answer)

    return "Done"   # No text visible

iface = gr.Interface(
    fn=speech_to_speech,
    inputs=[],
    outputs="text",   # We will hide this visually
    title="Offline Speech-to-Speech AI",
    description="Click Run and speak. AI will answer in voice only."
)

iface.launch(inbrowser=True)
