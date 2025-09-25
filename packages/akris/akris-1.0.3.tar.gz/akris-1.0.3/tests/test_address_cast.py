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
    CORTES_PEST_PORT,
    P_A_KEY,
    P_C_KEY,
    C_A_KEY,
)


def setup_cortes_station(api_client):
    api_client.send_command({"command": "handle", "args": ["cortes"]})
    api_client.send_command({"command": "peer", "args": ["pizarro"]})
    api_client.send_command({"command": "key", "args": ["pizarro", P_C_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["pizarro", f"{HOST}:{PIZARRO_PEST_PORT}"]}
    )
    api_client.send_command({"command": "peer", "args": ["atahualpa"]})
    api_client.send_command({"command": "key", "args": ["atahualpa", C_A_KEY]})
    api_client.send_command(
        {"command": "at", "args": ["atahualpa", f"{HOST}:{ATAHUALPA_PEST_PORT}"]}
    )

    # wait for the setup commands to be processed
    await_messages(7, api_client)


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
    api_client.send_command({"command": "peer", "args": ["cortes"]})
    api_client.send_command({"command": "key", "args": ["cortes", P_C_KEY]})
    await_messages(6, api_client)


@pytest.mark.usefixtures()
def test_address_cast(pizarro_client, atahualpa_client, cortes_client):
    setup_cortes_station(cortes_client)
    setup_pizarro_station(pizarro_client)
    setup_atahualpa_station(atahualpa_client)

    # disable broadcast on pizarro
    pizarro_client.send_command(
        {"command": "knob", "args": ["address_cast.interval_seconds", 2]}
    )
    pizarro_client.send_command(
        {"command": "knob", "args": ["prod.interval_seconds", 2]}
    )
    pizarro_client.send_command({"command": "knob", "args": ["cold_peer_seconds", 5]})
    assert_no_errors(await_messages(3, pizarro_client))

    # wait for the address cast to be triggered and propagated
    time.sleep(7)
    pizarro_client.send_command({"command": "at", "args": ["cortes"]})
    pizarro_at = await_messages(1, pizarro_client)
    cortes_client.send_command({"command": "at", "args": ["pizarro"]})
    cortes_at = await_messages(1, cortes_client)
    assert pizarro_at[0]["body"][0]["address"] == f"{HOST}:{CORTES_PEST_PORT}"
    assert cortes_at[0]["body"][0]["address"] == f"{HOST}:{PIZARRO_PEST_PORT}"
