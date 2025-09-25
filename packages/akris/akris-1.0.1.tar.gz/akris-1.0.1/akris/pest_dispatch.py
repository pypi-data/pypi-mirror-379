from .pest_command_executors.address_cast import AddressCast
from .pest_command_executors.broadcast_text import BroadcastText
from .pest_command_executors.broadcast_text_m import BroadcastTextM
from .pest_command_executors.direct_text import DirectText
from .pest_command_executors.direct_text_m import DirectTextM
from .pest_command_executors.get_data import GetData
from .pest_command_executors.key_offer import KeyOffer
from .pest_command_executors.key_slice import KeySlice
from .pest_command_executors.prod import Prod
from .pest_command_executors.ignore import Ignore
from .pest_command.constants import (
    ADDRESS_CAST,
    BROADCAST_TEXT,
    BROADCAST_TEXT_M,
    DIRECT_TEXT,
    DIRECT_TEXT_M,
    GET_DATA,
    IGNORE,
    KEY_OFFER,
    KEY_SLICE,
    PROD,
)
from .singleton import Singleton
from .log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_dispatch")


class PestDispatch(Singleton):
    def __init__(self):
        self.executors = {
            ADDRESS_CAST: AddressCast(),
            BROADCAST_TEXT: BroadcastText(),
            BROADCAST_TEXT_M: BroadcastTextM(),
            DIRECT_TEXT: DirectText(),
            DIRECT_TEXT_M: DirectTextM(),
            GET_DATA: GetData(),
            IGNORE: Ignore(),
            KEY_OFFER: KeyOffer(),
            KEY_SLICE: KeySlice(),
            PROD: Prod(),
        }

    def execute(self, message):
        try:
            # Nothing is done with the return value of pest command executors
            return self.executors[message.command].execute(message)
        except KeyError:
            logger.exception("error executing command")
