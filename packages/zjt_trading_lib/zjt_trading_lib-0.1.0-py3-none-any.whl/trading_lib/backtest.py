from decimal import Decimal
from uuid import UUID


from enums import OrderType, PositionStatus
from exchanges import BacktestFuturesExchange
from order_managers import BacktestFuturesOrderManager
from strategy import Strategy
from .typing import BacktestResult


class Backtest:
    """
    To be used to perform a backtest, evaluating
    the performance of strategy on experimental data.
    """

    def __init__(
        self,
        backtest_id: UUID,
        instrument: str,
        strategy: Strategy,
        starting_balance: float = 100_000,
        leverage: int = 10,
    ):
        self._backtest_id = backtest_id
        self._instrument = instrument
        self._starting_balance = starting_balance
        self._strat = strategy
        self._om = BacktestFuturesOrderManager(
            starting_balance=starting_balance, leverage=leverage
        )

        exchange = BacktestFuturesExchange({})
        self._om.set_exchange(exchange)
        self._strat.set_order_manager(self._om)

    def run(self):
        with self._strat:
            for tick in self._om._exchange.subscribe(self._instrument):
                # Placing and closing trades
                positions = list(self._om._positions.values())
                for pos in positions:
                    if pos.status == PositionStatus.OPEN:
                        if (pos.sl_price is not None and pos.sl_price == tick.last) or (
                            pos.tp_price is not None and pos.tp_price == tick.last
                        ):
                            self._om.close_position(pos.position_id, pos.current_amount)
                    elif pos.order_type in (OrderType.LIMIT, OrderType.STOP):
                        pos.status = PositionStatus.OPEN

                self._om.perform_risk_checks(tick)
                self._strat.run(tick)

        return self._build_backtest_result()

    def _build_backtest_result(self):
        closed_count = len(self._om._closed_positions)
        total_trades = len(self._om._positions) + closed_count

        n, wins = 0, 0
        for pos in self._om._closed_positions:
            if pos.realised_pnl is not None:
                n += 1
                if pos.realised_pnl > 0.0:
                    wins += 1

        win_rate = 1 / (n / wins) if wins else 0.0

        total_pnl = Decimal("0.0")
        for pos in self._om._closed_positions:
            total_pnl += pos.realised_pnl

        for pos in self._om.positions:
            total_pnl += pos.realised_pnl

        res = BacktestResult(
            backtest_id=self._backtest_id,
            total_pnl=total_pnl,
            starting_balance=self._starting_balance,
            end_balance=self._om._balance,
            total_trades=total_trades,
            win_rate=win_rate,
            positions=self._om._closed_positions + [*self._om.positions],
        )

        return res
