from hashlib import sha512

from ..singleton_registry import SingletonRegistry
from ..pest_command.key_slice import KeySlice
from ..pest_command.key_offer import KeyOffer as KeyOfferCommand


class KeyOffer:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()

    def execute(self, key_offer):
        peer_id = key_offer.peer.peer_id
        # check for an existing key offer to this peer
        if self.db.get_key_slice(peer_id):
            # generate key slice
            key_slice = KeySlice({"peer": key_offer.peer})

            # ensure the hash of the key slice is not equal to the offer
            if sha512(key_slice.get_slice()) != key_offer.offer:
                # send our key slice
                self.db.set_sent_peer_key_slice(peer_id)
                key_slice.send()

        # if there is none respond with a KeyOffer of our own
        else:
            # record peer's offer and send our own
            KeyOfferCommand({"peer": key_offer.peer}).send()

        # we need to set the key offer from this peer whether we originated the first offer or not
        self.db.set_key_offer(peer_id, key_offer.offer)
