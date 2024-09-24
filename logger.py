import logging
import os

def setup_logger(path, log_level=logging.INFO):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    logging.basicConfig(
        filename="app.log",
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logger = logging.getLogger(__name__)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(message)s]"))
    logger.addHandler(console_handler)

    return logger
