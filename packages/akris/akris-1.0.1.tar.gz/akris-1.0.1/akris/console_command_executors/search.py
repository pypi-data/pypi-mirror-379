import json

from .console_command_executor import ConsoleCommandExecutor
from .help import COMMANDS
from ..database import Database

def fix_phf_search_result(message):
    try:
        fixed_message = message[4:]
        fixed_message = fixed_message[:-38]
        fixed_message = fixed_message.rstrip(b"\x00")
        fixed_message = fixed_message.decode("utf-8")
        return fixed_message

    except UnicodeError:
        message["body"] = message["body"].decode("utf-8", errors="replace")
        return message
class Search(ConsoleCommandExecutor):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 1:
            search_string = args[0]
            messages = self.db.search(search_string)
            response = {
                "command": "console_response",
                "type": "search",
                "body": self.clean(messages)
            }
        elif len(args) == 2:
            speaker = args[0]
            search_string = args[1]
            messages = self.db.search(search_string, speaker=speaker)
            response = {
                "command": "console_response",
                "type": "search",
                "body": self.clean(messages)
            }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["search"]["help"]
            }
        return response

    def clean(self, messages):
        results = []
        for row in messages:
            try:
                json.dumps(row[2])
                results.append(row)
            except:
                fixed_row = (row[0], row[1], fix_phf_search_result(row[2]), row[3])
                results.append(fixed_row)
        return results
