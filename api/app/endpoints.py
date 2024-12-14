from flask import request, jsonify, render_template
from model.classify_service import predict_image
from utils.image_validator import validate_image
from utils.logging_helper import get_logger
from run import app

# Initialize the logger
logger = get_logger()

@app.before_request
def log_request_info():
    """
    Basic log of information about the received request.
    """
    logger.info(f"Incoming request: {request.method} {request.url}")
    logger.debug(f"Headers: {request.headers}")
    if request.method == 'POST' and request.content_type.startswith('multipart/form-data'):
        logger.debug("Request contains a file upload.")

@app.route('/')
def index():
    logger.info("Serving index page.")
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    logger.info("Handling '/classify' endpoint.")
    file = request.files.get('image')

    if not validate_image(file):
        logger.warning("Invalid file or file format in request.")
        return jsonify({"error": "Invalid file format or no file uploaded"}), 400

    try:
        logger.info(f"File '{file.filename}' uploaded successfully.")
        image_name, result, confidence = predict_image(file)
        response = {
            'status': 'success',
            'image_name': image_name,
            'prediction': result,
            'confidence': confidence
        }
        logger.info(f"Prediction successful: {result} (confidence: {confidence})")
        return jsonify(response), 200
    except Exception as e:
        logger.error("Error during image classification", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.after_request
def log_response_info(response):
    """
    Basic log about the response sent.
    """
    logger.info(f"Response: {response.status_code} {response.get_json()}")
    return response
