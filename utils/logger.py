import logging

def setup_logger(name: str = "test-logger") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    return logger