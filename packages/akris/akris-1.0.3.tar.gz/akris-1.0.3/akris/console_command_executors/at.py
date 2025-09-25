import ipaddress

from akris.database import Database
from akris.console_command_executors.help import COMMANDS


def sanitize(at):
    for peer in at:
        peer["handle"] = peer["handle"].decode()
    return at


def valid_address(address):
    try:
        ip, port = address.split(":")
        ipaddress.ip_address(ip)  # Validate the IP
        if not (0 <= int(port) <= 65535):  # Validate the port
            raise ValueError
    except ValueError:
        return False
    return True


class At:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        if len(args) == 0:
            response = {
                "command": "console_response",
                "type": "at",
                "body": self.db.get_at(),
            }
        elif len(args) == 1:
            handle = args[0]
            if handle not in self.db.get_peer_handles():
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": "No peer with handle: {}".format(handle),
                }
            else:
                response = {
                    "command": "console_response",
                    "type": "at",
                    "body": self.db.get_at(handle),
                }
        elif len(args) == 2:
            handle = args[0]
            if handle not in self.db.get_peer_handles():
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": "No peer with handle: {}".format(handle),
                }
            elif not valid_address(args[1]):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": "Invalid address",
                }
            elif self.db.address_exists(args[1]):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": "Duplicate address",
                }
            else:
                address_host, port = args[1].split(":")
                self.db.update_at(
                    {
                        "handle": handle,
                        "address": address_host,
                        "port": int(port),
                    }
                )
                response = {
                    "command": "console_response",
                    "type": "at",
                    "body": self.db.get_at(handle),
                }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["at"]["help"],
            }
        return response
