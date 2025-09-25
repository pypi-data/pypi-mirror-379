import json

from .console_command_executors.at import At
from .console_command_executors.broadcast_text import BroadcastText
from .console_command_executors.broadcast_text_m import BroadcastTextM
from .console_command_executors.direct_text import DirectText
from .console_command_executors.direct_text_m import DirectTextM
from .console_command_executors.genkey import Genkey
from .console_command_executors.handle import Handle
from .console_command_executors.help import Help
from .console_command_executors.key import Key
from .console_command_executors.knob import Knob
from .console_command_executors.message_stats import MessageStats
from .console_command_executors.page_around import PageAround
from .console_command_executors.page_down import PageDown
from .console_command_executors.page_up import PageUp
from .console_command_executors.peer import Peer
from .console_command_executors.report_presence import ReportPresence
from .console_command_executors.reset_database import ResetDatabase
from .console_command_executors.search import Search
from .console_command_executors.unpeer import Unpeer
from .console_command_executors.unkey import Unkey
from .console_command_executors.version_info import VersionInfo
from .console_command_executors.wot import Wot


class ConsoleDispatch:
    def __init__(self):
        self.executors = {
            "at": At(),
            "broadcast_text": BroadcastText(),
            "broadcast_text_m": BroadcastTextM(),
            "direct_text": DirectText(),
            "direct_text_m": DirectTextM(),
            "genkey": Genkey(),
            "handle": Handle(),
            "help": Help(),
            "key": Key(),
            "knob": Knob(),
            "message_stats": MessageStats(),
            "page_around": PageAround(),
            "page_down": PageDown(),
            "page_up": PageUp(),
            "peer": Peer(),
            "report_presence": ReportPresence(),
            "reset_database": ResetDatabase(),
            "search": Search(),
            "searchs": Search(),
            "unpeer": Unpeer(),
            "unkey": Unkey(),
            "version_info": VersionInfo(),
            "wot": Wot(),
        }

    def execute(self, command):
        try:
            return self.executors[command["command"]].execute(command["args"])
        except KeyError:
            return {
                "command": "console_response",
                "type": "error",
                "body": f"No command named {command['command']}",
            }
