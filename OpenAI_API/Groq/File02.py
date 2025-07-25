import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Create a message history (like a conversation)
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    reply = response.choices[0].message.content
    print(f"AI: {reply}")

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )


# messages = [
#     {"role": "system", "content": "You are a helpful assistant."}
# ]
# 🔹 This tells the model how to behave.

# When You Enter a Prompt:
# user_input = input("You: ")  # e.g., "What's the capital of Karnataka?"
# messages.append({"role": "user", "content": user_input})
# Now the messages list becomes:
# [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "What's the capital of Karnataka?"}
# ]

# 🤖 After Getting AI's Reply:
# reply = "The capital of Karnataka is Bengaluru."
# messages.append({"role": "assistant", "content": reply})
# Now your list looks like:
# [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "What's the capital of Karnataka?"},
#     {"role": "assistant", "content": "The capital of Karnataka is Bengaluru."}
# ]

# Why Is This Important?
# Each time you send this messages list to the model:
# ✅ It reads the whole conversation
# ✅ So it can respond with memory (like a real chat)

# If you don't append messages, the model will forget past questions.
