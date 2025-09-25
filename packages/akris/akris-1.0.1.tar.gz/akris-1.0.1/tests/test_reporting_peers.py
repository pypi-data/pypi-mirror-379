import pytest
from helpers import (
    assert_no_errors,
    await_messages,
    await_message_with_timeout,
    await_message_update_with_timeout,
    PIZARRO_PEST_PORT,
    HOST,
    ATAHUALPA_PEST_PORT,
    CORTES_PEST_PORT,
    P_C_KEY,
    C_A_KEY,
    P_A_KEY,
)


def configure_pizarro(client):
    client.send_command({"command": "handle", "args": ["pizarro"]})
    client.send_command({"command": "peer", "args": ["cortes"]})
    client.send_command({"command": "key", "args": ["cortes", P_C_KEY]})
    client.send_command(
        {"command": "at", "args": ["cortes", "{}:{}".format(HOST, CORTES_PEST_PORT)]}
    )
    client.send_command({"command": "peer", "args": ["atahualpa"]})
    client.send_command({"command": "key", "args": ["atahualpa", P_A_KEY]})
    client.send_command(
        {"command": "at", "args": ["cortes", "{}:{}".format(HOST, ATAHUALPA_PEST_PORT)]}
    )
    assert_no_errors(await_messages(7, client))


def configure_cortes(client):
    client.send_command({"command": "handle", "args": ["cortes"]})
    client.send_command({"command": "peer", "args": ["pizarro"]})
    client.send_command({"command": "key", "args": ["pizarro", P_C_KEY]})
    client.send_command(
        {
            "command": "at",
            "args": ["pizarro", "{}:{}".format(HOST, PIZARRO_PEST_PORT)],
        }
    )
    client.send_command({"command": "peer", "args": ["atahualpa"]})
    client.send_command({"command": "key", "args": ["atahualpa", C_A_KEY]})
    client.send_command(
        {
            "command": "at",
            "args": ["atahualpa", "{}:{}".format(HOST, ATAHUALPA_PEST_PORT)],
        }
    )
    assert_no_errors(await_messages(7, client))

def configure_atahualpa(client):
    client.send_command({"command": "handle", "args": ["atahualpa"]})
    client.send_command({"command": "peer", "args": ["pizarro"]})
    client.send_command({"command": "key", "args": ["pizarro", P_C_KEY]})
    client.send_command(
        {
            "command": "at",
            "args": ["pizarro", "{}:{}".format(HOST, PIZARRO_PEST_PORT)],
        }
    )
    client.send_command({"command": "peer", "args": ["cortes"]})
    client.send_command({"command": "key", "args": ["cortes", C_A_KEY]})
    client.send_command(
        {
            "command": "at",
            "args": ["cortes", "{}:{}".format(HOST, CORTES_PEST_PORT)],
        }
    )
    assert_no_errors(await_messages(7, client))


@pytest.mark.usefixtures()
def test_broadcast_text(atahualpa_client, cortes_client, pizarro_client):
    configure_atahualpa(atahualpa_client)
    configure_pizarro(pizarro_client)
    configure_cortes(cortes_client)

    message_body = "conquisto"
    cortes_client.send_command({"command": "broadcast_text", "args": [message_body]})
    assert await_message_with_timeout(pizarro_client, message_body)
    update = await_message_update_with_timeout(pizarro_client, message_body)
    assert update.get("reporting_peer") == "cortes"
    assert await_message_with_timeout(cortes_client, message_body)
    assert await_message_with_timeout(atahualpa_client, message_body)
