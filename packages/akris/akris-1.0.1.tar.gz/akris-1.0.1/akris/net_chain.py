import base64

from .message_factory import MessageFactory
from .database import Database
from .pest_command.message import EMPTY_CHAIN
from .singleton import Singleton


# sort results with identical timestamps by message hash
# this is kind of a heuristic because messages with identical timestamps are not
# guaranteed to be descendents or antecedents of one another
def sort_by_chain(messages):
    timestamp_groups = {}
    for query_result in messages:
        ts = query_result["timestamp"]
        added = False
        if timestamp_groups.get(ts, None) is None:
            timestamp_groups[ts] = [query_result]
        else:
            for message in timestamp_groups[ts]:
                # if query_result is a descendent of message
                if message["message_hash"] in [query_result["net_chain"], query_result["self_chain"]]:
                    timestamp_groups[ts].append(query_result)
                    added = True
                    break
                # query_result is an antecedent of message
                elif query_result["message_hash"] in [message["net_chain"], message["self_chain"]]:
                    timestamp_groups[ts].insert(timestamp_groups[ts].index(message), query_result)
                    added = True
                    break
            if not added:
                timestamp_groups[ts].append(query_result)

    # get the values of timestamp_groups as a list sorted by key (timestamp)
    messages_ordered_by_ts_and_chain = []
    ordered_ts_groups = [value for key, value in sorted(timestamp_groups.items())]
    for ts_group in ordered_ts_groups:
        messages_ordered_by_ts_and_chain += ts_group
    return messages_ordered_by_ts_and_chain


class NetChain(Singleton):
    def __init__(self):
        super().__init__()
        self.db = Database.get_instance()

    def get_broadcast_net_chain(self):
        latest_message_records = self.db.get_latest_broadcast_message_records()
        if len(latest_message_records) == 0:
            return EMPTY_CHAIN

        reheated_messages = [MessageFactory.reheat(mr) for mr in latest_message_records]
        stringified_reheated_messages = [m.stringify() for m in reheated_messages]
        sorted_messages = sort_by_chain(stringified_reheated_messages)
        return base64.b64decode(sorted_messages[-1]["message_hash"])

