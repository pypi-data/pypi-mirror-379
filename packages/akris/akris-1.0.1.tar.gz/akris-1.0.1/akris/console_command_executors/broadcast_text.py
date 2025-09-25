from .console_command_executor import split_utf8
from ..pest_command.broadcast_text import BroadcastText as BroadcastTextCommand
from ..singleton_registry import SingletonRegistry


class BroadcastText:
    def __init__(self):
        super().__init__()
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, args):
        # broadcast the message to the network
        parts = []
        for chunk in split_utf8(args[0], maxsize=324):
            broadcast_text = BroadcastTextCommand(
                {
                    "speaker": self.db.get_knob("handle"),
                    "body": chunk,
                },
            )
            broadcast_text.send()

            # send the message to the client to display
            parts.append(broadcast_text.stringify())
        return parts
