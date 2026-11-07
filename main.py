from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
from models import Trade, OrderBook
from analytics import net_flow, vwap, large_trades, depth_imbalance

app = FastAPI(title="Liquidity Whale Monitor", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://abasimaniww-maker.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
demo_trades = [
    Trade(trade_id="demo-1", symbol="AAPL", price=190.0, quantity=100, side="BUY", timestamp=datetime.now(timezone.utc)),
    Trade(trade_id="demo-2", symbol="AAPL", price=189.5, quantity=80, side="SELL", timestamp=datetime.now(timezone.utc)),
    Trade(trade_id="demo-3", symbol="AAPL", price=190.2, quantity=500, side="BUY", timestamp=datetime.now(timezone.utc)),
]

@app.get("/health")
def health():
    return {"status": "ok", "mode": "demo"}

@app.get("/symbols")
def symbols():
    return {"symbols": sorted({t.symbol for t in demo_trades})}

@app.get("/trades")
def trades(symbol: str = "AAPL"):
    return [t.model_dump() for t in demo_trades if t.symbol.upper() == symbol.upper()]

@app.post("/trades")
def add_trade(trade: Trade):
    demo_trades.append(trade)
    return {"accepted": True, "trade_id": trade.trade_id}

@app.get("/analytics/{symbol}")
def analytics(symbol: str):
    selected = [t for t in demo_trades if t.symbol.upper() == symbol.upper()]
    return {"symbol": symbol.upper(), **net_flow(selected), "vwap": vwap(selected), "trade_count": len(selected)}

@app.get("/large-trades/{symbol}")
def get_large_trades(symbol: str, min_value: float = 100000):
    selected = [t for t in demo_trades if t.symbol.upper() == symbol.upper()]
    return [t.model_dump() for t in large_trades(selected, min_value)]

@app.post("/orderbook/imbalance")
def orderbook_imbalance(book: OrderBook):
    return {"symbol": book.symbol, "depth_imbalance_top5": depth_imbalance(book)}

@app.post("/alerts/test")
def test_alert():
    return {"status": "demo", "message": "Alert endpoint placeholder; Telegram credentials not configured."}
