from ..singleton_registry import SingletonRegistry


class ResetDatabase:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, command):
        self.db.reset()
        return {
            "command": "console_response",
            "type": "reset_database",
            "body": "database reset",
        }
