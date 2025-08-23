# Trader Monorepo

End-to-end trading bot stack for Interactive Brokers (IBKR), designed for small-scale validation and scalable deployment on OVH VPS (Ubuntu 24.04 LTS).

## Repo Layout

```
trader/
  apps/
    gateway/              # Dockerfile for IB Gateway + IBC (headless)
    strategy/             # Python service using ibapi to connect, trade, and log fills
    monitor/              # Prometheus exporters, health endpoints
  packages/
    core/                 # utils: logging, retry, backoff, idempotent order journal
    ibkr/                 # wrapper around ibapi with reconnect logic
    risk/                 # pre-trade checks, kill switch
  infra/
    docker-compose.yml    # defines all services
    deploy/
      deploy.sh           # idempotent deploy script
      env.gateway         # example only (never commit secrets)
      env.strategy        # example only
      env.postgres        # example only
  tests/
    unit/                 # plumbing tests
    sim/                  # fake data and fills
  .github/workflows/
    ci.yml                # lint + test + docker build
    deploy.yml            # tag-based CD deploy to OVH VPS
  pyproject.toml
  README.md
```

## Setup

1. Clone repo, copy env files, fill secrets.
2. Build and run: `docker-compose up --build`
3. For prod deploy, see infra/deploy/deploy.sh

## Environment Variables

- See `infra/deploy/env.*` for templates.

## Local Run

- `docker-compose up`

## Production

- Tag and push to GitHub, deploy via Actions.

## Monitoring

- Prometheus scrapes strategy, Grafana dashboards auto-provisioned.

## Testing

- `pytest tests/unit`
- Sim tests: `pytest tests/sim`

## Services

- **gateway**: IB Gateway + IBC (headless)
- **strategy**: Python trading bot
- **monitor**: Prometheus exporters
- **redis**: event bus
- **postgres**: storage
- **prometheus/grafana**: monitoring

## Scaling

- Start with S$100, fractional US equities. Scale after pipeline validation.

---

See each folder for more details and code comments.
