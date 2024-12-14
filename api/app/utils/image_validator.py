from PIL import Image
from app.utils.logging_helper import get_logger

logger = get_logger()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """
    Checks whether the file name has a permitted extension.
    
    Args:
        filename (str): File name.

    Returns:
        bool: True if the extension is allowed, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image(file):
    if file and allowed_file(file.filename):
        try:
            img = Image.open(file)
            img.verify()  # Verifies that it's a valid image
            return True
        except (IOError, SyntaxError) as e:
            logger.error(f"Invalid image file: {e}")
            return False
    return False

