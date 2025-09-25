import pytest
from helpers import assert_no_errors, await_messages, assert_error


@pytest.mark.usefixtures()
def test_wot(cortes_client):
    cortes_client.send_command(
        {
            "command": "peer",
            "args": ["pizarro"],
        }
    )
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "pizarro",
                "v4i+KHefkvTVUbeskTh4rGHiKSdDbCSnsSNKpvKHhCZT9yEzRkdVNjQP6KjDzeSM3d4M0RbwNezGcfAGcD5VtQ==",
            ],
        }
    )
    assert_no_errors(await_messages(2, cortes_client))
    cortes_client.send_command({"command": "wot", "args": []})
    assert_no_errors(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_wot_for_peer(cortes_client):
    cortes_client.send_command(
        {
            "command": "peer",
            "args": ["pizarro"],
        }
    )
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "pizarro",
                "v4i+KHefkvTVUbeskTh4rGHiKSdDbCSnsSNKpvKHhCZT9yEzRkdVNjQP6KjDzeSM3d4M0RbwNezGcfAGcD5VtQ==",
            ],
        }
    )
    assert_no_errors(await_messages(2, cortes_client))
    cortes_client.send_command({"command": "wot", "args": ["pizarro"]})
    assert_no_errors(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_no_such_peer(cortes_client):
    cortes_client.send_command({"command": "wot", "args": ["pizarro"]})
    assert_error(await_messages(1, cortes_client))
