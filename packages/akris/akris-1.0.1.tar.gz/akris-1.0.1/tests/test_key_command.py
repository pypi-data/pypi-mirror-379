import pytest
from helpers import await_messages, assert_no_errors, assert_error


@pytest.mark.usefixtures()
def test_add_key(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "atahualpa",
                "wQjzT+gDEHilgmFDao7zORJ5PKMjEMWstxMAi/hVTK3coooUA+6+o705LWkAPWFZVLtIjgx2Vh+9Xr5fnPXBfQ==",
            ],
        }
    )
    assert_no_errors(await_messages(2, cortes_client))


@pytest.mark.usefixtures()
def test_duplicate_key(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "atahualpa",
                "wQjzT+gDEHilgmFDao7zORJ5PKMjEMWstxMAi/hVTK3coooUA+6+o705LWkAPWFZVLtIjgx2Vh+9Xr5fnPXBfQ==",
            ],
        }
    )
    assert_no_errors(await_messages(2, cortes_client))
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "atahualpa",
                "wQjzT+gDEHilgmFDao7zORJ5PKMjEMWstxMAi/hVTK3coooUA+6+o705LWkAPWFZVLtIjgx2Vh+9Xr5fnPXBfQ==",
            ],
        }
    )
    assert_error(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_invalid_key(cortes_client):
    cortes_client.send_command({"command": "peer", "args": ["atahualpa"]})
    assert_no_errors(await_messages(1, cortes_client))
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "atahualpa",
                "4i+KHefkvTVUbeskTh4rGHiKSdDbCSnsSNKpvKHhCZT9yEzRkdVNjQP6KjDzeSM3d4M0RbwNezGcfAGcD5VtQ==",
            ],
        }
    )
    assert_error(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_no_such_peer(cortes_client):
    cortes_client.send_command(
        {
            "command": "key",
            "args": [
                "pizarro",
                "wQjzT+gDEHilgmFDao7zORJ5PKMjEMWstxMAi/hVTK3coooUA+6+o705LWkAPWFZVLtIjgx2Vh+9Xr5fnPXBfQ==",
            ],
        }
    )
    assert_error(await_messages(1, cortes_client))
