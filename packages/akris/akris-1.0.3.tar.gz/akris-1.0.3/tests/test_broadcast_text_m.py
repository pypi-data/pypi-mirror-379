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
def test_broadcast_text_m(cortes_client, pizarro_client):
    configure_pizarro(pizarro_client)
    configure_cortes(cortes_client)

    # when broken apart this currently comes across damaged in some way

    text = """Ἄνδρα μοι ἔννεπε, Μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
    πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν:
    πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
    πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
    ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.

    δέκαῳ δ᾽ έτει μῆνι συνήνετο Ζεύς ἄναξ: ἐλθεῖν δ᾽ Ὀδυσσῆα τόν
    γ᾽ ἠπείγοντο θεοὶ πάντες, οὐδ᾽ ἦλθε, δύω δ᾽ ἔτι πόντον ἐλώρια
    τεῦχε κύνες οἰωνοῖσί τε πᾶσι, καὶ μένος ἠνείκετο λαῶν."""

    cortes_client.send_command({"command": "broadcast_text_m", "args": [text]})
    await_messages(3, cortes_client)
    await_messages(3, pizarro_client)

@pytest.mark.skip(reason="broken")
@pytest.mark.usefixtures()
def test_emoji(cortes_client, pizarro_client):
    configure_pizarro(pizarro_client)
    configure_cortes(cortes_client)

    text = "🔥"

    cortes_client.send_command({"command": "broadcast_text_m", "args": [text]})
    await_messages(1, cortes_client)
    await_messages(1, pizarro_client)
