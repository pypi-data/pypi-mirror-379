from .pest_command_executor import PestCommandExecutor
from ..log_config import LogConfig
from ..database import Database

logger = LogConfig.get_instance().get_logger("akris.pest_command_executors.ignore")


class Ignore(PestCommandExecutor):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()

    def execute(self, message):
        self.conditionally_update_at(message, message.metadata["address"])
        packet_info = message.metadata["packet_info"]
        address = packet_info[0]
        port = packet_info[1]
        packet_sample = packet_info[2]
        logger.debug("[%s:%d] -> ignoring packet: %s" % (address, port, packet_sample))
