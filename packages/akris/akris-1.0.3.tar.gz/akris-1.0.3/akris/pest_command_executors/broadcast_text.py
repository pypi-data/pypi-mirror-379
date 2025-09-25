import base64
import logging

from ..database import Database
from ..filter import Filter
from ..api_service import ApiService
from ..singleton_registry import SingletonRegistry
from ..pest_command_executors.pest_command_executor import PestCommandExecutor


class BroadcastText(PestCommandExecutor):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()
        self.filter = Filter.get_instance()
        self.api_service = ApiService.get_instance()
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )

    def execute(self, command):
        command.log_incoming(command.peer)
        self.deliver(command)

        self.rebroadcast(command)
        self.conditionally_update_at(command, command.metadata["address"])

    def deliver(self, command):
        # send to the client
        self.api_service.enqueue_outbound(command.stringify())

        # store
        self.filter.intern(command)

    def rebroadcast(self, message):
        if not message.get_data_response:
            if message.bounces < int(self.db.get_knob("max_bounces")):
                message.bounces = message.bounces + 1
                message.forward()
            else:
                logging.debug("message TTL expired: %s" % message.message_hash)
