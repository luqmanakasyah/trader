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
        # Simulate market data loop
        for symbol in self.symbols:
            price = np.random.uniform(100, 500)
            self.data[symbol].loc[datetime.datetime.now()] = price
            sma_fast = self.data[symbol]["price"].rolling(window=5).mean().iloc[-1]
            sma_slow = self.data[symbol]["price"].rolling(window=20).mean().iloc[-1]
            if sma_fast and sma_slow and sma_fast > sma_slow:
                notional = price * 0.1  # Fractional
                if self.risk.check_order(notional):
                    self.logger.info(f"Buy {symbol} @ {price}")
                    self.journal.record_order(f"{symbol}-{datetime.datetime.now()}", {"side": "buy", "price": price})
            elif sma_fast and sma_slow and sma_fast < sma_slow:
                notional = price * 0.1
                if self.risk.check_order(notional):
                    self.logger.info(f"Sell {symbol} @ {price}")
                    self.journal.record_order(f"{symbol}-{datetime.datetime.now()}", {"side": "sell", "price": price})
        self.logger.info("Strategy run complete. Flat by EOD.")
