from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("groq_key"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "you are an general chatbot"},
        {"role": "user", "content": "hi,give me a steps for using api"}
    ]
)

print(response.choices[0].message.content)