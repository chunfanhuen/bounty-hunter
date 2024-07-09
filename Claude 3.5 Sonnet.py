# import openai
#
# client = openai.OpenAI(
#     base_url='https://api.openai-proxy.org/anthropic/v1/messages',
#     api_key='sk-QNLQxq0rkkZcba18VLM80z1eguzLr3kbGua0WWsqpHjGl13E',
# )
#
# response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "hi",
#             "max_tokens": "3000",
#         }
#     ],
#     model="claude-3-sonnet-20240229",
# )
#
# print(response)
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
