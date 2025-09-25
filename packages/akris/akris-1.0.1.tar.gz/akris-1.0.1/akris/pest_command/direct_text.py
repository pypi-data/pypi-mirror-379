import base64
import hashlib
import struct

import time
import binascii

from ..database import Database
from ..pest_command.constants import DIRECT_TEXT
from ..pest_command.message import (
    Message,
    MAX_SPEAKER_SIZE,
    EMPTY_CHAIN,
    MESSAGE_PACKET_FORMAT,
)
from ..pest_command.text_message import TextMessage
from ..pest_command.message_exception import MessageException
from ..pest_command.message_exception import OUT_OF_ORDER_SELF
from ..singleton_registry import SingletonRegistry
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_command.direct_text")


class DirectText(TextMessage):
    def __init__(self, message):
        super().__init__(message)
        self.db = Database.get_instance()
        self.speaker = message.get("speaker")
        self.command = DIRECT_TEXT
        self.bounces = 0

    def stringify(self):
        return {
            "command": "direct_text",
            "handle": self.peer.handle(),
            "body": self.body,
            "message_hash": base64.b64encode(self.message_hash).decode("utf-8"),
            "net_chain": base64.b64encode(self.net_chain).decode("utf-8"),
            "self_chain": base64.b64encode(self.self_chain).decode("utf-8"),
            "speaker": self.speaker,
            "timestamp": self.get_adjusted_timestamp(),
        }

    def inflate(self, message):
        self.message_bytes = message.get("bytes")
        self.message_hash = Message.gen_hash(self.message_bytes)

        (int_ts, self_chain, net_chain, speaker, body) = self._unpack_generic_message(
            self.message_bytes, unpad_body=True
        )

        self.handle = self.db.get_knob('handle')
        self.peer = message.get("peer")
        self.body = body
        self.timestamp = int_ts
        self.speaker = speaker
        self.bounces = message.get("bounces")
        self.self_chain = self_chain
        self.net_chain = net_chain
        self.metadata = message.get("metadata")

        self.check_if_stale()
        self.check_if_duplicate()
        self.check_order()
        return self

    def send(self):
        if not self.speaker:
            logger.error("aborting message send due speaker not being set")
            return

        self.timestamp = int(time.time())
        target_peer = self.db.get_peer_by_handle(self.handle)
        if target_peer and not target_peer.get_key():
            logger.debug("No key for peer associated with %s" % self.handle)
            return

        if target_peer == None:
            logger.debug("Aborting message: unknown handle: %s" % self.handle)
            return

        self.message_bytes = self.get_message_bytes(target_peer)
        self.message_hash = hashlib.sha256(self.message_bytes).digest()

        logger.debug("generated message_hash: %s" % binascii.hexlify(self.message_hash))

        self.peer = target_peer
        self.filter.intern(self)

        signed_packet_bytes = self.pack(
            target_peer, self.command, self.bounces, self.message_bytes
        )
        self.db.update_handle_self_chain(target_peer.handles[0], self.message_hash)
        self.pest_service.enqueue_outbound_packet_to_address(
            {
                "black_packet": signed_packet_bytes,
                "address": (
                    target_peer.address,
                    target_peer.port,
                ),
            }
        )
        self.log_outgoing(target_peer)

    def get_message_bytes(self, peer=None):
        speaker = Message._pad(self.speaker, MAX_SPEAKER_SIZE)

        # let's generate the self_chain value from the last message or set it to zero if
        # this is the first message

        self.self_chain = self.db.get_handle_self_chain(peer.handles[0])
        self.net_chain = self.db.get_handle_net_chain(peer.handles[0])

        body = self.body.encode("utf-8", errors="replace")

        message_bytes = struct.pack(
            MESSAGE_PACKET_FORMAT,
            self.timestamp,
            self.self_chain,
            self.net_chain,
            speaker,
            body,
        )
        return message_bytes

    def retry(self, requesting_peer):
        if requesting_peer == None:
            logger.debug(
                "Aborting message: unknown peer: %s" % requesting_peer.handles[0]
            )
            return

        if not requesting_peer.get_key():
            logger.debug(
                "No key for peer associated with %s" % requesting_peer.handles[0]
            )
            return

        # TODO: Figure out how to verify that the requester was the original intended recipient
        signed_packet_bytes = self.pack(
            requesting_peer, self.command, self.bounces, self.message_bytes
        )
        self.pest_service.enqueue_outbound_packet_to_address(
            {
                "black_packet": signed_packet_bytes,
                "address": (
                    requesting_peer.address,
                    requesting_peer.port,
                ),
            }
        )
        self.log_outgoing(requesting_peer)
