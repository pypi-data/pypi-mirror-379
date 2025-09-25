import base64
import struct

from .message import MAX_SPEAKER_SIZE, MAX_MESSAGE_LENGTH
from .text_message import TextMessage
from ..log_config import LogConfig
from ..peer import Peer
from ..singleton_registry import SingletonRegistry

logger = LogConfig.get_instance().get_logger("akris.pest_command.multipart_message")
MULTIPART_PACKET_FORMAT = "<q32s32s32s288sHH32s"


class MultipartMessage(TextMessage):
    def __init__(self, command):
        super().__init__(command)
        self.n = command.get("n")
        self.of = command.get("of")
        self.text_hash = command.get("text_hash")
        self.prev_message_hash = command.get("prev_message_hash")

    def reheat(self, command):
        self.message_bytes = command.message_bytes
        self.message_hash = command.message_hash

        (
            _,
            self_chain,
            net_chain,
            _,
            body,
            n,
            of,
            text_hash,
        ) = self._unpack_multipart_message(self.message_bytes, unpad_body=True)

        recipient_handle = command.recipient_handle
        if recipient_handle == self.db.get_knob("handle"):
            self.peer = Peer({
                "handles": [self.db.get_knob("handle")],
            })
        else:
            self.peer = self.db.get_peer_by_handle(command.recipient_handle)
        self.body = body
        self.timestamp = command.timestamp
        self.speaker = command.speaker
        self.self_chain = self_chain
        self.net_chain = net_chain
        self.n = n
        self.of = of
        self.text_hash = text_hash
        self.immediate = command.immediate
        self.get_data_response = command.get_data_response

        return self

    def inflate(self, command):
        self.message_bytes = command.get("bytes")
        self.message_hash = self.gen_hash(self.message_bytes)

        (
            int_ts,
            self_chain,
            net_chain,
            speaker,
            body,
            n,
            of,
            text_hash,
        ) = self._unpack_multipart_message(self.message_bytes, unpad_body=True)

        self.peer = command.get("peer")
        self.handle = self.db.get_knob('handle')
        self.body = body
        self.timestamp = int_ts
        self.speaker = speaker
        self.self_chain = self_chain
        self.net_chain = net_chain
        self.n = n
        self.of = of
        self.text_hash = text_hash
        self.metadata = command.get("metadata")

        self.check_if_stale()
        self.check_if_duplicate()

    def _unpack_multipart_message(self, message_bytes, unpad_body=False):
        int_ts, self_chain, net_chain, speaker, body, n, of, text_hash = struct.unpack(
            MULTIPART_PACKET_FORMAT, message_bytes
        )
        self.assert_ascii(speaker)
        speaker = speaker.rstrip(b"\x00")
        speaker = speaker.decode("ascii")

        if unpad_body:
            body = self._unpad(body, "utf-8")

        return int_ts, self_chain, net_chain, speaker, body, n, of, text_hash

    def get_message_bytes(self, peer=None):
        speaker = self._pad(self.speaker, MAX_SPEAKER_SIZE)

        if peer is not None:
            if self.n == 1:
                self.self_chain = self.db.get_handle_self_chain(peer.handles[0])
                self.net_chain = self.db.get_handle_net_chain(peer.handles[0])
            else:
                # self_chain must be equal to the message hash of the previous chunk
                self.self_chain = self.prev_message_hash

                # net_chain must be equal to self chain
                self.net_chain = self.self_chain
        else:
            self.self_chain = self.db.get_broadcast_self_chain()
            nc = SingletonRegistry.get_instance().get("NetChain").get_instance()
            if self.n == 1:
                self.net_chain = nc.get_broadcast_net_chain()
            else:
                # self_chain must be equal to the message hash of the previous chunk
                self.self_chain = self.prev_message_hash

                # net_chain must be equal to self chain
                self.net_chain = self.self_chain

        body = self.body.encode("utf-8", errors="replace")

        message_bytes = struct.pack(
            MULTIPART_PACKET_FORMAT,
            self.timestamp,
            self.self_chain,
            self.net_chain,
            speaker,
            body,
            self.n,
            self.of,
            self.text_hash,
        )
        assert len(message_bytes) == MAX_MESSAGE_LENGTH
        return message_bytes
