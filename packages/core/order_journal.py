"""
Idempotent order journal for tracking orders and fills.
"""
from typing import Dict, Any
import threading

class OrderJournal:
    def __init__(self):
        self.lock = threading.Lock()
        self.orders = {}

    def record_order(self, order_id: str, order_data: Dict[str, Any]) -> None:
        with self.lock:
            self.orders[order_id] = order_data

    def get_order(self, order_id: str) -> Dict[str, Any]:
        return self.orders.get(order_id, {})
