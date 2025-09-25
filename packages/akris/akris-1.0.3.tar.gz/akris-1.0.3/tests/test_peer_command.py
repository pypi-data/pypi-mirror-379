import pytest
from helpers import (
    assert_error,
    await_messages,
    assert_no_errors,
    await_message_with_timeout,
)


@pytest.mark.usefixtures()
def test_peer_command(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["pizarro"]})
    await_message_with_timeout(cortes_client, "Peer added")


@pytest.mark.usefixtures()
def test_peer_exists(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    assert_no_errors(await_messages(1, cortes_client))
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    assert_error(await_messages(1, cortes_client))
