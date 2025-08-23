"""
Unit test for OrderJournal.
"""
from packages.core.order_journal import OrderJournal

def test_idempotent_journal():
    journal = OrderJournal()
    journal.record_order("1", {"side": "buy", "price": 100})
    assert journal.get_order("1")["side"] == "buy"
    journal.record_order("1", {"side": "sell", "price": 101})
    assert journal.get_order("1")["side"] == "sell"
