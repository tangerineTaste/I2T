# 1) openai 패키지 설치
# upload_and_finetune.py
import openai
from openai import OpenAI

# 1) API 키 설정
openai.api_key = "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"
client = OpenAI()

# 2) JSONL 파일 업로드
resp = openai.files.create(
    file=open("dialogue_finetune.jsonl", "rb"), 
    purpose="fine-tune"
)
file_id = resp.id #file-TPPeoP3KNBT6PBnWpAEebh
print("✅ 업로드 완료! file_id:", file_id)

# 3) Fine‑tune 작업 생성
ft_job = client.fine_tuning.jobs.create(
    
    training_file=file_id,
    model="gpt-3.5-turbo"
)
print("✅ 파인 튜닝 완료! id:", ft_job.id)

# 4) Status 조회 
status = client.fine_tuning.jobs.retrieve(ft_job.id)
print("상태      :", status.status) 
print("모델       :", status.fine_tuned_model)
print("Result files:", status.result_files)
