import binascii
import queue
import socket
import time
from concurrent.futures import ThreadPoolExecutor
from .database import Database
from .exception_dispatch import ExceptionDispatch
from .message_factory import *
from .pest_command.message_exception import *
from .pest_dispatch import PestDispatch
from .singleton_registry import SingletonRegistry
from .singleton import Singleton
from .log_config import LogConfig

logger = LogConfig.get_instance().get_logger("akris.pest_service")
MAX_WORKERS = 10
HOST = "127.0.0.1"
PORT = 8081


class PestService(Singleton):
    def __init__(self, host, port):
        self.__dict__.update({k: v for k, v in locals().items() if k != "self"})
        self.stopped = None
        self.udp_executor = None
        self.udp_socket = None
        self.socket_bound = None
        self.db = Database.get_instance()
        self.inbound_queue = queue.Queue()
        self.outbound_queue = queue.Queue()
        scheduler = SingletonRegistry.get_instance().get("Scheduler").get_instance()
        scheduler.register_task(
            self.process_inbound_queue, "pest_service.process_inbound_queue"
        )
        scheduler.register_task(
            self.process_outbound_queue, "pest_service.process_outbound_queue"
        )

    def handle_udp_request(self, data, address):
        self.inbound_queue.put((data, address))

    def inflate_message(self, peer, data, metadata):
        try:
            return MessageFactory().inflate(
                peer,
                data,
                metadata,
            )
        except MessageException as me:
            return me

    def udp_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            self.udp_socket = s
            s.bind((self.host, self.port))
            self.socket_bound = True
            logger.info(f"UDP Server started on {self.host}:{self.port}")

            with ThreadPoolExecutor(
                max_workers=MAX_WORKERS, thread_name_prefix="handle_udp_request"
            ) as executor:
                while True:
                    try:
                        data, addr = s.recvfrom(1024)
                        if self.stopped:
                            break
                        future = executor.submit(self.handle_udp_request, data, addr)
                        future.add_done_callback(self.handle_udp_request_done)
                    except OSError:
                        logger.exception("error shutting down udp socket")
                        if self.stopped:
                            break
                        time.sleep(1)

    def enqueue_outbound_packet_to_address(self, packet_and_address_dict):
        self.outbound_queue.put(packet_and_address_dict)

    def process_inbound_queue(self):
        while not self.inbound_queue.empty():
            data, address = self.inbound_queue.get()
            try:
                packet_info = (address[0], address[1], binascii.hexlify(data)[0:16])

                metadata = {
                    "address": address,
                    "packet_info": packet_info,
                }

                # if we don't have any peers let's just stop here
                keyed_peers = self.db.get_keyed_peers()
                if len(keyed_peers) == 0:
                    return

                for peer in keyed_peers:
                    message = self.inflate_message(peer, data, metadata)
                    if message.error_code is INVALID_SIGNATURE:
                        continue

                    if message.error_code in [
                        None,
                        UNSUPPORTED_VERSION,
                        UNSUPPORTED_COMMAND,
                        STALE_PACKET,
                        OUT_OF_ORDER_BOTH,
                        OUT_OF_ORDER_SELF,
                        OUT_OF_ORDER_NET,
                        DUPLICATE_PACKET,
                        MALFORMED_PACKET,
                        INVALID_HANDLE_ENCODING,
                    ]:
                        break

                if message.error_code is None:
                    PestDispatch().execute(message)
                else:
                    # message is actually a MessageException here, which includes the original
                    # message + error code and metadata
                    ExceptionDispatch().handle(message)
            except Exception as e:
                logger.exception("error handling udp request")

    def process_outbound_queue(self):
        while not self.outbound_queue.empty():
            packet_and_address_dict = self.outbound_queue.get()
            try:
                self.udp_socket.sendto(
                    packet_and_address_dict["black_packet"],
                    packet_and_address_dict["address"],
                )
            except OSError:
                logger.exception("Network error while attempting to send UDP packet")
                time.sleep(0.5)

    def ready(self):
        return self.socket_bound is not None

    def start(self):
        self.udp_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="udp")
        future = self.udp_executor.submit(self.udp_server)
        future.add_done_callback(self.handle_udp_server_done)

    def stop(self):
        self.stopped = True
        self.send_final_udp_packet()
        self.udp_executor.shutdown(wait=False)

    def send_final_udp_packet(self):
        # Send final UDP packet to stop UDP server
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet
        sock.sendto(b"STOP", (self.host, self.port))

    def handle_udp_request_done(self, future):
        logger.debug("handle_udp_request exited")
        ex = future.exception()
        if ex is not None:
            logger.exception(f"*********** error handling udp request: {ex}")

    def handle_udp_server_done(self, future):
        logger.info("udp_server exited")
        ex = future.exception()
        if ex is not None:
            logger.exception(f"*********** error in udp_server: {ex}")
