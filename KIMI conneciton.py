from docx import Document
from openai import OpenAI
import os
client = OpenAI(
    api_key="sk-rpCB5h0GPxfDE8AOGCqWfu5meZX3rpKrC96w4hyew47icmq7",
    base_url="https://api.moonshot.cn/v1",
)
prompt_file = r'D:\Desktop\prompt.txt'
with open (prompt_file, 'r' ,encoding='utf-8') as f:
    prompt = f.read()
completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "system",
         "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
)
print(completion.choices[0].message.content)
doc = Document()
doc.add_paragraph(completion.choices[0].message.content)
file_name = 'test.docx'
file_path = os.path.join(os.getcwd(), file_name)
doc.save(file_path)