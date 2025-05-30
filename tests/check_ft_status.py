import openai
import os
openai.api_key = os.environ['OPENAI_API_KEY']

job_id = "ftjob-F6PiEmbaHK9A7c5fwFpTaqHp"  # 위에서 출력된 job ID 복사
result = openai.fine_tuning.jobs.retrieve(job_id)
print("📌 현재 상태:", result.status)
print("📦 파인튜닝된 모델명:", result.fine_tuned_model)
