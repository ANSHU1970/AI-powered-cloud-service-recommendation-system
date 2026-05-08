import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def parse_input(text):

    prompt = f"""
You are an AI infrastructure parser.

Extract structured requirements from the text.

Return ONLY valid JSON.

Format:
{{
    "model_size": "string",
    "users": number,
    "latency": number,
    "budget": number,
    "gpu": true,
    "inference_type": "real-time"
}}

Text:
{text}
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0,
                    "num_predict": 150
                }
            }
        )

        result = response.json()["response"]

        parsed = json.loads(result)

        return parsed

    except Exception as e:

        print("Parser Error:", e)

        return {
            "model_size": "unknown",
            "users": 100,
            "latency": 100,
            "budget": 100,
            "gpu": False,
            "inference_type": "real-time"
        }