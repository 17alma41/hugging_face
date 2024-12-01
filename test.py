# Posible solucion
def interpretation_feelings(output):
    # Verificamos si 'output' es una lista y contiene una lista interna
    if isinstance(output, list) and len(output) > 0 and isinstance(output[0], list) and len(output[0]) > 0:
        # Obtenemos las etiquetas y puntuaciones de la lista interna
        sentiment_scores = output[0]
        
        # Ordenamos las etiquetas por la puntuación más alta
        sorted_sentiments = sorted(sentiment_scores, key=lambda x: x['score'], reverse=True)
        
        # Tomamos la etiqueta con el puntaje más alto
        feeling = sorted_sentiments[0]['label']

        # Interpretamos la etiqueta
        if feeling == 'positive':  # Positivo
            return "El sentimiento es mayormente positivo"
        elif feeling == 'neutral':  # Neutral
            return "El sentimiento es neutral"
        elif feeling == 'negative':  # Negativo
            return "El sentimiento es mayormente negativo"
        else:
            return "Sentimiento desconocido"
    else:
        return "Respuesta inesperada del modelo"

# Ejemplo de uso
output = [[{'label': 'positive', 'score': 0.9299362301826477}, {'label': 'neutral', 'score': 0.06471797823905945}, {'label': 'negative', 'score': 0.005345815327018499}]]
print(interpretation_feelings(output))
