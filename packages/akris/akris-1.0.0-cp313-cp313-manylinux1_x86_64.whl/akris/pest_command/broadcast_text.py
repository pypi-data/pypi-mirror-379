import base64
import struct

import time
import hashlib
from .constants import BROADCAST_TEXT
from .message import MAX_SPEAKER_SIZE, MESSAGE_PACKET_FORMAT
from .text_message import TextMessage
from ..singleton_registry import SingletonRegistry
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_command.broadcast")


class BroadcastText(TextMessage):
    def __init__(self, message):
        super().__init__(message)
        self.speaker = message.get("speaker")
        self.command = BROADCAST_TEXT
        self.bounces = message.get("bounces", 0)
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )

    def stringify(self):
        return {
            "command": "broadcast_text",
            "body": self.body,
            "message_hash": base64.b64encode(self.message_hash).decode("utf-8"),
            "net_chain": base64.b64encode(self.net_chain).decode("utf-8"),
            "self_chain": base64.b64encode(self.self_chain).decode("utf-8"),
            "speaker": self.speaker,
            "timestamp": self.get_adjusted_timestamp(),
            "immediate": self.immediate,
            "reporting_peers": self.reporting_peer_handles()
        }

    def inflate(self, message):
        self.message_bytes = message.get("bytes")
        self.message_hash = self.gen_hash(self.message_bytes)

        (int_ts, self_chain, net_chain, speaker, body) = self._unpack_generic_message(
            self.message_bytes, unpad_body=True
        )

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

    # evidently send is only called for messages originating from the client
    def send(self):
        # since we are not rebroadcasting we need to set the timestamp
        if not self.timestamp:
            self.timestamp = int(time.time())

        self.message_bytes = self.get_message_bytes()
        self.message_hash = hashlib.sha256(self.message_bytes).digest()

        self.filter.intern(self)

        self.db.update_broadcast_self_chain(self.message_hash)

        # disable broadcast on this station for testing purposes
        if self.db.get_knob("testing.disable_broadcast"):
            return

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

    def get_message_bytes(self):
        speaker = self._pad(self.speaker, MAX_SPEAKER_SIZE)

        # let's generate the self_chain value from the last message or set it to zero if
        # this is the first message

        self.self_chain = self.db.get_broadcast_self_chain()
        nc = SingletonRegistry.get_instance().get("NetChain").get_instance()
        self.net_chain = nc.get_broadcast_net_chain()

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

    # we already have message bytes here since this message came from the long buffer
    def retry(self, requesting_peer):
        signed_packet_bytes = self.pack(
            requesting_peer, self.command, self.bounces, self.message_bytes
        )
        self.pest_service.enqueue_outbound_packet_to_address(
            {
                "black_packet": signed_packet_bytes,
                "address": (requesting_peer.address, requesting_peer.port),
            }
        )
        self.log_outgoing(requesting_peer)

    def forward(self):
        reporting_peer_ids = self.reporting_peer_ids()
        for peer in self.db.get_keyed_peers(
            exclude_addressless=True, exclude_ids=reporting_peer_ids
        ):
            # we don't want to send a broadcast back to the originator
            if self.peer and (peer.peer_id == self.peer.peer_id):
                continue

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

    def reporting_peer_ids(self):
        return self.db.get_reporting_peer_ids(self.message_hash)

    def reporting_peer_handles(self):
        return self.db.get_reporting_peer_handles(self.message_hash)
