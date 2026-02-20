import requests
from config import OLLAMA_URL, MODEL_NAME, MAX_TOKENS

def generate_response(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": MAX_TOKENS
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return "Model error."
    except:
        return "Connection error."
