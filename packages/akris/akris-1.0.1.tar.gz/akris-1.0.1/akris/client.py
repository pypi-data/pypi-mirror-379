import logging
import json
import queue
import socket
from concurrent.futures import ThreadPoolExecutor

from .json_stream_parser import load_iter

HOST = "127.0.0.1"
PORT = 8080

logger = logging.getLogger("akris_client")


class Client:
    def __init__(self, host=HOST, port=PORT):
        self.executor = None
        self.host = host
        self.port = port
        self.socket = None
        self.sock_file = None
        self.message_queue = queue.Queue()
        self.connect()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.sock_file = self.socket.makefile(mode="rw")
        self.executor = ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="api_client"
        )
        self.executor.submit(self.listen)

    def listen(self):
        for message in load_iter(self.sock_file):
            if message["command"] == "shutdown":
                break
            if message["command"] == "disconnect":
                break
            logger.info(f"api client received: {message}")
            self.message_queue.put(message)
        self.close()

    def send_command(self, dict):
        logger.info(f"api client sending: {dict}")
        self.socket.sendall(json.dumps(dict).encode("utf-8", errors="replace"))

    def close(self):
        logger.info("disconnectiong from API service")
        self.executor.shutdown(wait=False)
        self.socket.close()

    def shutdown_station(self):
        logger.info("sending shutdown command to API service")
        self.socket.sendall(json.dumps({"command": "shutdown"}).encode("utf-8"))
        self.executor.shutdown(wait=False)
        self.socket.close()

    def disconnect(self):
        self.socket.sendall(json.dumps({"command": "disconnect"}).encode("utf-8"))
        self.close()
