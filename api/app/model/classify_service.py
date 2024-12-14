import random
import os

def predict_image(image):
    # DESENVOLVER AQUI COM MODELO
    # NOME FIXO - RESPOSTA ALEATÓRIA PARA TESTAR 
    image_name = "imagem_recebida-nomepadrao.png"

    result = random.choice(['aberta', 'fechada'])
    confidence = random.uniform(0.7, 1.0)  
    
    return image_name, result, confidence


