from .broadcast_text import BroadcastText


class BroadcastTextM(BroadcastText):
    def __init__(self):
        super().__init__()

    def deliver(self, command):
        # send to the client
        self.api_service.enqueue_outbound(command.stringify())

        # store
        self.filter.intern(command)
