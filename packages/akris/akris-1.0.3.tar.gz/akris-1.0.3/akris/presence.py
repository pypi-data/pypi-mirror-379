from .api_service import ApiService
from .database import Database


STATUS_OFFLINE = 0
STATUS_ONLINE = 1
STATUS_UNPEERED = 2

status_map = {
    STATUS_ONLINE: "online",
    STATUS_OFFLINE: "offline",
    STATUS_UNPEERED: "unpeered"
}

class Presence:
    def __init__(self):
        self.db = Database.get_instance()
        self.api_service = ApiService.get_instance()
        self.presence = {}

    def send_presence(self, handle, status):
        self.api_service.enqueue_outbound({
            "command": "presence",
            "type": status_map[status],
            "handle": handle,
        })

    def report_presence(self):
        # check for removed peers
        if len(self.presence) > len(self.db.get_peer_handles()):
            presence_copy = self.presence.copy()
            for handle in presence_copy:
                if handle not in self.db.get_peer_handles():
                    self.presence.pop(handle)
                    self.send_presence(handle, STATUS_UNPEERED)
        # if handle isn't in the presence dict, check if rubbish received and send online if so
        for handle in self.db.get_peer_handles():
            status = STATUS_ONLINE if self.db.handle_is_online(handle) else STATUS_OFFLINE
            if self.presence.get(handle) is None:
                self.presence[handle] = status
                self.send_presence(handle, status)
            else:
                if self.presence[handle] != status:
                    self.presence[handle] = status
                    self.send_presence(handle, status)
