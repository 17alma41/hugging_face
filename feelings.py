# TODO Mostrar la respuesta en lenguaje natural, por ejemplo
# "El sentimiento es mayormente positivo" o "El sentimiento es mayormente negativo"
import dotenv
import os
import requests

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "I like you. I love you",
})

def interpretation_feelings(output):
    if isinstance(output, list) and len(output) > 0 and isinstance(output[0], list) and len(output[0]) > 0:
        feeling = output[0]['label']  # Tomar la etiqueta label

        if feeling == 'negative':  # Negativo
            return "El sentimiento es mayormente negativo"
        elif feeling == 'neutral':  # Neutral
            return "El sentimiento es neutral"
        elif feeling == 'positive':  # Positivo
            return "El sentimiento es mayormente positivo"
        else:
            return "No tiene sentimientos"
    else:
        return "Respuesta inesperada del modelo"
    
print(interpretation_feelings(output))

