import base64
import sys
from hashlib import sha512

from ..singleton_registry import SingletonRegistry
from ..log_config import LogConfig
from ..pest_command.key_slice import KeySlice as KeySliceCommand

logger = LogConfig.get_instance().get_logger("akris.pest_command_executors.key_slice")


def xor_byte_strings(byte_strings):
    # Start with a 512-bit integer of all zeros
    xor_result = 0

    # Perform XOR operation on each byte string
    for byte_string in byte_strings:
        # Convert byte string to 512-bit integer
        i = int.from_bytes(byte_string, "big")
        # Perform XOR operation
        xor_result ^= i

    # Convert result to 512-bit byte string
    xor_result_bytes = xor_result.to_bytes(64, "big")

    return xor_result_bytes


class KeySlice:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, key_slice):
        peer_id = key_slice.peer.peer_id
        # check hash of peer's key slice against peer key offer
        peer_key_offer = self.db.get_peer_key_offer(peer_id)

        if peer_key_offer == sha512(key_slice.slice).digest():
            # send our key slice if we haven't already
            if not self.db.sent_peer_key_slice(peer_id):
                self.db.set_sent_peer_key_slice(peer_id)
                KeySliceCommand({"peer": key_slice.peer}).send()

            # xor peer key, peer key slice, and our key slice and save as new peer key
            peer_key = base64.b64decode(self.db.get_key(peer_id))
            our_slice = self.db.get_key_slice(peer_id)
            peer_slice = key_slice.slice

            new_peer_key = xor_byte_strings([peer_key, our_slice, peer_slice])
            self.db.add_key_by_peer_id(
                peer_id, base64.b64encode(new_peer_key).decode("utf-8")
            )
        else:
            logger.error("KeySlice hash mismatch, ignoring")

        self.db.clear_key_offer_and_slice(peer_id)
