COMMANDS = {
    "at": {
        "help": "at [handle] [address:port] - Get or set the address of a peer",
    },
    "genkey": {"help": "genkey - Randomly generate a symmetric key"},
    "handle": {"help": "handle [handle] - Get or set the station handle"},
    "help": {"help": "help [command] - Get help for a command"},
    "key": {"help": "key <handle> [key] - Get or set the key for a peer"},
    "knob": {
        "help": "knob [name] [value] - Get or set a knob. Omit all arguments to list knobs"
    },
    "page_around": {
        "help": "page_around <message_hash> [handle] - Get all messages from the day that includes <message_hash>"
        "All returned messages include a ref_link_hash field to be used to group the responses."
    },
    "page_down": {
        "help": "page_down <start_timestamp> <days_later> [handle] - Get page starting at <start_timestamp> until"
                " <days_later> from peer with [handle]"
                " If [handle] is specified direct messages to and from the peer specified by"
                " [handle] will be returned. Otherwise, broadcast messages will be returned."
                "  Messages are ordered by timestamp and chain, with the earliest messages first."
    },
    "page_up": {
        "help": "page_up <start_timestamp> <days_before> [handle] - Get page starting at <start_timestamp> until"
                " <days_before> from peer with [handle]"
                " If [handle] is specified direct messages from the peer specified by"
                " [handle] will be returned. Otherwise, broadcast messages will be returned."
                "  Messages are ordered by timestamp and chain, with the earliest messages first."
    },
    "peer": {
        "help": "peer <handle> - Add a peer",
    },
    "search": {
        "help": "search <search_string> - Search for messages containing <search_string>"
    },
    "searchs": {
        "help": "searchs <speaker> <search_string> - Search for messages from <speaker> containing <search_string>"
    },
    "unkey": {"help": "unkey [key] - Delete a key"},
    "unpeer": {
        "help": "unpeer <handle> - Remove a peer",
    },
    "version_info": {"help": "version_info - Get version information"},
    "wot": {
        "help": "wot [handle] - Get the latest address for all peers, or the keys for a specific peer",
    },
}


class Help:
    def __init__(self):
        pass

    def execute(self, args):
        if len(args) == 0:
            response = {
                "command": "console_response",
                "type": "help",
                "body": COMMANDS,
            }
        elif len(args) == 1:
            if not COMMANDS.get(args[0]):
                response = {
                    "command": "console_response",
                    "type": "error",
                    "body": f"No command named {args[0]}",
                }
            else:
                response = {
                    "command": "console_response",
                    "type": "help",
                    "body": {args[0]: COMMANDS[args[0]]},
                }
        else:
            response = {
                "command": "console_response",
                "type": "error",
                "body": COMMANDS["help"]["help"],
            }
        return response
