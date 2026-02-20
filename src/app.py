import gradio as gr
from stt_engine import listen_and_transcribe
from nlp_engine import generate_response

def speech_to_ai():
    # Step 1: Speech to text
    question = listen_and_transcribe()

    # Step 2: AI answer
    answer = generate_response(question)

    return f"Question: {question}\n\nAnswer: {answer}"

iface = gr.Interface(
    fn=speech_to_ai,
    inputs=[],
    outputs="text",
    title="Offline Speech-to-Text AI",
    description="Click Run, speak your question, and get text response."
)

iface.launch(inbrowser=True)
