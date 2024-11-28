import dotenv
import os
from huggingface_hub import InferenceClient

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

prompt = input("¿Qué quieres preguntar? ")

client = InferenceClient(api_key=TOKEN)

messages = [
	{
		"role": "user",
		"content": prompt
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)