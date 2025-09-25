import json
from ..singleton_registry import SingletonRegistry
from ..filter import Filter


class GetData:
    def __init__(self):
        self.api_service = (
            SingletonRegistry.get_instance().get("ApiService").get_instance()
        )
        self.filter = Filter.get_instance()

    def execute(self, command):
        command.log_incoming_get_data(command.peer)

        # check for the requested message
        archived_message = self.filter.exhume(command.body)

        # resend it if it exists
        if archived_message:
            archived_message.retry(command.peer)
