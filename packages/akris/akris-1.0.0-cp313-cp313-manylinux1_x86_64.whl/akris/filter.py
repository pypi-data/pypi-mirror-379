import time

from .pest_command.broadcast_text_m import BroadcastTextM
from .pest_command.constants import *
from .pest_command.broadcast_text import BroadcastText
from .pest_command.direct_text import DirectText
from .database import Database
from .pest_command.direct_text_m import DirectTextM
from .pest_command.message import EMPTY_CHAIN
from .log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.filter")


class Filter(object):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.db = Database.get_instance()
        self.cache = self.load_cache()

    def persist_cache(self):
        self.db.persist_cache(self.cache)

    def load_cache(self):
        return self.db.load_cache()

    def exhume(self, message_hash):
        command, message_bytes = self.db.get_message(message_hash)
        if message_bytes:
            if command == DIRECT_TEXT:
                return DirectText({"message_bytes": message_bytes})
            if command == DIRECT_TEXT_M:
                return DirectTextM({"message_bytes": message_bytes})
            if command == BROADCAST_TEXT:
                return BroadcastText({"message_bytes": message_bytes})
            if command == BROADCAST_TEXT_M:
                return BroadcastTextM({"message_bytes": message_bytes})

    def intern(self, message):
        # somehow we are trying to intern a message we've already got
        if self.has(message.message_hash):
            return

        self.cache[message.message_hash] = {"timestamp": time.time(), "value": message}
        self.persist_cache()
        self.evict_expired()
        if message.command in [
            BROADCAST_TEXT,
            BROADCAST_TEXT_M,
            DIRECT_TEXT,
            DIRECT_TEXT_M,
        ]:
            self.db.log_message(message)

            # if the message is hearsay we must log the reporting peer
            if not message.check_immediate():
                own_handle = self.db.get_knob("handle")
                if message.speaker != own_handle:
                    self.db.log_reporting_peer(message.message_hash, message.peer.peer_id)

    def has(self, message_hash):
        if EMPTY_CHAIN == message_hash:
            return True

        if message_hash in self.cache:
            return True

        if self.db.log_has_message(message_hash):
            return True
        return False

    def cache_has(self, message_hash):
        return message_hash in self.cache

    def evict_expired(self):
        working_cache = self.cache.copy()
        for key in working_cache:
            if time.time() - working_cache.get(key)["timestamp"] > float(
                self.db.get_knob("filter.cache_expiration_seconds")
            ):
                self.cache.pop(key)
