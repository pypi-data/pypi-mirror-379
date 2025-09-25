import struct
import time
import binascii
import hashlib
import logging
from .message import Message
from .message import OUTGOING_MESSAGE_LOGGING_FORMAT
from .constants import GET_DATA
from .constants import COMMAND_LABELS
from ..singleton_registry import SingletonRegistry

GETDATA_MESSAGE_PACKET_FORMAT = "<q32s32s32s32s292s"


class GetData(Message):
    def __init__(self, message):
        super(GetData, self).__init__(message)
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.timestamp = int(time.time())
        self.speaker = message.get("speaker")
        self.command = GET_DATA
        self.bounces = 0
        self.body = message.get("body")
        self.target_peer = message.get("target_peer")
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )

    def inflate(self, message):
        self.message_bytes = message.get("bytes")
        self.message_hash = Message.gen_hash(self.message_bytes)

        int_ts, self_chain, net_chain, speaker, body = self._unpack()

        self.peer = message.get("peer")
        self.bounces = message.get("bounces")
        self.body = body
        self.timestamp = int_ts
        self.speaker = speaker
        self.self_chain = self_chain
        self.net_chain = net_chain
        self.metadata = message.get("metadata")
        return self

    def _unpack(self):
        # TODO: possibly don't need to use different format - maybe can just unpad body
        int_ts, self_chain, net_chain, speaker, body, padding = struct.unpack(
            GETDATA_MESSAGE_PACKET_FORMAT, self.message_bytes
        )
        self.assert_ascii(speaker)
        speaker = self._unpad(speaker, "ascii")
        return int_ts, self_chain, net_chain, speaker, body

    def send(self):
        self.message_bytes = self.get_message_bytes()
        self.message_hash = hashlib.sha256(self.message_bytes).digest()
        for peer in self.db.get_keyed_peers(exclude_addressless=True):
            signed_packet_bytes = self.pack(
                peer, self.command, self.bounces, self.message_bytes
            )
            self.pest_service.enqueue_outbound_packet_to_address(
                {
                    "black_packet": signed_packet_bytes,
                    "address": (peer.address, peer.port),
                }
            )
            self.log_outgoing(peer)

    def log_outgoing(self, peer):
        logging.info(
            OUTGOING_MESSAGE_LOGGING_FORMAT
            % (
                peer.address,
                peer.port,
                peer.handles[0],
                COMMAND_LABELS[self.command],
                binascii.hexlify(self.body),
                self.bounces,
                binascii.hexlify(self.message_hash),
            )
        )
