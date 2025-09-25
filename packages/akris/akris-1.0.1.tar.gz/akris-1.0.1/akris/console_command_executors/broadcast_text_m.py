import time

from .console_command_executor import split_utf8
from ..pest_command.broadcast_text_m import BroadcastTextM as BroadcastTextMCommand
from ..singleton_registry import SingletonRegistry


class BroadcastTextM:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, args):
        concatenated_messages = []
        parts = []
        for chunk in split_utf8(args[0]):
            parts.append(chunk)
        of = len(parts)
        # text_hash and timestamp must be identical for all parts
        text_hash = BroadcastTextMCommand.gen_hash(args[0].encode("utf-8", errors="replace"))
        timestamp = int(time.time())
        prev_message_hash = None
        for n in range(1, of + 1):
            broadcast_text_m = BroadcastTextMCommand(
                {
                    "n": n,
                    "of": of,
                    "speaker": self.db.get_knob("handle"),
                    "body": parts[n - 1],
                    "text_hash": text_hash,
                    "timestamp": timestamp,
                    "prev_message_hash": prev_message_hash,
                },
            )
            broadcast_text_m.send()
            prev_message_hash = broadcast_text_m.message_hash

            # send the message to the client to display
            concatenated_messages.append(broadcast_text_m.stringify())
        return concatenated_messages
