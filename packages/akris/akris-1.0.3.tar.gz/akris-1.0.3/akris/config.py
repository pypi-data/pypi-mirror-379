from .singleton import Singleton


class Config(Singleton):
    def __init__(self, config={}):
        for key, value in config.items():
            setattr(self, key, value)
