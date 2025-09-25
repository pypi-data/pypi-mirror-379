from .help import COMMANDS
from .page import Page
from ..net_chain import sort_by_chain


class PageAround(Page):
    def __init__(self):
        super().__init__()

    def execute(self, args):
        response = []
        if len(args) in (
                1,
                2,
        ):
            messages = self.db.get_page_around(*args)
            response = self.reheat_messages(messages)
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["page_around"]["help"],
            }
            return response

        if len(response) == 0:
            return []

        messages_sorted_by_timestamp_and_chain = sort_by_chain(response)
        self.annotate_page_response(messages_sorted_by_timestamp_and_chain, args[0])
        return messages_sorted_by_timestamp_and_chain

    def annotate_page_response(self, page, message_hash):
        page[0]["start"] = True
        page[-1]["end"] = True
        # mark each message as being a page response
        for message in page:
            message["ref_link_page_response"] = True
            message["ref_link_hash"] = message_hash

