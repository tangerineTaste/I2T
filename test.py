import openai
import os
from openai import OpenAI
openai.api_key = os.environ['OPENAI_API_KEY']
model_name = "ft:gpt-3.5-turbo-0125:personal:chat-dailytone:BPOc9Msn"  # 파인튜닝된 모델명

client = OpenAI()

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "너는 감정에 맞는 자연스러운 대사를 생성하는 AI야."},
        {"role": "user", "content": "[장르: 판타지]\n[설명: 마법사가 빛나는 마법진을 펼친다]\n[감정: 경고]\n→ 대사:"}
    ],
    temperature=0.8
)

print("🎙️ 생성된 대사:")
print(response.choices[0].message.content)
