import base64

from .constants import DIRECT_TEXT_M
from .multipart_message import MultipartMessage
from .direct_text import DirectText
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_command.direct_text_m")


class DirectTextM(MultipartMessage, DirectText):
    def __init__(self, command):
        super().__init__(command)
        self.command = DIRECT_TEXT_M

    def stringify(self):
        return {
            "command": "direct_text_m",
            "speaker": self.db.get_knob("handle"),
            "handle": self.peer.handle(),
            "body": self.body,
            "timestamp": self.get_adjusted_timestamp(),
            "net_chain": base64.b64encode(self.net_chain).decode(),
            "self_chain": base64.b64encode(self.net_chain).decode(),
            "n": self.n,
            "of": self.of,
            "message_hash": base64.b64encode(self.message_hash).decode(),
            "text_hash": base64.b64encode(self.text_hash).decode(),
        }

    def inflate(self, command):
        super().inflate(command)
        self.check_order()
        return self
