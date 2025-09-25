import binascii
import time
import hashlib
import os
from .message import Message, MAX_MESSAGE_LENGTH
from .constants import IGNORE, COMMAND_LABELS
from ..singleton_registry import SingletonRegistry
from ..database import Database
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_command.ignore")

OUTGOING_MESSAGE_LOGGING_FORMAT = "[%s:%d %s] <- %s %s %s %s"


class Ignore(Message):
    def __init__(self, message={}):
        super().__init__(message)
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )
        self.db = Database.get_instance()
        self.speaker = self.db.get_knob("handle")
        self.command = IGNORE
        self.bounces = 0
        self.body = os.urandom(MAX_MESSAGE_LENGTH)

    def inflate(self, message):
        self.message_bytes = message.get("bytes")
        self.message_hash = Message.gen_hash(self.message_bytes)

        (
            int_ts,
            self_chain_ignore,
            net_chain_ignore,
            speaker,
            body,
        ) = self._unpack_generic_message(self.message_bytes)

        self.peer = message.get("peer")
        self.body = body
        self.timestamp = int_ts
        self.speaker = speaker
        self.bounces = message.get("bounces")
        self.self_chain = message.get("self_chain")
        self.net_chain = message.get("net_chain")
        self.metadata = message.get("metadata")
        return self

    def send(self):
        # since we are not rebroadcasting we need to set the timestamp
        self.timestamp = int(time.time())
        self.message_bytes = self.get_message_bytes()
        self.message_hash = hashlib.sha256(self.message_bytes).digest()

        for peer in self.db.get_keyed_peers(exclude_addressless=True):
            signed_packet_bytes = self.pack(
                peer, self.command, self.bounces, self.message_bytes
            )
            self.pest_service.enqueue_outbound_packet_to_address(
                {
                    "address": (peer.address, peer.port),
                    "black_packet": signed_packet_bytes,
                }
            )
            self.log_rubbish(peer)

    def log_rubbish(self, peer):
        logger.debug(
            OUTGOING_MESSAGE_LOGGING_FORMAT
            % (
                peer.address,
                peer.port,
                peer.handles[0],
                COMMAND_LABELS[self.command],
                "<rubbish>",
                self.bounces,
                binascii.hexlify(self.message_hash),
            )
        )
