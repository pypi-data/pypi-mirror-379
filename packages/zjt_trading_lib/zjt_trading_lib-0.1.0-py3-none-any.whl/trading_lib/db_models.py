from uuid import uuid4
from sqlalchemy import String, Float, BIGINT, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Ticks(Base):
    __tablename__ = "ticks"

    tick_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    instrument: Mapped[str] = mapped_column(String, nullable=False)
    last_price: Mapped[float] = mapped_column(Float, nullable=False)
    bid_price: Mapped[float] = mapped_column(Float, nullable=True)
    ask_price: Mapped[float] = mapped_column(Float, nullable=True)
    time: Mapped[int] = mapped_column(BIGINT, nullable=False)  # Unix Epoch seconds
