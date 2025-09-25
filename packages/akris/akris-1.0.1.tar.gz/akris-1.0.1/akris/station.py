import os
import time

from .asked_for import AskedFor
from .database import Database
from .api_service import ApiService
from .pest_service import PestService
from .config import Config
from .scheduler import Scheduler
from .singleton_registry import SingletonRegistry
from .pest_dispatch import PestDispatch
from .filter import Filter
from .net_chain import NetChain
from .pest_command.address_cast import AddressCast
from .pest_command.prod import Prod, PROD_PROMPT
from .pest_command.ignore import Ignore
from .pest_command.key_offer import KeyOffer
from .presence import Presence

HOST = "127.0.0.1"
TCP_PORT = 8080
UDP_PORT = 8081
DATA_PATH = os.path.join(os.path.expanduser("~"), ".akris")
DATABASE_NAME = "akris.db"

SINGLETON_CLASSES = [
    ApiService,
    AskedFor,
    Config,
    Database,
    Filter,
    NetChain,
    PestDispatch,
    PestService,
    Scheduler,
]


def register_singletons(cls):
    sr = SingletonRegistry.get_instance()
    for singleton_class in SINGLETON_CLASSES:
        sr.register(singleton_class)


def create_data_path(data_path):
    os.makedirs(data_path, exist_ok=True)


class Station:
    def __init__(
        self,
        tcp_host=HOST,
        host=HOST,
        tcp_port=TCP_PORT,
        udp_port=UDP_PORT,
        data_path=DATA_PATH,
        database_name=DATABASE_NAME,
    ):
        create_data_path(data_path)
        register_singletons(SINGLETON_CLASSES)
        self.config = Config.get_instance({})
        self.db = Database.get_instance(data_path, database_name)
        self.scheduler = Scheduler.get_instance()
        self.pest_service = None
        self.api_service = None
        self.presence = None

        # Task specific flags and variables
        self.sent_first_address_cast = False
        self.sent_address_cast_time = time.time()
        self.start_time = time.time()

        # set attributes from constructor arguments
        self.__dict__.update({k: v for k, v in locals().items() if k != "self"})

    def start(self, return_from_start=True):
        self.api_service = ApiService.get_instance(
            host=self.tcp_host, port=self.tcp_port
        )
        self.api_service.start()

        self.pest_service = PestService.get_instance(host=self.host, port=self.udp_port)
        self.pest_service.start()
        self.presence = Presence()

        self.scheduler.start()

        # schedule tasks that aren't in defined in long-running singletons
        self.scheduler.register_task(self.initiate_prod, "prod.interval_seconds")
        self.scheduler.register_task(
            self.initiate_key_offer, "key_offer.interval_seconds"
        )
        self.scheduler.register_task(
            self.initiate_address_cast, "address_cast.interval_seconds"
        )
        self.scheduler.register_task(self.send_ignore, "ignore.interval_seconds")
        self.scheduler.register_task(self.presence.report_presence, "presence.report_interval")

        if return_from_start:
            pass
        else:
            while not self.api_service.stopped:
                time.sleep(0.5)
            self.stop()

    def ready(self):
        return self.api_service.ready() and self.pest_service.ready()

    def stop(self):
        self.api_service.stop()
        self.pest_service.stop()
        self.scheduler.stop()
        self.db.close()

    def initiate_address_cast(self):
        if self.db.get_knob("address_cast.interval_seconds") == 0:
            return

        # send address cast on startup
        if not self.sent_first_address_cast:
            if time.time() > self.start_time + self.db.get_knob("cold_peer_seconds"):
                self.send_address_cast()

        # send address cast on address change
        else:
            if self.db.get_knob("prod.send_address_cast"):
                # (rate limited for those with flakey internet)
                if (
                    self.sent_address_cast_time
                    + self.db.get_knob("address_cast.interval_seconds")
                    < time.time()
                ):
                    self.sent_address_cast_time = time.time()
                    self.db.set_knob("prod.send_address_cast", 0)
                    self.send_address_cast()

    def initiate_key_offer(self):
        for peer in self.db.get_keyed_peers(exclude_addressless=True):
            KeyOffer({"peer": peer}).send()

    def initiate_prod(self):
        Prod({"speaker": self.db.get_knob("handle"), "flag": PROD_PROMPT}).broadcast()

    def send_address_cast(self):
        last_external_address = self.db.get_last_external_address()
        if last_external_address is not None:
            AddressCast(
                {
                    "speaker": self.db.get_knob("handle"),
                    "external_address": last_external_address,
                }
            ).broadcast()
            self.sent_first_address_cast = True
            self.db.set_knob("prod.send_address_cast", 0)

    def send_ignore(self):
        if self.db.get_knob("ignore.interval_seconds") == 0:
            return

        Ignore().send()

