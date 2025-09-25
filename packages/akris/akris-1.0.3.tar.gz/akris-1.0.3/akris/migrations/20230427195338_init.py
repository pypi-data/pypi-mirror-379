"""
This module contains a Caribou migration.

Migration Name: init 
Migration Version: 20230427195338
"""


def upgrade(connection):
    connection.execute("create table if not exists external_address(address blob not null)")

    connection.execute("create table if not exists cache(value text not null)")

    connection.execute(
        "create table if not exists key_offers(id integer primary key autoincrement,\
        peer_id text not null,\
        offer blob not null,\
        unique(peer_id))"
    )

    connection.execute(
        "create table if not exists key_slices(id integer primary key autoincrement,\
        peer_id text not null,\
        slice blob not null,\
        sent boolean default false,\
        unique(peer_id))"
    )

    connection.execute(
        "create table if not exists handle_self_chain(id integer primary key autoincrement,\
                                                                     handle string not null,\
                                                                     message_hash blob not null)"
    )

    connection.execute(
        "create table if not exists broadcast_self_chain(id integer primary key autoincrement,\
                                                                        message_hash blob not null)"
    )

    connection.execute(
        "create table if not exists net_chain(id integer primary key autoincrement,\
                                                             message_hash blob not null)"
    )

    connection.execute(
        "create table if not exists at(handle_id text,\
                                                      address text not null,\
                                                      port    integer not null,\
                                                      updated_at datetime default null,\
                                                      unique(address, port))"
    )

    connection.execute("create table if not exists wot(peer_id text primary key)")

    connection.execute(
        "create table if not exists handles(handle_id text primary key,\
                                                           peer_id text,\
                                                           handle text,\
                                                           unique(handle))"
    )

    connection.execute(
        "create table if not exists keys(peer_id text,\
                                                        key text,\
                                                        created_at datetime default current_timestamp,\
                                                        unique(key))"
    )

    connection.execute(
        "create table if not exists log(\
              speaker text not null,\
              immediate boolean default false,\
              recipient_handle text,\
              message_bytes blob not null,\
              message_hash text not null, \
              command integer not null, \
              timestamp datetime not null, \
              created_at datetime default current_timestamp, \
              get_data boolean default false, \
              body text not null, \
              base64_message_hash text not null, \
              unique(message_hash))"
    )

    connection.execute(
        "create virtual table log_index using fts5("
        "speaker,"
        "body,"
        "recipient_handle,"
        "base64_message_hash)"
    )

    connection.execute(
        "CREATE TRIGGER log_ai AFTER INSERT ON log BEGIN "
        "INSERT INTO log_index(speaker, recipient_handle, body, base64_message_hash) "
        "VALUES (new.speaker, new.recipient_handle, new.body, new.base64_message_hash);"
        "END;"
    )


    connection.execute(
        "create table if not exists reporting_peers (\
        message_hash text not null, \
        peer_id text not null, \
        unique(message_hash, peer_id))"
    )

    connection.execute("create index speaker_index on log(speaker)")

    connection.execute("create index timestamp_index on log(timestamp)")

    connection.execute(
        "create index speaker_timestamp_index on log(speaker, timestamp)"
    )

    connection.execute(
        "create table if not exists asked_for(want_hash text not null, \
         attempts int default 0, \
         requested_at int not null, \
         unique(want_hash))"
    )

    connection.execute(
        "create table if not exists knobs(\
                         name text not null,\
                         value text not null)"
    )


def downgrade(connection):
    connection.execute("drop table handle_self_chain")
    connection.execute("drop table broadcast_self_chain")
    connection.execute("drop table at")
    connection.execute("drop table wot")
    connection.execute("drop table handles")
    connection.execute("drop table keys")
    connection.execute("drop table log")
    connection.execute("drop table knobs")
