from datetime import datetime
from decimal import Decimal
from enum import Enum
from json import loads
from typing import Literal, NamedTuple
from uuid import UUID

from pydantic import BaseModel, Field

from trading_lib.enums import OrderType, PositionStatus, Side
from trading_lib.utils import get_datetime


BullishBearish = Literal["bullish", "bearish"]


class Tick(NamedTuple):
    last: float
    time: datetime


class OHLC(NamedTuple):
    open: float
    high: float
    low: float
    close: float
    time: int


class FVG(NamedTuple):
    above: float
    below: float


class MSS(NamedTuple):
    type: BullishBearish
    present: bool
    swing_high_idx: int
    swing_low_idx: int
    breakout_idx: int


class CustomBaseModel(BaseModel):
    model_config = {
        "json_encoders": {
            UUID: str,
            datetime: lambda dt: dt.isoformat(),
            Enum: lambda e: e.value,
        }
    }

    def to_serialisable_dict(self) -> dict:
        return loads(self.model_dump_json())


# TODO: Add support for partials
class Position(CustomBaseModel):
    position_id: str  # DB id
    instrument: str
    side: Side
    order_type: OrderType
    starting_amount: Decimal
    current_amount: Decimal = None
    price: float | None = None
    limit_price: float | None = None
    stop_price: float | None = None
    tp_price: float | None = None
    sl_price: float | None = None
    realised_pnl: Decimal | None = Decimal("0.0")
    unrealised_pnl: Decimal | None = Decimal("0.0")
    status: PositionStatus = PositionStatus.PENDING
    created_at: datetime | None = Field(default_factory=get_datetime)
    close_price: float | None = None
    closed_at: datetime | None = None
    extras: dict | None = None  # Extra platform specific data

    def model_post_init(self, context):
        self.current_amount = self.starting_amount


class BacktestResult(CustomBaseModel):
    backtest_id: str
    total_pnl: Decimal
    starting_balance: Decimal
    end_balance: Decimal
    total_trades: int
    win_rate: float
    positions: list[Position]


MODIFY_SENTINEL = "*"
