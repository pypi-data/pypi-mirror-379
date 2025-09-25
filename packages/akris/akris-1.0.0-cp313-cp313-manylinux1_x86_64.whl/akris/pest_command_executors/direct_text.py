import base64

from ..api_service import ApiService
from .pest_command_executor import PestCommandExecutor
from ..database import Database
from ..filter import Filter


class DirectText(PestCommandExecutor):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()
        self.api_service = ApiService.get_instance()
        self.filter = Filter.get_instance()

    def execute(self, command):
        command.log_incoming(command.peer)
        self.deliver(command)
        self.conditionally_update_at(command, command.metadata["address"])

    # send to the client
    def deliver(self, command):
        self.api_service.enqueue_outbound(command.stringify())

        # store
        self.filter.intern(command)
