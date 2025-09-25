import base64

from .multipart_message import MultipartMessage
from .broadcast_text import BroadcastText
from .constants import BROADCAST_TEXT_M


class BroadcastTextM(MultipartMessage, BroadcastText):
    def __init__(self, command):
        super().__init__(command)
        self.command = BROADCAST_TEXT_M

    def inflate(self, command):
        super().inflate(command)
        self.check_order()
        return self

    def stringify(self):
        return {
            "command": "broadcast_text_m",
            "speaker": self.db.get_knob("handle"),
            "body": self.body,
            "timestamp": self.get_adjusted_timestamp(),
            "net_chain": base64.b64encode(self.net_chain).decode(),
            "self_chain": base64.b64encode(self.net_chain).decode(),
            "n": self.n,
            "of": self.of,
            "message_hash": base64.b64encode(self.message_hash).decode(),
            "text_hash": base64.b64encode(self.text_hash).decode(),
            "immediate": self.immediate,
            "reporting_peers": self.reporting_peer_handles(),
        }
