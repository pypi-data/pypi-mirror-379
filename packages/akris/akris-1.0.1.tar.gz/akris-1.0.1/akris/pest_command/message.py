from .constants import COMMAND_LABELS
from .message_exception import MessageException, INVALID_HANDLE_ENCODING
import hashlib
import base64
import binascii
import time
import struct
import hmac
import os
import logging

from akris.c_serpent.serpent import encrypt

PEST_VERSION = 0xFA
EARLIEST_SUPPORTED_PEST_VERSION = 0xFC
PACKET_SIZE = 496
MAX_SPEAKER_SIZE = 32
TS_ACCEPTABLE_SKEW = 60 * 15
BLACK_PACKET_FORMAT = "<448s48s"
RED_PACKET_FORMAT = "<16sBBxB428s"
MESSAGE_PACKET_FORMAT = "<q32s32s32s324s"
MAX_MESSAGE_LENGTH = 428
NONCE_LENGTH = 16
TEXT_PAYLOAD_SIZE = 324

# logging formats
OUTGOING_MESSAGE_LOGGING_FORMAT = "[%s:%d %s] <- %s %s %s %s"
INCOMING_MESSAGE_LOGGING_FORMAT = "[%s:%d %s] -> %s %s %d %s"

EMPTY_CHAIN = ("\x00" * 32).encode("utf-8")


class Message(object):
    def __init__(self, message):
        # target peer handle
        self.handle = message.get("handle")
        self.peer = message.get("peer")
        self.body = message.get("body")
        self.timestamp = message.get("timestamp")
        self.speaker = message.get("speaker")
        self.self_chain = message.get("self_chain")
        self.net_chain = message.get("net_chain")
        self.self_chain_valid = message.get("self_chain_valid")
        self.error_code = message.get("error_code")
        self.message_hash = message.get("message_hash")
        self.message_bytes = message.get("message_bytes")
        self.get_data_response = message.get("get_data_response")
        self.metadata = message.get("metadata")

    @classmethod
    def pack(cls, peer, command, bounces, message_bytes):
        key_bytes = bytes(base64.b64decode(peer.get_key()))
        signing_key = key_bytes[:32]
        cipher_key = key_bytes[32:]

        # pack packet bytes
        nonce = os.urandom(NONCE_LENGTH)

        version = PEST_VERSION
        red_packet_bytes = struct.pack(
            RED_PACKET_FORMAT,
            nonce,
            bounces,
            version,
            command,
            cls._pad(message_bytes, MAX_MESSAGE_LENGTH),
        )

        black_packet_bytes = encrypt(cipher_key, red_packet_bytes)

        # sign packet
        signature_bytes = hmac.new(
            signing_key, black_packet_bytes, hashlib.sha384
        ).digest()

        # pack the signed black packet
        signed_packet_bytes = struct.pack(
            BLACK_PACKET_FORMAT, black_packet_bytes, signature_bytes
        )

        return signed_packet_bytes

    def _unpack_generic_message(self, message_bytes, unpad_body=False):
        int_ts, self_chain, net_chain, speaker, body = struct.unpack(
            MESSAGE_PACKET_FORMAT, message_bytes
        )
        self.assert_ascii(speaker)
        speaker = speaker.rstrip(b"\x00")
        speaker = speaker.decode("ascii")

        if unpad_body:
            body = self._unpad(body, "utf-8")

        return int_ts, self_chain, net_chain, speaker, body

    @classmethod
    def _unpad(cls, text, encoding):
        stripped_text = text.rstrip(b"\x00")

        try:
            return stripped_text.decode(encoding)

        except Exception:
            return text

    @classmethod
    def _pad(cls, text, size):
        try:
            return text.ljust(size, b"\x00")
        except TypeError:
            return text.encode("ascii").ljust(size, b"\x00")

    @classmethod
    def _check_for_ascii_encoding(cls, handle):
        for c in handle:
            if ord(c) not in range(0, 127):
                return False
        return True

    @classmethod
    def _ts_range(cls):
        current_ts = int(time.time())
        return range(current_ts - TS_ACCEPTABLE_SKEW, current_ts + TS_ACCEPTABLE_SKEW)

    @classmethod
    def gen_hash(cls, message_bytes):
        return hashlib.sha256(message_bytes).digest()

    def get_message_bytes(self):
        speaker = Message._pad(self.speaker, MAX_SPEAKER_SIZE)
        self.self_chain = self.net_chain = EMPTY_CHAIN
        message_bytes = struct.pack(
            MESSAGE_PACKET_FORMAT,
            self.timestamp,
            self.self_chain,
            self.net_chain,
            speaker,
            self.body,
        )
        return message_bytes

    def compute_message_hash(self):
        if self.message_hash is None:
            if self.message_bytes is not None:
                self.message_hash = Message.gen_hash(self.message_bytes)
                return self.message_hash
            else:
                return None
        else:
            return self.message_hash

    def log_outgoing(self, peer):
        logging.info(
            OUTGOING_MESSAGE_LOGGING_FORMAT
            % (
                peer.address,
                peer.port,
                peer.handles[0],
                COMMAND_LABELS[self.command],
                self.body,
                self.bounces,
                binascii.hexlify(self.compute_message_hash()),
            )
        )

    def log_incoming(self, peer):
        try:
            logging.info(
                INCOMING_MESSAGE_LOGGING_FORMAT
                % (
                    peer.address,
                    peer.port,
                    peer.handles[0],
                    COMMAND_LABELS[self.command],
                    self.body,
                    self.bounces,
                    binascii.hexlify(self.message_hash),
                )
            )
        except Exception as ex:
            logging.exception("unable to log incoming message")

    def log_incoming_get_data(self, peer):
        try:
            logging.info(
                INCOMING_MESSAGE_LOGGING_FORMAT
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
        except Exception as ex:
            logging.exception("unable to log incoming message")

    def retry(self, requesting_peer):
        logging.debug("Can't retry a message that isn't DIRECT or BROADCAST")

        return

    @classmethod
    def in_time_window(cls, timestamp):
        return timestamp in cls._ts_range()

    def assert_ascii(self, text):
        if not text.isascii():
            raise MessageException(INVALID_HANDLE_ENCODING, self.metadata, self)
