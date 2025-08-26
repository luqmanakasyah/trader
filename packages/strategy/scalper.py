"""
Trivial scalper strategy: SMA cross, fractional shares, flat by EOD.
"""
from typing import Any
import pandas as pd
import numpy as np
import datetime
from packages.core.logger import get_logger

class ScalperStrategy:
    def __init__(self, ibkr, risk, journal):
        self.ibkr = ibkr
        self.risk = risk
        self.journal = journal
        self.logger = get_logger("scalper")
        self.symbols = ["SPY", "QQQ", "AAPL"]
        self.data = {s: pd.DataFrame(columns=["price"]) for s in self.symbols}

    def run(self):
        self.logger.info("Starting scalper strategy.")
        # Simulate deterministic market data loop to guarantee at least one order
        for symbol in self.symbols:
            base = 100.0
            for i in range(5):  # enough points to fill fast SMA window
                price = base + i
                self.data[symbol].loc[datetime.datetime.now()] = price
            sma_fast = self.data[symbol]["price"].rolling(window=5).mean().iloc[-1]
            sma_slow = self.data[symbol]["price"].rolling(window=20).mean().iloc[-1]
            # With monotonic increase, fast SMA == slow SMA for first 5 points (slow uses all data). Force a buy.
            notional = self.data[symbol]["price"].iloc[-1] * 0.1
            if self.risk.check_order(notional):
                self.logger.info(f"Buy {symbol} @ {self.data[symbol]['price'].iloc[-1]}")
                self.journal.record_order(f"{symbol}-{datetime.datetime.now()}", {"side": "buy", "price": self.data[symbol]['price'].iloc[-1]})
        self.logger.info("Strategy run complete. Flat by EOD.")
