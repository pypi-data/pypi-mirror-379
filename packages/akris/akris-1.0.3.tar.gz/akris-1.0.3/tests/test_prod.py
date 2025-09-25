import pytest
from helpers import (
    await_messages,
    assert_no_errors,
    await_message_with_timeout,
)
from helpers import (
    HOST,
    PIZARRO_PEST_PORT,
    ATAHUALPA_PEST_PORT,
    P_A_KEY,
)


def setup_atahualpa_station(api_client):
    api_client.send_command({"command": "handle", "args": ["atahualpa"]})
    api_client.send_command({"command": "peer", "args": ["pizarro"]})
    api_client.send_command({"command": "key", "args": ["pizarro", P_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["pizarro", f"{HOST}:{PIZARRO_PEST_PORT}"]}
    )

    # wait for the setup commands to be processed
    await_messages(4, api_client)


def setup_pizarro_station(api_client):
    api_client.send_command({"command": "handle", "args": ["pizarro"]})
    api_client.send_command({"command": "peer", "args": ["atahualpa"]})
    api_client.send_command({"command": "key", "args": ["atahualpa", P_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["atahualpa", f"{HOST}:{ATAHUALPA_PEST_PORT}"]}
    )
    await_messages(4, api_client)


@pytest.mark.usefixtures()
def test_prod(pizarro_client, atahualpa_client):
    setup_pizarro_station(pizarro_client)
    setup_atahualpa_station(atahualpa_client)

    # disable broadcast on pizarro
    pizarro_client.send_command(
        {"command": "knob", "args": ["testing.disable_broadcast", 1]}
    )
    assert_no_errors(await_messages(1, pizarro_client))

    # create a broadcast message from pizarro to atahualpa
    m1 = "m1"
    pizarro_client.send_command({"command": "broadcast_text", "args": [m1]})
    assert await_message_with_timeout(pizarro_client, m1)

    # enable broadcast on pizarro
    pizarro_client.send_command(
        {"command": "knob", "args": ["testing.disable_broadcast", 0]}
    )
    assert_no_errors(await_messages(1, pizarro_client))

    # enable prod on atahualpa
    atahualpa_client.send_command(
        {"command": "knob", "args": ["prod.interval_seconds", 2]}
    )
    assert_no_errors(await_messages(1, atahualpa_client))

    # await the broadcast message from pizarro to atahualpa via getdata via prod
    assert await_message_with_timeout(atahualpa_client, m1)
