"""
IBKR API wrapper with reconnect logic.
"""
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import time
import threading
from packages.core.logger import get_logger

class IBKRClient(EWrapper, EClient):
    def __init__(self, host: str, port: int, client_id: int):
        EClient.__init__(self, self)
        self.host = host
        self.port = port
        self.client_id = client_id
        self.logger = get_logger("ibkr")
        self.connected = False
        self.connect_thread = threading.Thread(target=self._connect_loop)
        self.connect_thread.daemon = True
        self.connect_thread.start()

    def _connect_loop(self):
        while True:
            if not self.connected:
                try:
                    self.connect(self.host, self.port, self.client_id)
                    self.connected = True
                    self.logger.info("Connected to IB Gateway.")
                except Exception as e:
                    self.logger.error(f"Connect failed: {e}")
                    time.sleep(10)
            time.sleep(1)

    def disconnect(self):
        self.logger.info("Disconnecting from IB Gateway.")
        super().disconnect()
        self.connected = False
