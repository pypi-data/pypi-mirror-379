STALE_PACKET = 0
DUPLICATE_PACKET = 1
MALFORMED_PACKET = 2
INVALID_SIGNATURE = 3
UNSUPPORTED_VERSION = 4
OUT_OF_ORDER_SELF = 5
OUT_OF_ORDER_NET = 6
OUT_OF_ORDER_BOTH = 7
INVALID_HANDLE_ENCODING = 8
UNSUPPORTED_COMMAND = 9


class MessageException(Exception):
    def __init__(self, error_code, metadata, object=None):
        super(MessageException, self).__init__("message exception")
        self.error_code = error_code
        self.metadata = metadata
        self.object = object
