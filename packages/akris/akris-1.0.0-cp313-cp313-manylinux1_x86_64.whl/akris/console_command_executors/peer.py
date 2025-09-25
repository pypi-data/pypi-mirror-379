from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Peer:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) != 1:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["peer"]["help"],
            }
        else:
            if not self.db.get_peer_by_handle(args[0]):
                self.db.add_peer(args[0])
                response = {
                    "command": "console_response",
                    "type": "peer",
                    "body": "Peer added",
                }
            else:
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"Peer already exists: {args[0]}",
                }
        return response
