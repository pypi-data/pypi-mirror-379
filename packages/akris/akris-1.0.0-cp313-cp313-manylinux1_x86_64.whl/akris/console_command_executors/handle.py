from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Handle:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 0:
            # fetch the station handle if it exists
            response = {
                "command": "console_response",
                "type": "handle",
                "body": self.db.get_knob("handle"),
            }
        elif len(args) == 1:
            # set the station handle
            self.db.set_knob("handle", args[0])
            response = {
                "command": "console_response",
                "type": "handle",
                "body": f"Handle set to {args[0]}",
            }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["handle"]["help"],
            }
        return response
