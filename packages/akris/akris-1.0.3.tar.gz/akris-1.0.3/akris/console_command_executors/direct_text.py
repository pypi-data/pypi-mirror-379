from .console_command_executor import split_utf8
from ..singleton_registry import SingletonRegistry
from ..pest_command.direct_text import DirectText as DirectTextCommand
from ..filter import Filter


class DirectText:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, args):
        # send directly to peer with handle
        parts = []
        for chunk in split_utf8(args[1], maxsize=324):
            direct_text = DirectTextCommand(
                {
                    "speaker": self.db.get_knob("handle"),
                    "handle": args[0],
                    "body": chunk,
                    "filter": Filter.get_instance(),
                },
            )
            direct_text.send()

            # send the message to the client to display
            parts.append(direct_text.stringify())
        return parts
