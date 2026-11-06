# Liquidity Whale Monitor (Starter v0.1)

A starter prototype for money-flow and large-trade monitoring. It currently uses demo/sample data only.
It is **not production-ready** and is not connected to a real exchange feed.

## Run (requires Python 3.11+)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Then open http://127.0.0.1:8000/docs

## Included
- FastAPI starter backend
- trade-value, net-flow, VWAP, large-trade helpers
- SQLite persistence
- sample/demo data
- basic API endpoints
- unit-test source files

## Not included yet
- live market data/API connection
- robust reconnect/backfill
- institutional identity or verified block-trade classification
- production alerts, performance/load tests, deployment to a public server

Market data provider access and licensing must be arranged before real-time use.
