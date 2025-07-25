import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env file
load_dotenv()

# Create Groq client using your API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Performing a Chat Completion:
res = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Where is Mangaluru in India?",
        }
    ],
    model="llama-3.3-70b-versatile"
)

# print(res)
print(res.choices[0].message.content)