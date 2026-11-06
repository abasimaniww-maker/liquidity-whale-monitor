from collections import defaultdict

def trade_value(price: float, quantity: float) -> float:
    return price * quantity

def net_flow(trades):
    # Only meaningful when aggressor side is supplied by a trusted feed.
    buy = sum(trade_value(t.price, t.quantity) for t in trades if t.side.upper() == "BUY")
    sell = sum(trade_value(t.price, t.quantity) for t in trades if t.side.upper() == "SELL")
    return {"buy_value": buy, "sell_value": sell, "net_flow": buy - sell}

def vwap(trades):
    total_qty = sum(t.quantity for t in trades)
    if total_qty == 0:
        return None
    return sum(t.price * t.quantity for t in trades) / total_qty

def large_trades(trades, minimum_value: float):
    return [t for t in trades if trade_value(t.price, t.quantity) >= minimum_value]

def depth_imbalance(book):
    bid_qty = sum(q for _, q in book.bids[:5])
    ask_qty = sum(q for _, q in book.asks[:5])
    denom = bid_qty + ask_qty
    return 0.0 if denom == 0 else (bid_qty - ask_qty) / denom
