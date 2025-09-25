class SingletonRegistry:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self._registry = {}

    def register(self, cls):
        self._registry[cls.__name__] = cls

    def get(self, name):
        return self._registry.get(name)
