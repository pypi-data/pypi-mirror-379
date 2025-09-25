from akris.database import Database
from akris.console_command_executors.help import COMMANDS


class Knob:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 0:
            response = {
                "command": "console_response",
                "type": "knob",
                "body": self.db.get_knobs(),
            }
        elif len(args) == 1:
            if not self.db.has_knob(args[0]):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": "No knob named {}".format(args[0]),
                }
            else:
                response = {
                    "command": "console_response",
                    "type": "knob",
                    "body": {args[0]: self.db.get_knob(args[0])},
                    "name": args[0],
                    "value": self.db.get_knob(args[0]),
                }
        elif len(args) == 2:
            if not self.db.has_knob(args[0]):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": "No knob named {}".format(args[0]),
                }
            else:
                self.db.set_knob(args[0], args[1])
                response = {
                    "command": "console_response",
                    "type": "knob",
                    "body": {args[0]: self.db.get_knob(args[0])},
                    "name": args[0],
                    "value": self.db.get_knob(args[0]),
                }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["knob"]["help"],
            }
        return response
