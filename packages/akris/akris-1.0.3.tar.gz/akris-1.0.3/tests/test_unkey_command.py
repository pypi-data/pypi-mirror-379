import pytest
from helpers import assert_no_errors, await_messages, assert_error


@pytest.mark.usefixtures()
def test_unkey(cortes_client):
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
    cortes_client.send_command(
        {
            "command": "unkey",
            "args": [
                "v4i+KHefkvTVUbeskTh4rGHiKSdDbCSnsSNKpvKHhCZT9yEzRkdVNjQP6KjDzeSM3d4M0RbwNezGcfAGcD5VtQ=="
            ],
        }
    )
    assert_no_errors(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_key_not_found(cortes_client):
    cortes_client.send_command({"command": "unkey", "args": ["foobar"]})
    assert_error(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_no_args(cortes_client):
    cortes_client.send_command({"command": "unkey", "args": []})
    assert_error(await_messages(1, cortes_client))
