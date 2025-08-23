"""
Risk manager: notional caps, drawdown caps, order rate limits, kill switch.
"""
import time
from typing import Dict

class RiskManager:
    def __init__(self):
        self.max_notional = 100.0  # SGD
        self.max_drawdown_pct = 0.05
        self.max_orders_per_min = 5
        self.order_times = []
        self.last_pnl = 0.0
        self.kill_switch = False

    def check_order(self, notional: float) -> bool:
        now = time.time()
        self.order_times = [t for t in self.order_times if now - t < 60]
        if notional > self.max_notional:
            return False
        if len(self.order_times) >= self.max_orders_per_min:
            return False
        if self.kill_switch:
            return False
        self.order_times.append(now)
        return True

    def update_pnl(self, pnl: float) -> None:
        if pnl < self.last_pnl * (1 - self.max_drawdown_pct):
            self.kill_switch = True
        self.last_pnl = pnl
