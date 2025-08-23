"""
Unit test for RiskManager.
"""
import pytest
from packages.risk.risk import RiskManager

def test_order_limits():
    risk = RiskManager()
    assert risk.check_order(50.0) is True
    assert risk.check_order(200.0) is False
    for _ in range(risk.max_orders_per_min):
        assert risk.check_order(10.0) is True
    assert risk.check_order(10.0) is False

def test_drawdown_kill_switch():
    risk = RiskManager()
    risk.update_pnl(100.0)
    risk.update_pnl(90.0)  # 10% drawdown
    assert risk.kill_switch is True
