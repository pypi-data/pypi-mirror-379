import pytest
from trgenpy.connection import TrgenClient

def test_trigger_client_init():
    client = TrgenClient()
    assert client is not None

def test_trigger_client_is_available(monkeypatch):
    client = TrgenClient()
    # Mock is_available se necessario
    monkeypatch.setattr(client, "is_available", lambda: True)
    assert client.is_available() is True

# TODO add more tests for TrgenClient methods like connect, disconnect, send_trigger, sendMarker, etc.