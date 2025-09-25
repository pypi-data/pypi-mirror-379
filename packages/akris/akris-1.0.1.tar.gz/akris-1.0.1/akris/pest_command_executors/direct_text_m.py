import base64

from .direct_text import DirectText


class DirectTextM(DirectText):
    def __init__(self):
        super().__init__()

    def deliver(self, command):
        message_dict = {
            "command": "direct_text_m",
            "body": command.body,
            "message_hash": base64.b64encode(command.message_hash).decode("utf-8"),
            "net_chain": base64.b64encode(command.net_chain).decode("utf-8"),
            "self_chain": base64.b64encode(command.self_chain).decode("utf-8"),
            "speaker": command.speaker,
            "timestamp": command.timestamp,
            "n": command.n,
            "of": command.of,
            "text_hash": base64.b64encode(command.text_hash).decode("utf-8"),
        }

        # send to the client
        self.api_service.enqueue_outbound(message_dict)

        # store
        self.filter.intern(command)
