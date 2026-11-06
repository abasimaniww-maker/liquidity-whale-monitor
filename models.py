from pydantic import BaseModel
from datetime import datetime

class Trade(BaseModel):
    trade_id: str
    symbol: str
    price: float
    quantity: float
    side: str  # BUY or SELL aggressor
    timestamp: datetime

class OrderBook(BaseModel):
    symbol: str
    bids: list[tuple[float, float]]
    asks: list[tuple[float, float]]
