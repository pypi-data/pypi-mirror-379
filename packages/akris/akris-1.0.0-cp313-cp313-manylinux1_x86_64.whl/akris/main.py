#!/usr/bin/env python3

import os
import argparse
import logging

from akris.log_config import LogConfig

PEST_HOST = "127.0.0.1"
PEST_PORT = 8080
API_HOST = "127.0.0.1"
API_PORT = 8081
AKRIS_DATA_PATH = os.path.join(os.path.expanduser("~"), ".akris")
AKRIS_DATABASE_NAME = "akris.db"

logger = logging.getLogger("akris")
logger = LogConfig().get_logger("akris.main")
logging.basicConfig(level=logging.INFO)

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", action='store_true', default=False, help="continue running")
    parser.add_argument("--pest-host", default=PEST_HOST, help="pest station host")
    parser.add_argument("--api-host", default=API_HOST, help="api service host")
    parser.add_argument("--pest-port", default=PEST_PORT, help="pest station port")
    parser.add_argument("--api-port", default=API_PORT, help="api service port")
    parser.add_argument(
        "--akris-data-path",
        default=AKRIS_DATA_PATH,
        help="path at which to locate persistent Akris data",
    )
    parser.add_argument(
        "--akris-database-name",
        default=AKRIS_DATABASE_NAME,
        help="name to use for the Akris database file",
    )
    return parser.parse_args()


def main():
    options = get_options()
    LogConfig(data_path=options.akris_data_path).get_logger("akris.main")
    from akris.station import Station

    station = Station(
        tcp_host=options.api_host,
        tcp_port=int(options.api_port),
        udp_port=int(options.pest_port),
        host=options.pest_host,
        data_path=options.akris_data_path,
        database_name=options.akris_database_name,
    )
    station.start(return_from_start=not options.daemon)


if __name__ == "__main__":
    main()