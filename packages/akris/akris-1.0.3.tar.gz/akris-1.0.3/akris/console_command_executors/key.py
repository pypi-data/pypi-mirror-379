from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Key:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 2:
            handle = args[0]
            key = args[1]
            if not len(key) == 88:
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"Invalid key {key}",
                }
            elif self.db.key_exists(key):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"Key {key} already exists",
                }
            elif handle not in self.db.get_peer_handles():
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"No such handle: {handle}",
                }
            else:
                self.db.add_key(handle, key)
                response = {
                    "command": "console_response",
                    "type": "key",
                    "body": f"Added key: {key} for peer: {handle}",
                }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["key"]["help"],
            }
        return response
