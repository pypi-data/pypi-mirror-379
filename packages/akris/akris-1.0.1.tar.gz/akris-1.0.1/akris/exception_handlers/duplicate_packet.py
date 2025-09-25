from ..database import Database
from ..singleton_registry import SingletonRegistry
from ..pest_command.constants import BROADCAST_TEXT, BROADCAST_TEXT_M
from base64 import b64encode

class DuplicatePacket:
    def __init__(self):
        self.db = Database.get_instance()
        self.filter = SingletonRegistry.get_instance().get("Filter").get_instance()
        self.api_service = SingletonRegistry.get_instance().get("ApiService").get_instance()

    def handle(self, exception):
        message = exception.object
        own_handle = self.db.get_knob("handle")

        # if we didn't originate this packet
        if message.speaker == own_handle:
            return

        # and the packet is still in the cache
        if not self.filter.cache_has(message.message_hash):
            return

        if message.command not in [BROADCAST_TEXT, BROADCAST_TEXT_M]:
            return

        # log the reporting peer
        self.db.log_reporting_peer(message.message_hash, message.peer.peer_id)

        # notify client

        self.api_service.enqueue_outbound(
            {
                "command": "message_update",
                "message_hash": b64encode(message.message_hash).decode("utf-8"),
                "reporting_peer": message.peer.handle(),
                "message_command": message.command,
                "timestamp": message.timestamp,
            }
        )