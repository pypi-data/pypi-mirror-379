# coding=utf-8
import base64
import calendar
import json
import sqlite3
import uuid
import logging
import datetime
import time
import os
import importlib.resources
from hashlib import sha512
from itertools import chain

from . import caribou

from .sqlite3worker import Sqlite3Worker

from .config import Config
from .peer import Peer
from .pest_command.constants import (
    ADDRESS_CAST,
    BROADCAST_TEXT,
    BROADCAST_TEXT_M,
    DIRECT_TEXT,
    DIRECT_TEXT_M,
)
from .pest_command.message import EMPTY_CHAIN
from .version import VERSION
from .singleton import Singleton
from .log_config import LogConfig


logger = LogConfig.get_instance().get_logger("akris.database")


def fetchone(results):
    if len(results) > 0:
        return results[0]
    else:
        return None


def convert_to_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


KNOBS = {
    "api_service.process_outbound_queue": 0.1,
    "asked_for.get_data_tries": 2,
    "asked_for.get_data_wait": 2,
    "asked_for.get_data_window": 5,
    "asked_for.check_interval": 1,
    "pest_service.process_inbound_queue": 0.5,
    "pest_service.process_outbound_queue": 0.5,
    "max_bounces": 3,
    "ignore.interval_seconds": 10,
    "filter.cache_expiration_seconds": 3600,
    "asked_for.expiration_seconds": 120,
    "presence.peer_offline_interval_seconds": 120,
    "presence.report_interval": 0,
    "key_offer.interval_seconds": 0,
    "prod.interval_seconds": 60,
    "address_cast.interval_seconds": 0,
    "address_cast.port_hammering_enabled": 0,
    "cold_peer_seconds": 62,
    "banner": f"Akris {VERSION}",
    "prod.send_address_cast": "0",
    "handle": "anon",
    "testing.disable_broadcast": 0,
}


class MessageRecord:
    fields = ",".join(
        [
            "speaker",
            "immediate",
            "recipient_handle",
            "message_bytes",
            "message_hash",
            "command",
            "timestamp",
            "created_at",
            "get_data",
            "body",
            "base64_message_hash"
        ]
    )

    def __init__(self, record):
        (
            self.speaker,
            self.immediate,
            self.recipient_handle,
            self.message_bytes,
            self.message_hash,
            self.command,
            self.timestamp,
            self.created_at,
            self.get_data_response,
            self.body,
            self.base64_message_hash,
        ) = record


class Database(Singleton):
    def __init__(self, db_path=".", db_name="akris.db"):
        full_path = os.path.join(db_path, db_name)
        self.config = Config.get_instance()
        with importlib.resources.path("akris", "migrations") as migrations_path:
            caribou.upgrade(full_path, migrations_path)
        self.worker = Sqlite3Worker(full_path)

    def reset(self):
        table_names = [
            "handle_self_chain",
            "cache",
            "broadcast_self_chain",
            "at",
            "wot",
            "handles",
            "keys",
            "log",
            "asked_for",
            "knobs",
            "key_slices",
            "key_offers",
            "reporting_peers",
        ]
        for table_name in table_names:
            self.worker.execute(f"DELETE FROM {table_name};")

    def search(self, search_query, speaker=None):
        if speaker:
            sql_query = (
                "SELECT speaker, recipient_handle, highlight(log_index,1, '<<', '>>'), base64_message_hash FROM log_index "
                "WHERE body match ? and speaker = ? order by rank",
                (search_query, speaker),
            )
        else:
            sql_query = (
                "SELECT speaker, recipient_handle, highlight(log_index,1, '<<', '>>'), base64_message_hash FROM log_index "
                "WHERE body match ? order by rank",
                (search_query,),
            )
        return self.worker.execute(*sql_query)

    def set_last_external_address(self, address):
        self.worker.execute("DELETE FROM external_address;")
        self.worker.execute(
            "INSERT INTO external_address (address) VALUES (?)", (address,)
        )

    def get_last_external_address(self):
        result = fetchone(
            self.worker.execute("SELECT address FROM external_address LIMIT 1;")
        )
        if result:
            return result[0]
        else:
            return None

    def page_query(self, handle):
        if handle:
            own_handle = self.get_knob("handle")
            command_ids = ",".join(
                [str(command_id) for command_id in [DIRECT_TEXT, DIRECT_TEXT_M]]
            )
            query = (
                f"SELECT {MessageRecord.fields} FROM log WHERE ((speaker='{own_handle}' AND recipient_handle='{handle}')"
                f" OR (recipient_handle='{own_handle}' AND speaker='{handle}'))"
                f" AND command in ({command_ids})"
                " AND timestamp >= ? AND timestamp <= ? ORDER BY timestamp DESC"
            )
        else:
            command_ids = ",".join(
                [str(command_id) for command_id in [BROADCAST_TEXT, BROADCAST_TEXT_M]]
            )
            query = (
                f"SELECT {MessageRecord.fields} FROM log WHERE command in ({command_ids})"
                " AND timestamp >= ? AND timestamp <= ? ORDER BY timestamp ASC"
            )
        return query

    def get_latest_message_timestamp(self, handle=None):
        if handle:
            own_handle = self.get_knob("handle")
            command_ids = ",".join(
                [str(command_id) for command_id in [DIRECT_TEXT, DIRECT_TEXT_M]]
            )
            query = (
                f"SELECT MAX(timestamp) FROM log WHERE ((speaker='{own_handle}' AND recipient_handle='{handle}')"
                f" OR (recipient_handle='{own_handle}' AND speaker='{handle}'))"
                f" AND command in ({command_ids})"
            )
        else:
            command_ids = ",".join(
                [str(command_id) for command_id in [BROADCAST_TEXT, BROADCAST_TEXT_M]]
            )
            query = f"SELECT MAX(timestamp) FROM log WHERE command in ({command_ids})"
        results = fetchone(self.worker.execute(query))
        if results:
            return results[0]
        else:
            return None

    # this should really be called "get_window"
    def get_previous_page(self, timestamp, days_before, handle=None):
        start_date = datetime.datetime.fromtimestamp(timestamp) - datetime.timedelta(
            days=days_before
        )
        # Add ten minutes for to cactch messages from those with significant forward clock skew
        end_date = datetime.datetime.fromtimestamp(timestamp + 60 * 10)
        query = self.page_query(handle)
        return self.worker.execute(
            query,
            (
                start_date.timestamp(),
                end_date.timestamp(),
            ),
        )

    def get_next_page(self, timestamp, days_later, handle=None):
        start_date = datetime.datetime.fromtimestamp(timestamp)
        end_date = start_date + datetime.timedelta(days=1)

        query = self.page_query(handle)
        return self.worker.execute(
            query,
            (
                start_date.timestamp(),
                end_date.timestamp(),
            ),
        )

    def get_page_around(self, message_hash, handle=None):
        timestamp = fetchone(
            self.worker.execute(
                "select timestamp from log where message_hash = ?",
                (base64.b64decode(message_hash),),
            )
        )[0]
        start_date = datetime.datetime.fromtimestamp(timestamp) - datetime.timedelta(
            days=1
        )
        end_date = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(
            days=1
        )
        query = self.page_query(handle)
        return self.worker.execute(
            query,
            (
                start_date.timestamp(),
                end_date.timestamp(),
            ),
        )

    def persist_cache(self, cache):
        self.worker.execute("delete from cache")
        filtered_cache = {}
        for key, value in cache.items():
            if not value["value"]:
                filtered_cache[base64.b64encode(key).decode()] = {
                    "timestamp": value["timestamp"],
                    "value": None,
                }
            elif value["value"].command is ADDRESS_CAST:
                filtered_cache[base64.b64encode(key).decode()] = {
                    "timestamp": value["timestamp"],
                    "value": None,
                }

        self.worker.execute(
            "insert into cache(value) values(?);", (json.dumps(filtered_cache),)
        )

    def load_cache(self):
        decoded_cache = {}
        results = fetchone(self.worker.execute("select value from cache"))
        if results is not None:
            encoded_cache = json.loads(results[0])
            for key, value in encoded_cache.items():
                decoded_cache[base64.b64decode(key)] = value
            return decoded_cache
        else:
            return {}

    def clear_key_offer_and_slice(self, peer_id):
        self.worker.execute("delete from key_offers where peer_id=?", (peer_id,))
        self.worker.execute("delete from key_slices where peer_id=?", (peer_id,))

    def get_key_offer(self, peer_id):
        results = fetchone(
            self.worker.execute(
                "select slice from key_slices where peer_id=?", (peer_id,)
            )
        )
        if results is not None:
            return sha512(results[0]).digest()
        else:
            slice = os.urandom(64)
            self.worker.execute(
                "insert into key_slices(peer_id, slice) values(?, ?)", (peer_id, slice)
            )
            return sha512(slice).digest()

    def get_peer_key_offer(self, peer_id):
        results = fetchone(
            self.worker.execute(
                "select offer from key_offers where peer_id=?", (peer_id,)
            )
        )
        if results is not None:
            return results[0]
        else:
            return None

    def set_key_offer(self, peer_id, key_offer):
        self.worker.execute(
            "insert into key_offers(peer_id, offer) values(?, ?)", (peer_id, key_offer)
        )

    def get_key_slice(self, peer_id):
        results = fetchone(
            self.worker.execute(
                "select slice from key_slices where peer_id=?", (peer_id,)
            )
        )
        if results is not None:
            return results[0]
        else:
            return None

    def set_sent_peer_key_slice(self, peer_id):
        self.worker.execute("update key_slices set sent=1 where peer_id=?", (peer_id,))

    def sent_peer_key_slice(self, peer_id):
        results = fetchone(
            self.worker.execute(
                "select sent from key_slices where peer_id=?", (peer_id,)
            )
        )
        if results is not None:
            return results[0]
        else:
            return None

    def has_knob(self, knob):
        return knob in KNOBS

    def close(self):
        self.worker.close()

    def update_handle_self_chain(self, handle, message_hash):
        self.worker.execute(
            "insert into handle_self_chain(handle, message_hash) values(?, ?)",
            (handle, memoryview(message_hash)),
        )

    def get_handle_self_chain(self, handle):
        results = fetchone(
            self.worker.execute(
                "select message_hash from handle_self_chain where handle=?\
                                  order by id desc limit 1",
                (handle,),
            )
        )
        if results is not None:
            return results[0][:]
        else:
            return EMPTY_CHAIN

    def get_handle_net_chain(self, handle):
        command_ids = ",".join(
            [str(command_id) for command_id in [DIRECT_TEXT, DIRECT_TEXT_M]]
        )
        own_handle = self.get_knob("handle")
        results = fetchone(
            self.worker.execute(
                f"SELECT message_hash FROM log WHERE ((speaker=? AND recipient_handle=?)"
                f" OR (recipient_handle=? AND speaker=?))"
                f" AND command in ({command_ids})"
                f" ORDER BY timestamp desc LIMIT 1",
                (own_handle, handle, own_handle, handle),
            )
        )
        if results is not None:
            return results[0][:]
        else:
            return EMPTY_CHAIN

    def update_broadcast_self_chain(self, message_hash):
        self.worker.execute(
            "insert into broadcast_self_chain(message_hash) values(?)",
            (memoryview(message_hash),),
        )

    def get_broadcast_self_chain(self):
        results = fetchone(
            self.worker.execute(
                "select message_hash from broadcast_self_chain order by id desc limit 1"
            )
        )
        if results is not None:
            return results[0][:]
        else:
            return EMPTY_CHAIN

    def get_latest_broadcast_message_records(self):
        results = self.worker.execute(
            "select * from log where (command=? OR command=?) "
            "AND timestamp = (select max(timestamp) from log where command=? OR command=?)",
            (BROADCAST_TEXT, BROADCAST_TEXT_M, BROADCAST_TEXT, BROADCAST_TEXT_M),
        )
        return [MessageRecord(m) for m in results]

    def get_knobs(self):
        results = self.worker.execute("select name, value from knobs order by name asc")
        knobs = {}
        for result in results:
            knobs[result[0]] = result[1]
        for key in KNOBS.keys():
            if not knobs.get(key):
                knobs[key] = KNOBS[key]
        return knobs

    def get_knob(self, knob_name):
        result = fetchone(
            self.worker.execute("select value from knobs where name=?", (knob_name,))
        )
        if result:
            return convert_to_number(result[0])
        elif KNOBS.get(knob_name):
            return convert_to_number(KNOBS.get(knob_name))
        else:
            return None

    def set_knob(self, knob_name, knob_value):
        result = fetchone(
            self.worker.execute("select value from knobs where name=?", (knob_name,))
        )
        if result:
            self.worker.execute(
                "update knobs set value=? where name=?",
                (
                    knob_value,
                    knob_name,
                ),
            )
        else:
            self.worker.execute(
                "insert into knobs(name, value) values(?, ?)",
                (
                    knob_name,
                    knob_value,
                ),
            )

    def get_at(self, handle=None):
        at = []
        if handle == None:
            results = self.worker.execute(
                "select handle_id, address, port, updated_at, strftime('%s', updated_at) from at\
                                           order by updated_at desc"
            )
        else:
            result = fetchone(
                self.worker.execute(
                    "select handle_id from handles where handle=?", (handle,)
                )
            )
            if None != result:
                handle_id = result[0]
            else:
                return []
            results = self.worker.execute(
                "select handle_id, address, port, updated_at, strftime('%s', updated_at) from at \
                                           where handle_id=? order by updated_at desc",
                (handle_id,),
            )
        for result in results:
            handle_id, address, port, updated_at_utc, updated_at_unixtime = result
            h = fetchone(
                self.worker.execute(
                    "select handle from handles where handle_id=?", (handle_id,)
                )
            )[0]
            if updated_at_utc:
                if "." not in updated_at_utc:
                    updated_at_utc = updated_at_utc + ".0"
                dt_format = "%Y-%m-%d %H:%M:%S.%f"
                dt_utc = datetime.datetime.strptime(updated_at_utc, dt_format)
                dt_local = self.utc_to_local(dt_utc)
                updated_at = datetime.datetime.strftime(dt_local, dt_format)
            else:
                updated_at = "no packets received from this address"

            at.append(
                {
                    "handle": h,
                    "address": "%s:%s" % (address, port),
                    "active_at": updated_at,
                    "active_at_unixtime": int(updated_at_unixtime)
                    if updated_at_unixtime
                    else 0,
                }
            )
        return at

    def update_at(self, peer, set_active_at=True):
        row = self.worker.execute(
            "select handle_id from handles where handle=?", (peer["handle"],)
        )
        if row != None:
            handle_id = row[0][0]
        else:
            raise Exception("handle not found")

        at_entry = fetchone(
            self.worker.execute(
                "select handle_id, address, port from at where handle_id=?",
                (handle_id,),
            )
        )

        # if there are no AT entries for this handle, insert one
        timestamp = datetime.datetime.utcnow() if set_active_at else None
        if at_entry == None:
            self.worker.execute(
                "insert into at(handle_id, address, port, updated_at) values(?, ?, ?, ?)",
                (handle_id, peer["address"], peer["port"], timestamp),
            )
            logging.debug(
                "inserted new at entry for %s: %s:%d"
                % (peer["handle"], peer["address"], peer["port"])
            )

        # otherwise just update the existing entry
        else:
            try:
                self.worker.execute(
                    "update at set updated_at = ?,\
                address = ?,\
                port = ?\
                where handle_id=?",
                    (timestamp, peer["address"], peer["port"], handle_id),
                )

            except sqlite3.IntegrityError:
                self.worker.execute("delete from at where handle_id=?", (handle_id,))

    def add_peer(self, handle):
        peer_id = uuid.uuid4().hex
        self.worker.execute("insert into wot(peer_id) values(?)", (peer_id,))
        handle_id = uuid.uuid4().hex
        self.worker.execute(
            "insert into handles(handle_id, peer_id, handle) values(?, ?, ?)",
            (handle_id, peer_id, handle),
        )

    def remove_peer(self, handle):
        # get peer id
        result = fetchone(
            self.worker.execute("select peer_id from handles where handle=?", (handle,))
        )
        if result == None:
            raise Exception("handle not found")
        else:
            peer_id = result[0]
            # get all aliases

            handle_ids = self.get_handle_ids_for_peer(peer_id)
            for handle_id in handle_ids:
                # delete at entries for each alias
                self.worker.execute("delete from at where handle_id=?", (handle_id,))

            self.worker.execute("delete from handles where peer_id=?", (peer_id,))

            # delete all keys for peer id
            self.worker.execute("delete from keys where peer_id=?", (peer_id,))

            # delete peer from wot
            self.worker.execute("delete from wot where peer_id=?", (peer_id,))

    def add_key(self, handle, key):
        peer_id = fetchone(
            self.worker.execute("select peer_id from handles where handle=?", (handle,))
        )[0]
        if peer_id != None:
            self.worker.execute(
                "insert into keys(peer_id, key) values(?, ?)", (peer_id, key)
            )
            # let's send an address cast to let our new peer know where to find us
            self.set_knob("prod.send_address_cast", 1)

    def add_key_by_peer_id(self, peer_id, key):
        self.worker.execute(
            "insert into keys(peer_id, key) values(?, ?)", (peer_id, key)
        )

    def get_key(self, peer_id):
        return fetchone(
            self.worker.execute(
                "select key from keys where peer_id=? order by created_at desc limit 1",
                (peer_id,),
            )
        )[0]

    def key_exists(self, key):
        return (
            fetchone(self.worker.execute("select key from keys where key=?", (key,)))
            is not None
        )

    def remove_key(self, key):
        self.worker.execute("delete from keys where key=?", (key,))

    def get_handle_ids_for_peer(self, peer_id):
        return list(
            chain.from_iterable(
                self.worker.execute(
                    "select handle_id from handles where peer_id=?", (peer_id,)
                )
            )
        )

    def get_peer_handles(self):
        handles = self.listify(self.worker.execute("select handle from handles"))
        return handles

    def get_peers(self):
        peers = []
        handles = self.worker.execute("select handle from handles")

        for handle in handles:
            peer = self.get_peer_by_handle(handle[0])
            # leaving this check in here to help detect corrupt db
            peers.append(peer)
        return peers

    def listify(self, results):
        return list(chain.from_iterable(results))

    def wanted(self):
        get_data_tries = self.get_knob("asked_for.get_data_tries")
        get_data_window = self.get_knob("asked_for.get_data_window")
        wanted = self.listify(
            self.worker.execute(
                "select want_hash from asked_for where " "attempts < ? limit ?",
                (get_data_tries, get_data_window),
            )
        )
        return wanted

    def increment_attempts(self, want_hash):
        self.worker.execute(
            "update asked_for set attempts = attempts + 1 where want_hash=?",
            (want_hash,),
        )

    def get_attempts(self, want_hash):
        result = fetchone(
            self.worker.execute(
                "select attempts from asked_for where want_hash=?", (want_hash,)
            )
        )
        if result == None:
            return None
        else:
            return result[0]

    def get_requested_at(self, want_hash):
        result = fetchone(
            self.worker.execute(
                "select requested_at from asked_for where want_hash=?", (want_hash,)
            )
        )
        if result == None:
            return None
        else:
            return result[0]

    def update_requested_at(self, want_hash):
        self.worker.execute(
            "update asked_for set requested_at = ? where want_hash=?",
            (
                time.time(),
                want_hash,
            ),
        )

    def asked_for_expects(self, message_hash):
        result = fetchone(
            self.worker.execute(
                "select exists(select 1 from asked_for where want_hash=?)\
                                 limit 1",
                (message_hash,),
            )
        )
        return result[0]

    def add_asked_for(self, want_hash):
        self.worker.execute(
            "insert into asked_for(want_hash, requested_at) values(?, ?)",
            (want_hash, time.time()),
        )

    def unwant(self, want_hash):
        # check and make sure we have the want hash
        self.worker.execute("delete from asked_for where want_hash=?", (want_hash,))

    def log_has_message(self, message_hash):
        result = fetchone(
            self.worker.execute(
                "select exists(select 1 from log where message_hash=?)\
                                 limit 1",
                (message_hash,),
            )
        )
        return result[0]

    def log_message(self, message):
        self.worker.execute(
            "insert into log("
            "message_hash, speaker, immediate, recipient_handle, message_bytes, command, timestamp, get_data, body, base64_message_hash) "
            "values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                message.message_hash,
                message.speaker,
                message.check_immediate(),
                message.handle,
                message.message_bytes,
                message.command,
                message.timestamp,
                message.get_data_response,
                message.body,
                base64.b64encode(message.message_hash).decode("utf-8"),
            ),
        )

    def log_reporting_peer(self, message_hash, peer_id):
        self.worker.execute(
            "insert into reporting_peers(peer_id, message_hash) values(?, ?)",
            (peer_id, message_hash),
        )

    def get_reporting_peer_ids(self, message_hash):
        return self.listify(
            self.worker.execute(
                "select peer_id from reporting_peers where message_hash=?",
                (message_hash,),
            )
        )

    def get_reporting_peer_handles(self, message_hash):
        peer_ids = self.listify(
            self.worker.execute(
                "select peer_id from reporting_peers where message_hash=?",
                (message_hash,),
            )
        )
        handles = []
        for peer_id in peer_ids:
            result = fetchone(
                self.worker.execute(
                    "select handle from handles where peer_id=? limit 1",
                    (peer_id,),
                )
            )
            if result:
                handles.append(result[0])
        return handles

    def get_message(self, message_hash):
        result = fetchone(
            self.worker.execute(
                "select command, message_bytes from log where message_hash=? limit 1",
                (message_hash,),
            )
        )
        if result:
            return result[0], result[1][:]
        return None, None

    def get_keyed_peers(
        self, exclude_addressless=False, exclude_ids=[], no_at_only=False
    ):
        if len(list(exclude_ids)) == 0:
            query = "select distinct peer_id from keys order by random()"
        else:
            query = (
                "select distinct peer_id from keys where peer_id not in (%s) order by random()"
                % ",".join("?" * len(list(exclude_ids)))
            )

        peer_ids = self.listify(self.worker.execute(query, list(exclude_ids)))
        peers = []
        for peer_id in peer_ids:
            try:
                handle = fetchone(
                    self.worker.execute(
                        "select handle from handles where peer_id=?", (peer_id,)
                    )
                )[0]
                peer = self.get_peer_by_handle(handle)
                if exclude_addressless and (peer.address is None or peer.port is None):
                    continue
                if no_at_only and (peer.address is not None or peer.port is not None):
                    continue
                peers.append(peer)
            except:
                pass
        return peers

    def get_cold_peers(self):
        cold_peer_seconds = self.get_knob("cold_peer_seconds")
        all_peers = self.get_peers()
        cold_peers = []

        # peers with keys and no address
        for peer in all_peers:
            current_time = time.time()
            if peer.address is None and len(peer.keys) > 0:
                cold_peers.append(peer)
            elif peer.address and len(peer.keys) > 0:
                at = self.get_at(peer.handles[0])[0]
                if at["active_at_unixtime"] < (current_time - cold_peer_seconds):
                    cold_peers.append(peer)

        return cold_peers

    def handle_is_online(self, handle):
        # last rubbish message from peer associated with handle is
        # sufficiently recent
        try:
            at = self.get_at(handle)[0]
        except IndexError:
            return False

        if at["active_at_unixtime"] > time.time() - float(
            self.get_knob("presence.peer_offline_interval_seconds")
        ):
            return True
        else:
            return False

    def utc_to_local(self, utc_dt):
        # get integer timestamp to avoid precision lost
        timestamp = calendar.timegm(utc_dt.timetuple())
        local_dt = datetime.datetime.fromtimestamp(timestamp)
        assert utc_dt.resolution >= datetime.timedelta(microseconds=1)
        return local_dt.replace(microsecond=utc_dt.microsecond)

    def get_peer_by_handle(self, handle):
        handle_info = fetchone(
            self.worker.execute(
                "select handle_id, peer_id from handles where handle=?", (handle,)
            )
        )

        if handle_info == None:
            return None

        peer_id = handle_info[1]
        address = fetchone(
            self.worker.execute(
                "select address, port from at where handle_id=?\
                                       order by updated_at desc limit 1",
                (handle_info[0],),
            )
        )
        handles = self.listify(
            self.worker.execute(
                "select handle from handles where peer_id=?", (peer_id,)
            )
        )
        keys = self.listify(
            self.worker.execute(
                "select key from keys where peer_id=?\
                                                             order by random()",
                (peer_id,),
            )
        )
        return Peer(
            {
                "handles": handles,
                "peer_id": handle_info[1],
                "address": address[0] if address else None,
                "port": address[1] if address else None,
                "keys": keys,
            }
        )

    def address_exists(self, address):
        # break address into ip and port
        ip, port = address.split(":")
        result = fetchone(
            self.worker.execute(
                "select exists(select 1 from at where address=? and port=?)\
                                 limit 1",
                (ip, int(port)),
            )
        )
        # return true if address exists otherwise false
        return result[0]
