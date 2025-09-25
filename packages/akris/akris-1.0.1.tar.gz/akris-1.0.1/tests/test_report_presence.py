import pytest

from helpers import (
    await_messages,
    assert_no_errors,
    assert_error,
)


@pytest.mark.usefixtures()
def test_at_command(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    cortes_client.send_command(
        {"command": "at", "args": ["atahualpa", "122.122.0.1:8081"]}
    )
    assert_no_errors(await_messages(2, cortes_client))
    cortes_client.send_command({"command": "report_presence", "args": []})
    assert_no_errors(await_messages(1, cortes_client))