import os
import logging
from logging.handlers import RotatingFileHandler
from .singleton import Singleton
AKRIS_DATA_PATH = os.path.join(os.path.expanduser("~"), ".akris")

# Since LogConfig is called in many places, its easier just to parse the cmdline args here as well
class LogConfig(Singleton):
    def __init__(self, data_path=AKRIS_DATA_PATH):

        if not os.path.exists(data_path):
            os.makedirs(data_path)

        # Check if the directory exists
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        log_path = os.path.join(data_path, "logs")
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        self.handler = RotatingFileHandler(os.path.join(log_path, "station.log"), maxBytes=10**7)

    def get_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(self.handler)
        return logger
