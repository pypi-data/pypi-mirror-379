import base64
import hashlib
import hmac
import logging
import os
import struct
import time

from .message_exception import MessageException, DUPLICATE_PACKET
from .message import Message
from .constants import ADDRESS_CAST
from .prod import get_ascii_address
from .prod import OUTGOING
from .prod import INCOMING
from ..filter import Filter
from ..log_config import LogConfig
from ..singleton_registry import SingletonRegistry
from akris.c_serpent.serpent import encrypt, decrypt

logger = LogConfig.get_instance().get_logger("akris.pest_command.address_cast")

BLACK_PACKET_FORMAT = "<272s48s4s"
RED_PACKET_FORMAT = "<16sL6s246s"
LOGGING_FORMAT = "[%s:%d %s] %s %s %s %s"
NONCE_LENGTH = 16
RED_PACKET_PADDING_LENGTH = 246
PAYLOAD_PADDING_LENGTH = 4
SEND_PROD = 0x00
PORT_HAMMER = 0x01


class AddressCast(Message):
    def __init__(self, message):
        super().__init__(message)
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )
        self.command = ADDRESS_CAST
        self.address = message.get("external_address")
        self.bounces = message.get("bounces", 0)
        self.filter = Filter.get_instance()
        self.origin_peer = None
        self.flag = SEND_PROD

    def inflate(self, message):
        self.peer = message.get("peer")
        self.message_bytes = message.get("bytes")
        (int_ts, self_chain, net_chain, speaker, body) = self._unpack_generic_message(
            self.message_bytes
        )
        self.timestamp = int_ts
        self.speaker = speaker
        self.body = body
        self.message_hash = self.gen_hash(self.message_bytes)
        self.filter = Filter.get_instance()
        if self.filter.has(self.message_hash):
            raise MessageException(DUPLICATE_PACKET, self.metadata, self)

        # if the signature checks out decrypt
        for peer in self.db.get_keyed_peers(exclude_addressless=False):
            if peer:
                (
                    black_packet_bytes,
                    signature,
                ) = struct.unpack(
                    BLACK_PACKET_FORMAT, body
                )[0:2]

                for key in peer.keys:
                    key_bytes = base64.b64decode(key)
                    signing_key = key_bytes[:32]
                    cipher_key = key_bytes[32:]
                    signature_check = hmac.new(
                        signing_key, black_packet_bytes, hashlib.sha384
                    ).digest()

                    if signature_check != signature:
                        continue

                    red_packet_bytes = decrypt(cipher_key, black_packet_bytes)

            try:
                (flag, address) = struct.unpack(RED_PACKET_FORMAT, red_packet_bytes)[
                    1:3
                ]
                self.origin_peer = peer
                self.address = address
                self.flag = flag
                self.log_incoming(
                    message.get("peer"),
                    peer.handles[0],
                    get_ascii_address(address),
                )
                return self
            except NameError as ne:
                # This message was not intended for us.
                # We must forward it on if the bounce count is below the cutoff
                pass

        self.log_incoming(message.get("peer"), "N/A", "N/A")
        return self

    # Increment bounce count and send to everyone except originating peer
    def forward(self):
        # forward to everyone except the station from which we received this
        for peer in self.db.get_keyed_peers(
            exclude_addressless=True, exclude_ids=[self.peer.peer_id]
        ):
            self.message_bytes = self.get_message_bytes()
            signed_packet_bytes = self.pack(
                peer, self.command, self.bounces, self.message_bytes
            )
            self.pest_service.enqueue_outbound_packet_to_address(
                {
                    "address": (peer.address, peer.port),
                    "black_packet": signed_packet_bytes,
                }
            )

    # send to every peer with an address in the AT
    def broadcast(self):
        self.timestamp = int(time.time())

        # for each *cold* peer we have a key for
        cold_peers = self.db.get_cold_peers()
        cold_peer_ids = map(lambda p: p.peer_id, cold_peers)
        for peer in self.db.get_keyed_peers(
            exclude_addressless=True, exclude_ids=cold_peer_ids
        ):
            for cold_peer in cold_peers:
                # parse peer key
                key_bytes = base64.b64decode(cold_peer.get_key())
                signing_key = key_bytes[:32]
                cipher_key = key_bytes[32:]

                # build the red packet
                red_packet_bytes = struct.pack(
                    RED_PACKET_FORMAT,
                    os.urandom(NONCE_LENGTH),
                    1 if self.db.get_knob("port_hammering_enabled") else 0,
                    self.address,
                    os.urandom(RED_PACKET_PADDING_LENGTH),
                )
                # form the black packet by encrypting and signing the red packet
                black_packet_bytes = encrypt(cipher_key, red_packet_bytes)

                # sign and pack the black address cast packet
                seal = hmac.new(
                    signing_key, black_packet_bytes, hashlib.sha384
                ).digest()
                self.body = struct.pack(
                    BLACK_PACKET_FORMAT,
                    black_packet_bytes,
                    seal,
                    os.urandom(PAYLOAD_PADDING_LENGTH),
                )

                # send off the black packet
                self.message_bytes = self.get_message_bytes()
                self.message_hash = hashlib.sha256(self.message_bytes).digest()
                self.filter.intern(self)
                signed_packet_bytes = self.pack(
                    peer, self.command, self.bounces, self.message_bytes
                )
                self.pest_service.enqueue_outbound_packet_to_address(
                    {
                        "address": (peer.address, peer.port),
                        "black_packet": signed_packet_bytes,
                    }
                )
                self.log_outgoing(red_packet_bytes, cold_peer, peer)

    def log_incoming(self, peer, origin_peer_handle, address):
        params = (
            peer.address,
            peer.port,
            peer.handles[0],
            INCOMING,
            "ADDRESS_CAST",
            origin_peer_handle,
            address,
        )
        logger.info(LOGGING_FORMAT % params)

    def log_outgoing(self, red_packet_bytes, cold_peer, peer):
        (
            nonce,
            command,
            pest_address,
            padding,
        ) = struct.unpack(RED_PACKET_FORMAT, red_packet_bytes)

        logger.info(
            LOGGING_FORMAT
            % (
                peer.address,
                peer.port,
                peer.handles[0],
                OUTGOING,
                "ADDRESS_CAST",
                cold_peer.handles[0],
                get_ascii_address(pest_address),
            )
        )
