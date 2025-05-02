import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve API keys and URL from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = os.getenv("GROQ_URL")

PROMPT_OPTIMIZER_PROMPT = """
You are a Prompt Optimizer Agent...
"""

def call_groq_api(system_content, user_content):
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        "model": "deepseek-r1-distill-llama-70b", 
        'messages': [
            {'role': 'system', 'content': system_content},
            {'role': 'user', 'content': user_content}
        ],
        'temperature': 0.3,
        'max_tokens': 9000
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    return f"Error: {response.status_code} - {response.text}"
