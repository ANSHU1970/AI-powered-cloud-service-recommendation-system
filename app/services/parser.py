import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT_TEMPLATE = """
You are a strict JSON generator.

Return ONLY JSON. No explanation.

Format:
{{
  "model_size": "...",
  "users": number,
  "latency": number,
  "budget": number,
  "gpu": true/false,
  "inference_type": "real-time" or "batch"
}}

Text:
{input}
"""

def parse_input(text: str):

    prompt = PROMPT_TEMPLATE.format(input=text)

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0
                }
            }
        )

        result = response.json()["response"]

        parsed = json.loads(result)
        return parsed

    except Exception as e:
        return fallback_parser(text)


def fallback_parser(text):
    return {
        "model_size": "unknown",
        "users": 100,
        "latency": 200,
        "budget": 100,
        "gpu": "gpu" in text.lower(),
        "inference_type": "real-time"
    }