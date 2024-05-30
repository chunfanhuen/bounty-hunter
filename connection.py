from openai import OpenAI

client = OpenAI(
    base_url='https://api.openai-proxy.live/v1',
    api_key='sk-013X14IshjqO9tFZQkwIAia1eAflLfTMbImwZ8I5uczxJq4q@1005732',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say hi",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)