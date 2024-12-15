from flask import Flask, request, jsonify, render_template
from tempfile import NamedTemporaryFile
from ultralytics import YOLO
from PIL import Image
import os

app = Flask(__name__)

# Carregar o modelo YOLO
model = YOLO("best.pt")  # Atualize com o caminho correto do seu modelo

def process_image(file):
    """
    Processa a imagem enviada, converte se necessário e salva em um arquivo temporário.
    """
    try:
        img = Image.open(file)
        if img.mode == 'RGBA':  # Converte RGBA para RGB, se necessário
            img = img.convert('RGB')

        with NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            img.save(tmp_file.name)
            return tmp_file.name  # Retorna o caminho do arquivo temporário

    except Exception as e:
        raise ValueError(f"Erro ao processar a imagem: {e}")

@app.route('/')
def index():
    """
    Exibe a página inicial com o formulário de upload de imagem.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para receber e processar uma imagem, retornando a predição.
    """
    if 'image' not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    file = request.files['image']

    try:
        # Processa a imagem e realiza a predição
        image_path = process_image(file)
        results = model.predict(image_path)

        # Processa o resultado
        result = results[0]
        class_names = result.names
        probs = result.probs.data.cpu().numpy()
        predicted_class_idx = probs.argmax()
        predicted_class = class_names[predicted_class_idx]
        confidence = float(probs[predicted_class_idx])

        # Mapeia as classes para nomes amigáveis
        class_mapping = {"open": "aberta", "close": "fechada"}
        result_mapped = class_mapping.get(predicted_class, "desconhecida")

        response = {
            "image_name": os.path.basename(image_path),
            "prediction": result_mapped,
            "confidence": confidence
        }

        # Remove o arquivo temporário após o processamento
        os.remove(image_path)

        return jsonify(response), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception as e:
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
