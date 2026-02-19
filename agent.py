import os
import subprocess
from openai import OpenAI

# Get recent commits
commits = subprocess.getoutput(
    'git log --since="24 hours ago" --oneline'
)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = f"""
Summarize today's repository activity.

Commits:
{commits}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}]
)

summary = response.choices[0].message.content

print("===== AI SUMMARY =====")
print(summary)

# Save to file
with open("report.txt", "w") as f:
    f.write(summary)
