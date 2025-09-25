from ..singleton_registry import SingletonRegistry
from .pest_command_executor import PestCommandExecutor
from ..pest_command.get_data import GetData
from ..pest_command.prod import Prod as ProdCommand, PROD_REPLY, PROD_PROMPT


class Prod(PestCommandExecutor):
    def __init__(self):
        super().__init__()
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.filter = SingletonRegistry.get_instance().get("Filter").get_instance()
        self.asked_for = SingletonRegistry.get_instance().get("AskedFor").get_instance()

    def execute(self, prod):
        self.conditionally_update_at(prod, prod.metadata.get("address"))

        # we need to "refresh" the peer in case the peer for this
        # prod doesn't have an address set yet
        prod.peer = self.db.get_peer_by_handle(prod.peer.handles[0])
        prod.log_incoming(prod.peer)

        # reply to prod if necessary
        if prod.flag == PROD_PROMPT:
            ProdCommand(
                {
                    "speaker": self.db.get_knob("handle"),
                    "flag": PROD_REPLY,
                    "prompt": prod,
                }
            ).reply()

        # if our external address has changed, broadcast an address cast
        last_external_address = self.db.get_last_external_address()
        if last_external_address is not None:
            if last_external_address != prod.pest_address:
                self.db.set_knob("prod.send_address_cast", 1)

        # update last_external_address for future Address Cast messages
        self.db.set_last_external_address(prod.pest_address)

        # request missing chain tips
        for chain in ["broadcast_self_chain", "handle_self_chain", "net_chain"]:
            want_hash = getattr(prod, chain)
            if not self.filter.has(want_hash):
                if not self.asked_for.expects(want_hash):
                    self.asked_for.add(want_hash)
                    GetData(
                        {"speaker": self.db.get_knob("handle"), "body": want_hash}
                    ).send()
