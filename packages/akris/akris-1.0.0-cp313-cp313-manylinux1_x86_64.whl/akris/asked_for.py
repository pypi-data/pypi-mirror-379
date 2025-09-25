import time

from .pest_command.message import EMPTY_CHAIN
from .singleton_registry import SingletonRegistry
from .singleton import Singleton
from .pest_command.get_data import GetData

class AskedFor(Singleton):
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.attempts = {}
        self.requested_at = {}
        scheduler = SingletonRegistry.get_instance().get("Scheduler").get_instance()
        scheduler.register_task(self.retry_task, "asked_for.check_interval")

    def add(self, want_hash):
        self.attempts[want_hash] = 1
        if not self.db.asked_for_expects(want_hash):
            self.requested_at[want_hash] = time.time()
            self.db.add_asked_for(want_hash)

    def expects(self, want_hash):
        if EMPTY_CHAIN == want_hash:
            return True

        return self.db.asked_for_expects(want_hash)

    def unwant(self, want_hash):
        # remove the want_hash from the database
        self.db.unwant(want_hash)

    # Attempt to re-send any GetDatas that we have not received a response for
    def retry_task(self):
        for want_hash in self.db.wanted():
            if time.time() - self.db.get_requested_at(want_hash) < self.db.get_knob(
                "asked_for.get_data_wait"
            ):
                continue

            else:
                self.db.update_requested_at(want_hash)
                self.db.increment_attempts(want_hash)
                GetData(
                    {
                        "speaker": self.db.get_knob("handle"),
                        "body": want_hash,
                    }
                ).send()
