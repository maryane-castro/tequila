from tempfile import NamedTemporaryFile
from ultralytics import YOLO
from PIL import Image
import os

model = YOLO("model/best.pt")

def predict_image(image):
    try:
        img = Image.open(image)
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        with NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            img.save(tmp_file.name)
            results = model.predict(tmp_file.name)

        result = results[0]
        class_names = result.names
        probs = result.probs.data.cpu().numpy()
        predicted_class_idx = probs.argmax()
        predicted_class = class_names[predicted_class_idx]
        confidence = float(probs[predicted_class_idx])

        class_mapping = {"open": "aberta", "close": "fechada"}
        result_mapped = class_mapping.get(predicted_class, "desconhecida")

        image_name = os.path.basename(tmp_file.name)
        return image_name, result_mapped, confidence

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return None, "erro", 0.0
