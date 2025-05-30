import openai
import os
from openai import OpenAI
openai.api_key = os.environ['OPENAI_API_KEY']
model_name = "ft:gpt-3.5-turbo-0125:personal:chat-dailytone:BPOc9Msn"  # 파인튜닝된 모델명

client = OpenAI()

response = client.chat.completions.create(
    model=model_name,
    messages=[
    {"role": "system", "content": "너는 여러 장면의 흐름을 보고 어울리는 대사를 생성하는 AI야."},
    {"role": "user", "content": "[장면 1] 학생이 복도에서 달려온다.\n[장면 2] 교실 문을 벌컥 열고 들어온다.\n[장면 3] 친구들이 놀라서 쳐다본다.\n[감정 흐름] 초조 → 급박 → 민망\n→ 이 흐름에 어울리는 대사를 컷별로 만들어줘."}
    ],
    temperature=0.8
)

print("🎙️ 생성된 대사:")
print(response.choices[0].message.content)
