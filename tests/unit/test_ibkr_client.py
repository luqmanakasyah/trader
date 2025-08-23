"""
Unit test for IBKRClient reconnect logic (mocked).
"""
import pytest
from unittest.mock import patch
from packages.ibkr.ibkr_client import IBKRClient

def test_reconnect():
    with patch.object(IBKRClient, 'connect', return_value=None) as mock_connect:
        client = IBKRClient("localhost", 4002, 1)
        client.connected = False
        client._connect_loop()
        assert mock_connect.called
