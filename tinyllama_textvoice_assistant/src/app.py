import gradio as gr
from nlp_engine import generate_response
from tts_engine import speak_text

def ask_ai(question):
    if not question.strip():
        return "Please enter a question."

    answer = generate_response(question)

    # Speak answer
    speak_text(answer)

    return answer

iface = gr.Interface(
    fn=ask_ai,
    inputs=gr.Textbox(label="Ask Anything"),
    outputs=gr.Textbox(label="AI Response"),
    title="TinyLLaMA Offline Voice Assistant",
    description="Type any question. TinyLLaMA will answer and speak it."
)

iface.launch(inbrowser=True)
