from ..database import Database
class MessageStats:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
       direct_message_timestamps = {}
       handles = self.db.get_peer_handles()
       for handle in handles:
           direct_message_timestamps[handle] = self.db.get_latest_message_timestamp(handle)

       response = {
            "command": "console_response",
            "type": "message_stats",
            "latest_broadcast_message_timestamp": self.db.get_latest_message_timestamp(),
            "direct_message_timestamps": direct_message_timestamps,
        }
       return response
