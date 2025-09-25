from ..message_factory import MessageFactory
from ..database import Database, MessageRecord

class Page:
    def __init__(self):
        self.db = Database.get_instance()

    def annotate_page_response(self, page):
        page[0]["start"] = True
        page[-1]["end"] = True
        # mark each message as being a page response
        for message in page:
            message["page_response"] = True

    def reheat_messages(self, messages):
        reheated_messages = []
        for message in [MessageRecord(message) for message in messages]:
            reheated_message = MessageFactory.reheat(message)
            reheated_messages.append(reheated_message.stringify())
        return reheated_messages

