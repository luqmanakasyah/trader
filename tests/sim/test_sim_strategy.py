"""
Sim test for ScalperStrategy with fake market data and fills.
"""
from packages.strategy.scalper import ScalperStrategy
from packages.core.order_journal import OrderJournal
from packages.risk.risk import RiskManager

class FakeIBKR:
    pass

def test_sim_run():
    ibkr = FakeIBKR()
    risk = RiskManager()
    journal = OrderJournal()
    strategy = ScalperStrategy(ibkr, risk, journal)
    strategy.run()
    # Check journal has orders
    assert len(journal.orders) > 0
