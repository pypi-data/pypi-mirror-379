from ..database import Database


class ReportPresence:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args=[]):
        response = []
        if len(args) > 0:
            response = {
                "command": "console_response",
                "type": "error",
                "body": "report_presence takes no arguments",
            }
            return response

        for handle in self.db.get_peer_handles():
            status = "online" if self.db.handle_is_online(handle) else "offline"
            response.append({
                "command": "presence",
                "handle": handle,
                "type": status,
            })

        return response