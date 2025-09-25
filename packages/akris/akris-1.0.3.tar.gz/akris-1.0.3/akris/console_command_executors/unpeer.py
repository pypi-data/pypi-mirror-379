from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Unpeer:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) != 1:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["unpeer"]["help"],
            }
        else:
            handle = args[0]
            if not self.db.get_peer_by_handle(handle):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"No such peer: {handle}",
                }
            else:
                self.db.remove_peer(handle)
                response = {
                    "command": "console_response",
                    "type": "unpeer",
                    "body": f"Peer {handle} removed",
                }
        return response
