import time
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
def test_rekey(pizarro_client, atahualpa_client):
    setup_pizarro_station(pizarro_client)
    setup_atahualpa_station(atahualpa_client)

    # disable broadcast on pizarro
    pizarro_client.send_command(
        {"command": "knob", "args": ["key_offer.interval_seconds", 3600]}
    )
    assert_no_errors(await_messages(1, pizarro_client))
    time.sleep(5)
    pizarro_client.send_command({"command": "wot", "args": []})
    pizarro_wot = await_messages(1, pizarro_client)
    atahualpa_client.send_command({"command": "wot", "args": []})
    atahualpa_wot = await_messages(1, atahualpa_client)
    assert len(pizarro_wot[0]["body"][0]["keys"]) == 2
    assert len(atahualpa_wot[0]["body"][0]["keys"]) == 2
