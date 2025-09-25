import pytest
from helpers import (
    assert_no_errors,
    await_messages,
    await_message_with_timeout,
    PIZARRO_PEST_PORT,
    HOST,
    CORTES_PEST_PORT,
    P_C_KEY,
)


def configure_pizarro(client):
    client.send_command({"command": "handle", "args": ["pizarro"]})
    client.send_command({"command": "peer", "args": ["cortes"]})
    client.send_command({"command": "key", "args": ["cortes", P_C_KEY]})
    client.send_command(
        {"command": "at", "args": ["cortes", "{}:{}".format(HOST, CORTES_PEST_PORT)]}
    )
    assert_no_errors(await_messages(4, client))


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
    assert_no_errors(await_messages(4, client))


@pytest.mark.usefixtures()
def test_direct_text(cortes_client, pizarro_client):
    configure_pizarro(pizarro_client)
    configure_cortes(cortes_client)

    message_body = "conquisto"
    cortes_client.send_command(
        {"command": "direct_text", "args": ["pizarro", message_body]}
    )
    assert await_message_with_timeout(pizarro_client, message_body)
    assert await_message_with_timeout(cortes_client, message_body)

@pytest.mark.skip(reason="broken")
@pytest.mark.usefixtures()
def test_emoji(cortes_client, pizarro_client):
    configure_pizarro(pizarro_client)
    configure_cortes(cortes_client)

    message_body = "conquisto 🔥"
    cortes_client.send_command(
        {"command": "direct_text", "args": ["pizarro", message_body]}
    )
    await_messages(1, cortes_client)
    await_messages(1, pizarro_client)
