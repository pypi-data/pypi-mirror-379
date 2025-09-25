import logging
import json
import socket
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import time

from .log_config import LogConfig
from .console_dispatch import ConsoleDispatch
from .json_stream_parser import load_iter
from .singleton_registry import SingletonRegistry
from .singleton import Singleton

logger = LogConfig.get_instance().get_logger("akris.api_service")

MAX_WORKERS = 10
HOST = "127.0.0.1"
PORT = 8080

def fix_phf_message(message):
    try:
        message["body"] = message["body"][4:]
        message["body"] = message["body"][:-38]
        message["body"] = message["body"].rstrip(b"\x00")
        message["body"] = message["body"].decode("utf-8")
        return message
    except UnicodeError:
        message["body"] = message["body"].decode("utf-8", errors="replace")
        return message


class ApiService(Singleton):
    def __init__(self, host, port):
        # set attributes from constructor arguments
        self.__dict__.update({k: v for k, v in locals().items() if k != "self"})

        self.socket = None
        self.tcp_connection = None
        self.tcp_executor = None
        self.outbound_queue = Queue()
        self.console_dispatch = ConsoleDispatch()
        self.stopped = False
        scheduler = SingletonRegistry.get_instance().get("Scheduler").get_instance()
        scheduler.register_task(
            self.process_outbound_queue, "api_service.process_outbound_queue"
        )

    def enqueue_outbound(self, message):
        try:
            json_message = json.dumps(message)
        except TypeError as e:
            fixed_message = fix_phf_message(message)
            json_message = json.dumps(fixed_message)
        encoded_json = json_message.encode("utf-8")
        self.outbound_queue.put(encoded_json)

    def handle_tcp_connection(self, conn, addr):
        with conn:
            logger.info(f"API client connected from {addr}")
            self.tcp_connection = conn
            sock_file = conn.makefile(mode="rw")
            for command in load_iter(sock_file):
                logger.info("api service received: {}".format(command))
                if command.get("command") == "shutdown":
                    logging.info("handle_tcp_connection received shutdown command")
                    self.enqueue_outbound(command)
                    # keep the connection open until self.stopped is set
                    while not self.stopped:
                        time.sleep(0.1)
                    break
                if command.get("command") == "disconnect":
                    logger.info("disconnecting API service\n")
                    self.enqueue_outbound({"command": "disconnect"})
                try:
                    response = self.console_dispatch.execute(command)

                    if type(response) == list:
                        for r in response:
                            self.enqueue_outbound(r)
                    else:
                        self.enqueue_outbound(response)
                except Exception as e:
                    logger.exception("error executing command")
                    error_response = {
                        "command": "console_response",
                        "type": "error",
                        "body": str(e),
                    }
                    self.enqueue_outbound(error_response)
            logger.info(f"client at {addr} disconnected")

    def api_service_thread(self):
        while not self.stopped:
            try:
                logger.info(
                    f"API service waiting for connections on {self.host}:{self.port}"
                )
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    sock.bind((self.host, self.port))
                    sock.listen()
                    sock.settimeout(1)
                    self.socket = sock

                    with ThreadPoolExecutor(
                        max_workers=MAX_WORKERS,
                        thread_name_prefix="handle_tcp_connection",
                    ) as executor:
                        while not self.stopped:
                            try:
                                conn, addr = sock.accept()
                                future = executor.submit(
                                    self.handle_tcp_connection, conn, addr
                                )
                                future.add_done_callback(self.handle_tcp_thread_done)
                            except TimeoutError:
                                pass
            except OSError:
                logger.exception(
                    f"API service failed to start on {self.host}:{self.port}"
                )
                time.sleep(1)

    def process_outbound_queue(self):
        while not self.stopped and not self.outbound_queue.empty():
            message = self.outbound_queue.get()
            try:
                logger.info("api service sending: {}".format(message))
                self.tcp_connection.sendall(message)
                self.tcp_connection.sendall(b"")
                if type(json.loads(message)) == dict:
                    if json.loads(message).get("command") == "shutdown":
                        logger.info("shutting down API service\n")
                        self.stop()
                        break
            except AttributeError:
                logger.info("client not connected")
            except OSError:
                logger.info("client disconnected")
                self.tcp_connection = None

    def ready(self):
        return self.socket is not None

    def start(self):
        executor = ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="api_service_thread"
        )
        future = executor.submit(self.api_service_thread)
        future.add_done_callback(self.handle_api_service_thread_done)

    def stop(self):
        self.stopped = True

    def handle_api_service_thread_done(self, future):
        logger.info("handle_api_service_thread_done exited")
        self.stop()
        ex = future.exception()
        if ex is not None:
            logger.exception(f"exception in api_service_thread: {ex}")

    def handle_tcp_thread_done(self, future):
        logger.info("handle_tcp_thread_done exited")
        ex = future.exception()
        if ex is not None:
            logger.exception(f"exception in handle_tcp_thread: {ex}")
