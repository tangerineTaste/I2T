import openai
from openai import OpenAI

openai.api_key = "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"
client = OpenAI()

# 조회할 파인튜닝 잡 ID
ft_id = "ftjob-yWp0K1d9hxs4DpUbkUvoIjnb"

status = client.fine_tuning.jobs.retrieve("ftjob-lxFxvv6CLx3btwfcVKWGTwRg")
print("Status      :", status.status)
print("Model       :", status.fine_tuned_model)
print("Result files:", status.result_files)
