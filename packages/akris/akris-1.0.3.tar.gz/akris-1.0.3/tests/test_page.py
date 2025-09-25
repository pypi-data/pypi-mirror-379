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
def test_broadcast_text_page_up(cortes_client):
    configure_cortes(cortes_client)

    messages = [f"m{i}" for i in range(0, 10)]
    for message in messages:
        cortes_client.send_command({"command": "broadcast_text", "args": [message]})
        time.sleep(1)
        assert await_message_with_timeout(cortes_client, message)

    cortes_client.send_command({"command": "page_up", "args": [time.time(), 1]})
    page_messages = await_messages(10, cortes_client)
    assert page_messages[0]["body"] == messages[0]
    assert page_messages[1]["body"] == messages[1]
    assert page_messages[2]["body"] == messages[2]


@pytest.mark.usefixtures()
def test_broadcast_text_m_page_up(cortes_client):
    configure_cortes(cortes_client)

    messages = [f"m{i}" for i in range(0, 10)]
    for message in messages:
        cortes_client.send_command({"command": "broadcast_text_m", "args": [message]})
        time.sleep(1)
        assert await_message_with_timeout(cortes_client, message)

    cortes_client.send_command({"command": "page_up", "args": [time.time(), 1]})
    page_messages = await_messages(10, cortes_client)
    assert page_messages[0]["body"] == messages[0]
    assert page_messages[1]["body"] == messages[1]
    assert page_messages[2]["body"] == messages[2]


@pytest.mark.usefixtures()
def test_direct_text_page_up(cortes_client):
    configure_cortes(cortes_client)

    messages = [f"m{i}" for i in range(0, 10)]
    for message in messages:
        cortes_client.send_command(
            {"command": "direct_text", "args": ["pizarro", message]}
        )
        time.sleep(1)
        assert await_message_with_timeout(cortes_client, message)

    cortes_client.send_command({"command": "page_up", "args": [time.time(), 1, "pizarro"]})
    page_messages = await_messages(10, cortes_client)
    assert page_messages[0]["body"] == messages[0]
    assert page_messages[1]["body"] == messages[1]
    assert page_messages[2]["body"] == messages[2]


@pytest.mark.usefixtures()
def test_direct_text_m_page_up(cortes_client):
    configure_cortes(cortes_client)

    messages = [f"m{i}" for i in range(0, 10)]
    for message in messages:
        cortes_client.send_command(
            {"command": "direct_text_m", "args": ["pizarro", message]}
        )
        time.sleep(1)
        assert await_message_with_timeout(cortes_client, message)

    cortes_client.send_command({"command": "page_up", "args": [time.time(), 1, "pizarro"]})
    page_messages = await_messages(10, cortes_client)
    assert page_messages[0]["body"] == messages[0]
    assert page_messages[1]["body"] == messages[1]
    assert page_messages[2]["body"] == messages[2]

@pytest.mark.usefixtures()
def test_broadcast_text_page_down(cortes_client):
    configure_cortes(cortes_client)

    now = time.time()
    time.sleep(1)
    messages = [f"m{i}" for i in range(0, 10)]
    for message in messages:
        cortes_client.send_command({"command": "broadcast_text", "args": [message]})
        time.sleep(1)
        assert await_message_with_timeout(cortes_client, message)

    cortes_client.send_command({"command": "page_down", "args": [now, 1]})
    page_messages = await_messages(10, cortes_client)
    assert page_messages[0]["body"] == messages[0]
    assert page_messages[1]["body"] == messages[1]
    assert page_messages[2]["body"] == messages[2]


@pytest.mark.usefixtures()
def test_broadcast_text_page_around(cortes_client):
    configure_cortes(cortes_client)

    time.sleep(1)
    messages = [f"m{i}" for i in range(0, 10)]
    sent_messages = []
    for message in messages:
        cortes_client.send_command({"command": "broadcast_text", "args": [message]})
        time.sleep(1)
        message = await_message_with_timeout(cortes_client, message)
        assert message
        sent_messages.append(message)

    cortes_client.send_command({"command": "page_around", "args": [sent_messages[4].get("message_hash")]})
    page_messages = await_messages(10, cortes_client)
    assert page_messages[0]["body"] == messages[0]
    assert page_messages[1]["body"] == messages[1]
    assert page_messages[2]["body"] == messages[2]
