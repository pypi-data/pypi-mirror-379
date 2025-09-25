import base64
import hashlib
import hmac
import struct
import logging

from .pest_command.message import EARLIEST_SUPPORTED_PEST_VERSION
from .pest_command.constants import *
from .pest_command.prod import Prod
from .pest_command.direct_text import DirectText
from .pest_command.direct_text_m import DirectTextM
from .pest_command.broadcast_text import BroadcastText
from .pest_command.broadcast_text_m import BroadcastTextM
from .pest_command.get_data import GetData
from .pest_command.ignore import Ignore
from .pest_command.address_cast import AddressCast
from .pest_command.key_offer import KeyOffer
from .pest_command.key_slice import KeySlice
from .pest_command.message_exception import (
    MessageException,
    UNSUPPORTED_VERSION,
    UNSUPPORTED_COMMAND,
)
from .pest_command.message_exception import MALFORMED_PACKET, INVALID_SIGNATURE
from akris.c_serpent.serpent import decrypt

PACKET_SIZE = 496
MAX_SPEAKER_SIZE = 32
TS_ACCEPTABLE_SKEW = 60 * 15
BLACK_PACKET_FORMAT = "<448s48s"
RED_PACKET_FORMAT = "<16sBBxB428s"

MESSAGE_TYPES = {
    BROADCAST_TEXT: BroadcastText,
    BROADCAST_TEXT_M: BroadcastTextM,
    DIRECT_TEXT: DirectText,
    DIRECT_TEXT_M: DirectTextM,
    PROD: Prod,
    GET_DATA: GetData,
    KEY_OFFER: KeyOffer,
    KEY_SLICE: KeySlice,
    ADDRESS_CAST: AddressCast,
    IGNORE: Ignore,
}


class MessageFactory:
    def inflate(self, peer, black_packet, metadata):
        # unpack the black packet
        for key in peer.keys:
            key_bytes = base64.b64decode(key)
            signing_key = key_bytes[:32]
            cipher_key = key_bytes[32:]

            try:
                black_packet_bytes, signature_bytes = struct.unpack(
                    BLACK_PACKET_FORMAT, black_packet
                )
            except:
                logging.error(
                    "Discarding malformed black packet from %s" % peer.get_key()
                )
                raise MessageException(MALFORMED_PACKET, metadata)

            # check signature
            signature_check_bytes = hmac.new(
                signing_key, black_packet_bytes, hashlib.sha384
            ).digest()

            if signature_check_bytes != signature_bytes:
                continue

            # try to decrypt black packet
            red_packet_bytes = decrypt(cipher_key, black_packet_bytes)

        # unpack red packet
        try:
            nonce, bounces, version, command, message_bytes = struct.unpack(
                RED_PACKET_FORMAT, red_packet_bytes
            )

        # if red_packet_bytes was never set, no matching key for the sig was found
        # this is expected to happen often as only one peer's key should match for each
        # message we receive
        except NameError as ex:
            raise MessageException(INVALID_SIGNATURE, metadata)

        if version > EARLIEST_SUPPORTED_PEST_VERSION:
            raise MessageException(UNSUPPORTED_VERSION, metadata)

        try:
            return MESSAGE_TYPES[command]({"metadata": metadata}).inflate(
                {
                    "peer": peer,
                    "bounces": bounces,
                    "bytes": message_bytes,
                    "metadata": metadata,
                }
            )
        except KeyError as ke:
            raise MessageException(UNSUPPORTED_COMMAND, metadata)

    @staticmethod
    def reheat(message_record):
        return MESSAGE_TYPES[message_record.command]({}).reheat(message_record)
