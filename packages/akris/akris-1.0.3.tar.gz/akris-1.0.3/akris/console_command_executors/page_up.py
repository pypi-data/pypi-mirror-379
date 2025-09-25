from akris.console_command_executors.help import COMMANDS
from .page import Page
from ..net_chain import sort_by_chain


class PageUp(Page):
    def __init__(self):
        super().__init__()

    def execute(self, args):
        if len(args) in (
            2,
            3,
        ):
            messages = self.db.get_previous_page(*args)
            response = self.reheat_messages(messages)
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["page"]["help"],
            }
            return response

        if len(response) == 0:
            return []

        messages_sorted_by_timestamp_and_chain = sort_by_chain(response)
        self.annotate_page_response(messages_sorted_by_timestamp_and_chain)
        return messages_sorted_by_timestamp_and_chain
