from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Wot:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 0:
            # Display the current WOT
            peers = self.db.get_peers()
            response = {
                "command": "console_response",
                "type": "wot",
                "body": [p.serialize() for p in peers],
            }
        elif len(args) == 1:
            handle = args[0]
            peer = self.db.get_peer_by_handle(handle)
            if not peer:
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"No such handle: {handle}",
                }
            else:
                response = {
                    "command": "console_response",
                    "type": "wot",
                    "body": [peer.serialize()],
                }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["wot"]["help"],
            }
        return response
