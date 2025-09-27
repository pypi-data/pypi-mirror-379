from abc import abstractmethod
from decimal import Decimal

from enums import OrderType, Side
from ..exchanges import FuturesExchange
from ..typing import Position, MODIFY_SENTINEL


class FuturesOrderManager:

    def __init__(self):
        self._positions: dict[str, Position] = {}
        self._exchange: FuturesExchange | None = None

    def set_exchange(self, exchange: FuturesExchange) -> None:
        if not self._exchange:
            self._exchange = exchange

    @abstractmethod
    def login(self) -> bool: ...

    @abstractmethod
    def open_position(
        self,
        instrument: str,
        side: Side,
        order_type: OrderType,
        amount: Decimal,
        limit_price: float | None = None,
        stop_price: float | None = None,
        tp_price: float | None = None,
        sl_price: float | None = None,
    ) -> str | None:
        """
        Returns the position id or None if position
        couldn't be placed
        """

    @abstractmethod
    def modify_position(
        self,
        position_id: str,
        limit_price: float | None = MODIFY_SENTINEL,
        stop_price: float | None = MODIFY_SENTINEL,
        tp_price: float | None = MODIFY_SENTINEL,
        sl_price: float | None = MODIFY_SENTINEL,
    ) -> bool: ...

    """Returns whether or not the call was successfull"""

    @abstractmethod
    def close_position(
        self, position_id: str, price: float, amount: Decimal
    ) -> bool: ...

    @abstractmethod
    def close_all_positions(self) -> None: ...

    @abstractmethod
    def cancel_position(self, position_id: str) -> bool: ...

    @abstractmethod
    def cancel_all_positions(self) -> None: ...

    @property
    def positions(self) -> tuple[Position]:
        return tuple(self._positions.values())
