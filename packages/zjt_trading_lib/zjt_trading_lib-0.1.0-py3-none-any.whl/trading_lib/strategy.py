from abc import abstractmethod

from trading_lib.order_managers.futures_order_manager import FuturesOrderManager
from trading_lib.enums import StrategyType
from trading_lib.typing import Tick


class Strategy:
    """
    Base class for all startegies. The run method is called
    when a new tick comes in
    """

    def __init__(
        self, type: StrategyType, instrument: str, om: FuturesOrderManager | None = None
    ):
        self._type = type
        self._instrument = instrument.lower()
        self._om: FuturesOrderManager | None = om

    def set_order_manager(self, om: FuturesOrderManager) -> None:
        if not self._om:
            self._om = om

    @abstractmethod
    def run(self, tick: Tick): ...

    def shutdown(self):
        """
        Contains any necessary shutdown logic. For example
        closing all positions and / or orders.
        """

    def startup(self):
        """
        Pretrade logic to be ran before receiving ticks
        """
        if not self._om:
            raise Exception("OM not initialised.")
        if not self._om.login():
            raise Exception("OM failed to login")

    def __enter__(self):
        self.startup()
        return self

    def __exit__(self, exc_type, exc_value, tcb):
        self.shutdown()

    @property
    def type(self) -> StrategyType:
        return self._type
