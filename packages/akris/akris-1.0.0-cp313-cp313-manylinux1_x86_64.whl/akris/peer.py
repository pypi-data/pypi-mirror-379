class Peer(object):
    def __init__(self, peer_entry):
        self.handles = peer_entry.get("handles")
        self.keys = peer_entry.get("keys")
        self.peer_id = peer_entry.get("peer_id")
        self.address = peer_entry.get("address")
        self.port = peer_entry.get("port")

    def get_key(self):
        if len(self.keys) > 0:
            return self.keys[0]
        else:
            return None

    def handle(self):
        if self.handles:
            if len(self.handles) > 0:
                return self.handles[0]
        return None

    def serialize(self):
        return {
            "handles": self.handles,
            "keys": self.keys,
            "peer_id": self.peer_id,
            "address": self.address,
            "port": self.port,
        }
