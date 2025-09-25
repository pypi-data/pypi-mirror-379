import pytest
from helpers import await_messages, assert_no_errors


@pytest.mark.usefixtures()
def test_fetch_handle(cortes_client):
    cortes_client.send_command({"command": "handle", "args": []})
    assert_no_errors(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_set_handle(cortes_client):
    cortes_client.send_command({"command": "handle", "args": ["pizarro"]})
    assert_no_errors(await_messages(1, cortes_client))
