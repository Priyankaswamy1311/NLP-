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
            result = response.json()
            return result.get("response", "No response from model.")
        else:
            return "Error: Model not responding."

    except Exception as e:
        return f"Connection error: {str(e)}"
