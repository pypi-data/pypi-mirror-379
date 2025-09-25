import time
import pytest
from helpers import (
    assert_no_errors,
    await_messages,
    await_message_with_timeout,
    P_C_KEY,
    HOST,
    PIZARRO_PEST_PORT,
)


def configure_cortes(client):
    client.send_command({"command": "handle", "args": ["cortes"]})
    client.send_command({"command": "peer", "args": ["pizarro"]})
    client.send_command({"command": "key", "args": ["pizarro", P_C_KEY]})
    client.send_command(
        {
            "command": "at",
            "args": ["pizarro", "{}:{}".format(HOST, PIZARRO_PEST_PORT)],
        }
    )
    assert_no_errors(await_messages(3, client))


@pytest.mark.usefixtures()
def test_broadcast_text_search(cortes_client):
    configure_cortes(cortes_client)

    messages = [f"m{i}" for i in range(0, 2)]
    for message in messages:
        cortes_client.send_command({"command": "broadcast_text", "args": [message]})
        time.sleep(1)
        assert await_message_with_timeout(cortes_client, message)

    cortes_client.send_command({"command": "search", "args": ["m1"]})
    search_results = await_messages(1, cortes_client)
    assert search_results[0]["type"] == "search"

