import pytest
from helpers import assert_error, assert_no_errors, await_messages, assert_no_errors


@pytest.mark.usefixtures()
def test_genkey_command(cortes_client):
    cortes_client.send_command({"command": "genkey", "args": []})
    assert_no_errors(await_messages(1, cortes_client))
