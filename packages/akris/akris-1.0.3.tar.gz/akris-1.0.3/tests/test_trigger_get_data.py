import pytest
from helpers import (
    await_messages,
    assert_no_errors,
    await_message_with_timeout,
)
from helpers import (
    HOST,
    PIZARRO_PEST_PORT,
    CORTES_PEST_PORT,
    ATAHUALPA_PEST_PORT,
    P_A_KEY,
    C_A_KEY,
)


def setup_atahualpa_station(api_client):
    api_client.send_command({"command": "handle", "args": ["atahualpa"]})
    api_client.send_command({"command": "peer", "args": ["pizarro"]})
    api_client.send_command({"command": "key", "args": ["pizarro", P_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["pizarro", f"{HOST}:{PIZARRO_PEST_PORT}"]}
    )
    api_client.send_command({"command": "peer", "args": ["cortes"]})
    api_client.send_command({"command": "key", "args": ["cortes", C_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["cortes", f"{HOST}:{CORTES_PEST_PORT}"]}
    )

    # wait for the setup commands to be processed
    await_messages(7, api_client)


def setup_pizarro_station(api_client):
    api_client.send_command({"command": "handle", "args": ["pizarro"]})
    api_client.send_command({"command": "peer", "args": ["atahualpa"]})
    api_client.send_command({"command": "key", "args": ["atahualpa", P_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["atahualpa", f"{HOST}:{ATAHUALPA_PEST_PORT}"]}
    )
    await_messages(4, api_client)


def setup_cortes_station(api_client):
    api_client.send_command({"command": "handle", "args": ["cortes"]})
    api_client.send_command({"command": "peer", "args": ["atahualpa"]})
    api_client.send_command({"command": "key", "args": ["atahualpa", C_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["atahualpa", f"{HOST}:{ATAHUALPA_PEST_PORT}"]}
    )
    await_messages(3, api_client)


# sender: pizarro
# recipient: atahualpa
# 3rd party recipient: cortes
@pytest.mark.usefixtures()
def test_trigger_get_data(atahualpa_client, pizarro_client, cortes_client):
    setup_atahualpa_station(atahualpa_client)
    setup_pizarro_station(pizarro_client)
    setup_cortes_station(cortes_client)

    # create a broadcast message from pizarro to atahualpa
    m1 = "m1"
    pizarro_client.send_command({"command": "broadcast_text", "args": [m1]})
    assert await_message_with_timeout(pizarro_client, m1)

    # wait for the message to be delivered to atahualpa's client
    assert await_message_with_timeout(atahualpa_client, m1)

    # wait for the packet to be received by cortes
    assert await_message_with_timeout(cortes_client, m1)

    # disable broadcast on pizarro
    pizarro_client.send_command(
        {"command": "knob", "args": ["testing.disable_broadcast", 1]}
    )
    assert_no_errors(await_messages(1, pizarro_client))

    # "send" a second message from pizarro to atahualpa (atahualpa shouldn't receive it)
    m2 = "m2"
    pizarro_client.send_command({"command": "broadcast_text", "args": [m2]})
    assert await_message_with_timeout(pizarro_client, m2)

    # enable broadcast on pizarro
    pizarro_client.send_command(
        {"command": "knob", "args": ["testing.disable_broadcast", 0]}
    )
    assert_no_errors(await_messages(1, pizarro_client))

    # send a third message from pizarro to atahualpa
    m3 = "m3"
    pizarro_client.send_command({"command": "broadcast_text", "args": [m3]})
    assert await_message_with_timeout(pizarro_client, m3)

    # wait for the message to be delivered to atahualpa's client
    assert await_message_with_timeout(atahualpa_client, m3)

    # wait for the getdata response to be delivered to atahualpa's client
    assert await_message_with_timeout(atahualpa_client, m2)

    # wait for the rebroadcast to reach cortes
    assert await_message_with_timeout(cortes_client, m2)
