"""
Monitor service: exposes /health and /metrics endpoints for Prometheus scraping.
"""
from fastapi import FastAPI
from prometheus_client import Gauge, generate_latest

app = FastAPI()
health_gauge = Gauge('monitor_health', 'Health status')

@app.get("/health")
def health():
    health_gauge.set(1)
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return generate_latest()
