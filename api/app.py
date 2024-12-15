import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tempfile import NamedTemporaryFile
from ultralytics import YOLO
from PIL import Image
import os

app = Flask(__name__)

# Habilitar CORS para o aplicativo inteiro
CORS(app)

# Carregar o modelo YOLO
try:
    model = YOLO("best.pt")  # Atualize com o caminho correto do seu modelo
except Exception as e:
    print(f"Erro ao carregar o modelo YOLO: {e}")
    model = None

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

    # Verifica se o arquivo é uma imagem válida
    if not file.content_type.startswith('image'):
        return jsonify({"error": "O arquivo enviado não é uma imagem válida"}), 400

    try:
        # Salvar a imagem com seu nome original
        original_filename = file.filename

        # Processa a imagem e realiza a predição
        image_path = process_image(file)

        if model is None:
            return jsonify({"error": "Modelo YOLO não carregado"}), 500

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

        # Responde com o nome real da imagem e os dados de predição
        response = {
            "image_name": original_filename,  # Usando o nome real da imagem
            "prediction": result_mapped,
            "confidence": confidence
        }

        return jsonify(response), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception as e:
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), 500

    finally:
        # Remove o arquivo temporário após o processamento
        if os.path.exists(image_path):
            os.remove(image_path)


if __name__ == "__main__":
    # Usar a porta da variável de ambiente ou 5000 como padrão
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host='0.0.0.0', port=port)
