import requests
import json

# Replace with your actual Groq API key
API_KEY = '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'

# Groq API endpoint for chat completions
url = 'https://api.groq.com/openai/v1/chat/completions'

# Headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Payload for the API request
data = {
    "model": "deepseek-r1-distill-llama-70b",  # or "deepseek-coder-33b" if using OpenRouter
    "messages": [
        {"role": "user", "content": "Give only the complete working Flask code with two routes: '/' returns 'Hello World' and '/about' returns 'About page'. Do not include explanations, just the Python code."}
    ],
    "temperature": 0.5,
    "max_tokens": 300
}


# Send the POST request to the Groq API
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    # Extract and print the assistant's reply
    assistant_reply = response_data['choices'][0]['message']['content']
    print("Assistant's Reply:", assistant_reply)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
