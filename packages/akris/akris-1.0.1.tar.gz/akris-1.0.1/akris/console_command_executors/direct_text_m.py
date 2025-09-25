import base64
import time

from .console_command_executor import split_utf8
from ..singleton_registry import SingletonRegistry
from ..pest_command.direct_text_m import DirectTextM as DirectTextMCommand


class DirectTextM:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, args):
        concatenated_messages = []
        parts = []
        for chunk in split_utf8(args[1]):
            parts.append(chunk)
        of = len(parts)
        # text_hash and timestamp must be identical for all parts
        text_hash = DirectTextMCommand.gen_hash(args[1].encode("utf-8", errors="replace"))
        timestamp = int(time.time())
        prev_message_hash = None
        for n in range(1, of + 1):
            direct_text_m = DirectTextMCommand(
                {
                    "handle": args[0],
                    "n": n,
                    "of": of,
                    "speaker": self.db.get_knob("handle"),
                    "body": parts[n - 1],
                    "text_hash": text_hash,
                    "timestamp": timestamp,
                    "prev_message_hash": prev_message_hash,
                },
            )
            direct_text_m.send()
            prev_message_hash = direct_text_m.message_hash

            # send the message to the client to display
            concatenated_messages.append(direct_text_m.stringify())
        return concatenated_messages
