import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_explanation(service, parsed):

    prompt = f"""
Explain in 2-3 lines why {service} is suitable.

User requirements:
{parsed}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7
                }
            }
        )

        return response.json()["response"]

    except:
        return "Explanation unavailable"