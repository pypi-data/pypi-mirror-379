from ..database import Database
from ..version import VERSION
from ..pest_command.message import EARLIEST_SUPPORTED_PEST_VERSION, PEST_VERSION

class VersionInfo:
    def __init__(self):
        self.db = Database.get_instance()

    def execute(self, args):
        response = {
            "command": "console_response",
            "type": "version_info",
            "version": VERSION,
            "pest_version": PEST_VERSION,
            "earliest_supported_pest_version": EARLIEST_SUPPORTED_PEST_VERSION,
        }
        return response
