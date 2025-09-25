import pytest
from helpers import assert_no_errors, await_messages, assert_error


@pytest.mark.usefixtures()
def test_version_info(cortes_client):
    cortes_client.send_command(
        {
            "command": "version_info",
            "args": [],
        }
    )
    assert_no_errors(await_messages(1, cortes_client))
