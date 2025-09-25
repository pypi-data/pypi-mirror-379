import base64
import os


class Genkey:
    def __init__(self):
        pass

    def execute(self, args):
        response = {
            "command": "console_response",
            "type": "genkey",
            "body": base64.b64encode(os.urandom(64)).decode("utf-8"),
        }
        return response
