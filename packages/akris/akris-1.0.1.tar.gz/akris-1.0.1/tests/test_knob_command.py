import pytest
from helpers import assert_no_errors, await_messages, await_message_with_timeout


@pytest.mark.usefixtures()
def test_knobs(cortes_client):
    cortes_client.send_command({"command": "knob", "args": []})
    assert_no_errors(await_messages(1, cortes_client))


@pytest.mark.usefixtures()
def test_knob_get(cortes_client):
    cortes_client.send_command({"command": "knob", "args": ["max_bounces"]})
    await_message_with_timeout(cortes_client, {"max_bounces": 3})


@pytest.mark.usefixtures()
def test_knob_set(cortes_client):
    cortes_client.send_command({"command": "knob", "args": ["max_bounces", "4"]})
    await_message_with_timeout(cortes_client, {"max_bounces": 4})
