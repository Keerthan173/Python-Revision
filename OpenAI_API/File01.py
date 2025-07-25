import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables where API key is stored

client = OpenAI()  # Creates a connection to OpenAI's GPT service using your API key.


# List available models
# models = client.models.list()
# for model in models.data:
#     print(model.id)


# Generate text from a model
res = client.chat.completions.create(      # asking the OpenAI chat completion endpoint to generate a reply
    model="gpt-3.5-turbo",          # choosing which model to use
    messages=[
        {
            "role": "user",         # sending the message as the user
            "content": "Where is Mangaluru in India?"
        }
    ]
)

# print(res)
print(res.choices[0].message.content)
