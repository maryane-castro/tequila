from locust import HttpUser, task, between
from locust.contrib.fasthttp import FastHttpUser
import random

class TequilaApiUser(HttpUser):
    # Tempo entre as requisições, para simular um usuário real (de 1 a 3 segundos)
    wait_time = between(1, 3)
    
    # URL base para a API
    host = "https://tequila-hegvh9f0cshnb6dq.brazilsouth-01.azurewebsites.net"

    @task(1)
    def predict(self):
        # Caminho para a imagem que você deseja enviar na requisição
        image_path = "/caminho/para/sua/imagem.jpg"
        
        with open(image_path, 'rb') as f:
            files = {'image': (image_path, f, 'image/jpeg')}
            response = self.client.post("/predict", files=files)

        # Validação da resposta
        if response.status_code == 200:
            print("Predição realizada com sucesso.")
        else:
            print(f"Erro: {response.status_code}")
    
    @task(2)
    def health_check(self):
        # Endpoint de saúde para verificar se a API está funcionando
        response = self.client.get("/health")
        if response.status_code != 200:
            print(f"Erro no health check: {response.status_code}")

