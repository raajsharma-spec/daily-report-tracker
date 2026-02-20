from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],   # changed name
    base_url="https://api.groq.com/openai/v1"   # important
)

response = client.chat.completions.create(
    model="llama3-8b-8192",   # free Groq model
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)