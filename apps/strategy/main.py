"""
Main entrypoint for strategy service.
Connects to IB Gateway, subscribes to market data, runs scalper strategy, logs fills, exposes health/metrics.
"""
import os
from packages.ibkr.ibkr_client import IBKRClient
from packages.core.logger import get_logger
from packages.risk.risk import RiskManager
from packages.core.order_journal import OrderJournal
from packages.strategy.scalper import ScalperStrategy
from prometheus_client import start_http_server, Gauge
from fastapi import FastAPI
import uvicorn

logger = get_logger()
app = FastAPI()

health_gauge = Gauge('strategy_health', 'Health status')

@app.get("/health")
def health():
    health_gauge.set(1)
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    # Prometheus metrics auto-exposed
    return {}

if __name__ == "__main__":
    start_http_server(8000)
    ibkr = IBKRClient(
        host=os.getenv("IB_HOST", "ib-gateway"),
        port=int(os.getenv("IB_PORT", 4002)),
        client_id=int(os.getenv("IB_CLIENT_ID", 1)),
    )
    risk = RiskManager()
    journal = OrderJournal()
    strategy = ScalperStrategy(ibkr, risk, journal)
    strategy.run()
    uvicorn.run(app, host="0.0.0.0", port=8000)
