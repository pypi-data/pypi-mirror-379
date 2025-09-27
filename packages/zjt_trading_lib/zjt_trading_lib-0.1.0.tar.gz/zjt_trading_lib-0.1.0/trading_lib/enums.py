from enum import Enum


class TradingPlatform(Enum):
    MT5 = "mt5"


class StrategyType(Enum):
    FUTURES = 0
    SPOT = 1


class Side(Enum):
    ASK = 0
    BID = 1


class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"


class PositionStatus(Enum):
    PENDING = 0
    OPEN = 1
    CLOSED = 2
    CANCELLED = 3
