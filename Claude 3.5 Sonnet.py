import requests

url = 'https://api.openai-proxy.org/anthropic/v1/messages'
headers = {
    'x-api-key': 'sk-QNLQxq0rkkZcba18VLM80z1eguzLr3kbGua0WWsqpHjGl13E',
    'anthropic-version': '2023-06-01',
    'content-type': 'application/json'
}
data = {
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1024,
    "stream": False,
    "messages": [
        {"role": "user", "content": "who are you?"},
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())
