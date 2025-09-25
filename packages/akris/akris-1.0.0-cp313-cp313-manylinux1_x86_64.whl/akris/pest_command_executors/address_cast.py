from ..pest_command.prod import get_ascii_address, Prod, PROD_PROMPT
from ..log_config import LogConfig
from ..singleton_registry import SingletonRegistry

logger = LogConfig.get_instance().get_logger(
    "akris.pest_command_executors.address_cast"
)


class AddressCast:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.filter = SingletonRegistry.get_instance().get("Filter").get_instance()

    def execute(self, address_cast):
        self.filter.intern(address_cast)
        if address_cast.address:
            address_tuple = get_ascii_address(address_cast.address).split(":")
            handle_to_update = address_cast.origin_peer.handles[0]
            self.db.update_at(
                {
                    "handle": handle_to_update,
                    "address": address_tuple[0],
                    "port": int(address_tuple[1]),
                }
            )
            target_peer = self.db.get_peer_by_handle(handle_to_update)
            Prod({"speaker": self.db.get_knob("handle"), "flag": PROD_PROMPT}).send(
                target_peer
            )
        else:
            self.rebroadcast(address_cast)

    def rebroadcast(self, command):
        if command.bounces < int(self.db.get_knob("max_bounces")):
            command.bounces = command.bounces + 1
            command.forward()
        else:
            logger.debug("message TTL expired: %s" % command.message_hash)
