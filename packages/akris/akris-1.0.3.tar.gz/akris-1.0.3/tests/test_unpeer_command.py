import pytest
from helpers import assert_no_errors, await_messages, assert_error


@pytest.mark.usefixtures()
def test_unpeer_command(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    cortes_client.send_command(
        {"command": "at", "args": ["atahualpa", "122.122.0.1:8081"]}
    )
    cortes_client.send_command(
        {"command": "unpeer", "args": ["atahualpa"]}
    )
    assert_no_errors(await_messages(3, cortes_client))


@pytest.mark.usefixtures()
def test_unpeer_unknown_command(cortes_client):
    cortes_client.send_command({"command": "unpeer", "args": ["pizarro"]})
    assert_error(await_messages(1, cortes_client))
