class PestCommandExecutor:
    def __init__(self):
        pass

    # we only update the address table if the speaker is same as peer
    def conditionally_update_at(self, command, address):
        address = command.metadata["address"]
        if command.speaker in command.peer.handles:
            self.db.update_at(
                {"handle": command.speaker, "address": address[0], "port": address[1]}
            )
