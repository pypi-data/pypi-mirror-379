import datetime
import time

from .message import Message
from .message_exception import MessageException, STALE_PACKET, DUPLICATE_PACKET, OUT_OF_ORDER_BOTH, OUT_OF_ORDER_SELF, \
    OUT_OF_ORDER_NET
from ..database import Database
from ..singleton_registry import SingletonRegistry
from ..log_config import LogConfig
from ..peer import Peer

logger = LogConfig.get_instance().get_logger("akris.pest_command.text_message")


class TextMessage(Message):
    def __init__(self, message):
        super().__init__(message)
        self.created_at = message.get("created_at")
        self.asked_for = SingletonRegistry.get_instance().get("AskedFor").get_instance()
        self.db = Database.get_instance()
        self.pest_service = (
            SingletonRegistry.get_instance().get("PestService").get_instance()
        )
        self.filter = SingletonRegistry.get_instance().get("Filter").get_instance()
        self.immediate = None

    def reheat(self, message):
        self.message_bytes = message.message_bytes
        self.message_hash = message.message_hash

        (_, self_chain, net_chain, _, body) = self._unpack_generic_message(
            self.message_bytes, unpad_body=True
        )

        recipient_handle = message.recipient_handle
        if recipient_handle == self.db.get_knob("handle"):
            self.peer = Peer({
                "handles": [self.db.get_knob("handle")],
            })
        else:
            self.peer = self.db.get_peer_by_handle(message.recipient_handle)
        self.body = body
        self.timestamp = message.timestamp
        self.created_at = message.created_at
        self.speaker = message.speaker
        self.self_chain = self_chain
        self.net_chain = net_chain
        self.immediate = message.immediate
        self.get_data_response = message.get_data_response

        return self

    def check_if_stale(self):
        # if we're expecting this message as a GETDATA response, skip the timestamp check
        if self.asked_for.expects(self.message_hash):
            self.asked_for.unwant(self.message_hash)
            # we need to mark this as a get data response in order not to rebroadcast it
            # TODO how to handle out of order unrequested but not stale messages subsequent to a message in AskedFor?
            self.get_data_response = True
        elif not self.in_time_window(self.timestamp):
                raise MessageException(STALE_PACKET, self.metadata, self)

    def check_if_duplicate(self):
        if self.filter.has(self.message_hash):
            raise MessageException(DUPLICATE_PACKET, self.metadata, self)

    def check_immediate(self):
        if self.speaker == self.db.get_knob("handle"):
            return False
        if self.peer.handle() == self.speaker:
            return True
        return False

    def check_order(self):
        if not self.filter.has(self.self_chain) and not self.filter.has(self.net_chain):
            # check if this is the first message on the net or an unsynced peer
            if self.self_chain != self.net_chain:
                raise MessageException(OUT_OF_ORDER_BOTH, self.metadata, self)
            else:
                raise MessageException(OUT_OF_ORDER_SELF, self.metadata, self)
        elif not self.filter.has(self.net_chain):
            raise MessageException(OUT_OF_ORDER_NET, self.metadata, self)
        elif not (self.filter.has(self.self_chain)):
            raise MessageException(OUT_OF_ORDER_SELF, self.metadata, self)

    def get_adjusted_timestamp(self):
        if self.get_data_response:
            return self.timestamp

        if not self.created_at:
            return self.timestamp

        created_at_datetime = datetime.datetime.strptime(self.created_at, "%Y-%m-%d %H:%M:%S")
        utc_dt = created_at_datetime.replace(tzinfo=datetime.timezone.utc)
        local_tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        system_dt = utc_dt.astimezone(local_tz)
        local_created_at_ts = int(time.mktime(system_dt.timetuple()))
        return local_created_at_ts

