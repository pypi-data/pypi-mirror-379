from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Unkey:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 1:
            if not self.db.key_exists(args[0]):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"No such key: {args[0]}",
                }
            else:
                self.db.remove_key(args[0])
                response = {
                    "command": "console_response",
                    "type": "unkey",
                    "body": f"Removed key: {args[0]}",
                }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["unkey"]["help"],
            }
        return response
