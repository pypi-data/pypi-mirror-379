import binascii
import time
import hashlib
import socket
import struct

from ..pest_command.constants import PROD
from ..pest_command.message import Message
from ..singleton_registry import SingletonRegistry
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_command.prod")

PROD_PROMPT = 0x00
PROD_REPLY = 0x1
PROD_MESSAGE_PACKET_FORMAT = "<h6s32s32s32s220s"
PEST_ADDRESS = "<H4s"
PROD_MESSAGE_LOGGING_FORMAT = "[%s:%d %s] %s %s flag: %d %s %s %s %s %s"
INCOMING = "->"
OUTGOING = "<-"


def get_ascii_address(bytes):
    port, address_bytes = struct.unpack(PEST_ADDRESS, bytes)
    dotted_quad = socket.inet_ntoa(address_bytes)
    return "%s:%d" % (dotted_quad, port)


def get_pest_address_bytes(peer):
    if peer.address in "localhost":
        ip_bytes = socket.inet_aton("127.0.0.1")
    else:
        ip_bytes = socket.inet_aton(peer.address)
    return struct.pack(PEST_ADDRESS, peer.port, ip_bytes)


class Prod(Message):
    def __init__(self, message):
        super().__init__(message)
        self.speaker = message.get("speaker")
        self.command = PROD
        self.bounces = 0
        self.prompt = message.get("prompt")
        self.flag = message.get("flag")
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )
        self.scheduler = (
            SingletonRegistry.get_instance().get("Scheduler").get_instance()
        )

    def inflate(self, message):
        self.message_bytes = message.get("bytes")
        self.message_hash = Message.gen_hash(self.message_bytes)

        (
            int_ts,
            self_chain_ignore,
            net_chain_ignore,
            speaker,
            prod_bytes,
        ) = self._unpack_generic_message(self.message_bytes)

        (
            flag,
            address,
            broadcast_self_chain,
            net_chain,
            handle_self_chain,
            banner,
        ) = struct.unpack(PROD_MESSAGE_PACKET_FORMAT, prod_bytes)

        self.timestamp = int_ts
        self.peer = message.get("peer")
        self.flag = flag
        self.speaker = speaker
        self.broadcast_self_chain = broadcast_self_chain
        self.handle_self_chain = handle_self_chain
        self.net_chain = net_chain
        self.banner = self._unpad(banner, "utf-8")
        self.metadata = message.get("metadata")
        self.pest_address = address
        return self

    def broadcast(self):
        for peer in self.db.get_keyed_peers(exclude_addressless=True):
            self.prepare_and_send(peer)
            self.log_outgoing(peer)

    def send(self, peer):
        self.prepare_and_send(peer)
        self.log_outgoing(peer)

    def reply(self):
        self.prepare_and_send(self.prompt.peer)
        self.log_outgoing(self.prompt.peer)

    def prepare_and_send(self, peer):
        self.set_body(peer)
        self.timestamp = int(time.time())
        self.message_bytes = self.get_message_bytes()
        self.message_hash = hashlib.sha256(self.message_bytes).digest()
        signed_packet_bytes = self.pack(
            peer, self.command, self.bounces, self.message_bytes
        )

        self.pest_service.enqueue_outbound_packet_to_address(
            {
                "black_packet": signed_packet_bytes,
                "address": (peer.address, peer.port),
            }
        )

    def set_body(self, peer):
        address = get_pest_address_bytes(peer)
        nc = SingletonRegistry.get_instance().get("NetChain").get_instance()
        self.body = struct.pack(
            PROD_MESSAGE_PACKET_FORMAT,
            self.flag,
            address,
            self.db.get_broadcast_self_chain(),
            nc.get_broadcast_net_chain(),
            self.db.get_handle_self_chain(peer.handle()),
            self._pad(self.db.get_knob("banner"), 220),
        )

    def log_outgoing(self, peer):
        (
            flag,
            pest_address,
            broadcast_self_chain,
            net_chain,
            handle_self_chain,
            banner,
        ) = struct.unpack(PROD_MESSAGE_PACKET_FORMAT, self.body)

        logger.info(
            PROD_MESSAGE_LOGGING_FORMAT
            % (
                peer.address,
                peer.port,
                peer.handles[0],
                OUTGOING,
                "PROD",
                flag,
                self._unpad(banner, "utf-8"),
                get_ascii_address(pest_address),
                binascii.hexlify(net_chain),
                binascii.hexlify(broadcast_self_chain),
                binascii.hexlify(handle_self_chain),
            )
        )

    def log_incoming(self, peer):
        try:
            logger.info(
                PROD_MESSAGE_LOGGING_FORMAT
                % (
                    peer.address,
                    peer.port,
                    peer.handles[0],
                    INCOMING,
                    "PROD",
                    self.flag,
                    self.banner,
                    get_ascii_address(self.pest_address),
                    binascii.hexlify(self.net_chain),
                    binascii.hexlify(self.broadcast_self_chain),
                    binascii.hexlify(self.handle_self_chain),
                )
            )
        except Exception as e:
            logger.error(e)
