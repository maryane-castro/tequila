import logging

def setup_logger(log_file="app.log", log_level=logging.DEBUG):
    """
    Configures the logger for the application.
    
    :param log_file: File where the logs will be saved. The default is "app.log".
    :param log_level: Log level. The default is DEBUG.
    :return: The configured logger object.
    """
    logger = logging.getLogger("app_logger")

    if logger.hasHandlers():
        return logger

    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def get_logger():
    """
    Returns the logger configured to be used in other modules.
    """
    return setup_logger()
