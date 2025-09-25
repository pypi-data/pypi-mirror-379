import os
import struct
import time

from .constants import KEY_OFFER
from .message import Message, MAX_SPEAKER_SIZE, MAX_MESSAGE_LENGTH
from ..singleton_registry import SingletonRegistry
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_command.key_offer")

LOGGING_FORMAT = "[%s:%d %s] %s %s"
INCOMING = "->"
OUTGOING = "<-"
KEY_OFFER_PACKET_FORMAT = "<q64s32s64s260s"


class KeyOffer(Message):
    def __init__(self, command):
        super().__init__(command)
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )
        self.command = KEY_OFFER
        self.timestamp = int(time.time())
        self.speaker = self.db.get_knob("handle")
        self.peer = command.get("peer")
        self.bounces = 0
        self.offer = None

    def inflate(self, command):
        self.message_bytes = command.get("bytes")
        data = self._unpack_key_offer_message(self.message_bytes)
        self.peer = command.get("peer")
        self.timestamp = data.get("timestamp")
        self.speaker = data.get("speaker").rstrip(b"\x00").decode("ascii")
        self.offer = data.get("offer")

        self.log_incoming()
        return self

    def get_message_bytes(self):
        self.offer = self.db.get_key_offer(self.peer.peer_id)
        message_bytes = struct.pack(
            KEY_OFFER_PACKET_FORMAT,
            self.timestamp,
            os.urandom(64),
            self._pad(self.speaker, MAX_SPEAKER_SIZE),
            self.offer,
            os.urandom(260),
        )
        assert len(message_bytes) == MAX_MESSAGE_LENGTH
        return message_bytes

    def _unpack_key_offer_message(self, message_bytes):
        int_ts, _, speaker, offer, _ = struct.unpack(
            KEY_OFFER_PACKET_FORMAT, message_bytes
        )

        return {
            "timestamp": int_ts,
            "speaker": speaker,
            "offer": offer,
        }

    def send(self):
        signed_packet_bytes = self.pack(
            self.peer, self.command, self.bounces, self.get_message_bytes()
        )
        self.pest_service.enqueue_outbound_packet_to_address(
            {
                "address": (self.peer.address, self.peer.port),
                "black_packet": signed_packet_bytes,
            }
        )
        self.log_outgoing()

    def log_incoming(self):
        logger.info(
            LOGGING_FORMAT
            % (
                self.peer.address,
                self.peer.port,
                self.peer.handles[0],
                INCOMING,
                "KEY_OFFER",
            )
        )

    def log_outgoing(self):
        logger.info(
            LOGGING_FORMAT
            % (
                self.peer.address,
                self.peer.port,
                self.peer.handles[0],
                OUTGOING,
                "KEY_OFFER",
            )
        )
