import pandas as pd
import json

# CSV 불러오기
df = pd.read_csv("dialogue_dataset.csv")

# OpenAI용 JSONL로 변환
with open("dialogue_finetune.jsonl", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        prompt = f"[장르: {row['genre']}]\n[설명: {row['description']}]\n[감정: {row['emotion']}]\n→ 대사:"
        completion = " " + row['dialogue_text'].strip() + "\n"
        json.dump({"prompt": prompt, "completion": completion}, f, ensure_ascii=False)
        f.write("\n")
