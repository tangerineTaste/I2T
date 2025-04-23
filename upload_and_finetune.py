import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# 1. 학습 데이터 업로드
file_response = openai.files.create(
    file=open("training_data_sequence.jsonl", "rb"),
    purpose="fine-tune"
)
file_id = file_response.id
print("✅ 파일 업로드 완료:", file_id)

# 2. 파인튜닝 작업 생성
job_response = openai.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    suffix="chat-dailytone"
)
print("🚀 파인튜닝 시작됨, job id:", job_response.id)
