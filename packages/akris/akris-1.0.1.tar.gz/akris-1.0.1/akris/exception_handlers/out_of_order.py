import binascii
import logging

from ..pest_command.get_data import GetData
from ..pest_command.message_exception import (
    OUT_OF_ORDER_SELF,
    OUT_OF_ORDER_NET,
    OUT_OF_ORDER_BOTH,
)
from ..singleton_registry import SingletonRegistry
from ..pest_dispatch import PestDispatch
from ..log_config import LogConfig

logger = LogConfig.get_instance().get_logger(
    "akris.pest_command_executors.out_of_order"
)


class OutOfOrder:
    def __init__(self):
        self.db = SingletonRegistry.get_instance().get("Database").get_instance()
        self.asked_for = SingletonRegistry.get_instance().get("AskedFor").get_instance()
        self.pest_dispatch = PestDispatch()

    def handle(self, exception):
        if exception.error_code == OUT_OF_ORDER_SELF:
            self.add_message_to_asked_for_and_send_get_data(exception, ["self_chain"])
        elif exception.error_code == OUT_OF_ORDER_NET:
            self.add_message_to_asked_for_and_send_get_data(exception, ["net_chain"])
        elif exception.error_code == OUT_OF_ORDER_BOTH:
            self.add_message_to_asked_for_and_send_get_data(
                exception, ["self_chain", "net_chain"]
            )
        else:
            raise Exception("Unexpected error code")

    def add_message_to_asked_for_and_send_get_data(self, exception, broken_chains):
        message = exception.object
        packet_info = exception.metadata["packet_info"]
        address = packet_info[0]
        port = packet_info[1]
        logger.debug(
            "[%s:%d] -> message received out of order: %s"
            % (address, port, binascii.hexlify(message.message_hash))
        )
        for chain in broken_chains:
            want_hash = getattr(message, chain)
            if not self.asked_for.expects(want_hash):
                self.asked_for.add(want_hash)
        # handle the message as usual from here on
        self.pest_dispatch.execute(message)
