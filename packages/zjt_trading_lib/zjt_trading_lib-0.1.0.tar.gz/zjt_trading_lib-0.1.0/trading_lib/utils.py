from contextlib import asynccontextmanager, contextmanager
from datetime import UTC, datetime
from typing import AsyncGenerator, Generator

from db_manager import DBManager
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


def get_datetime() -> datetime:
    return datetime.now(UTC)


@asynccontextmanager
async def get_db_sess() -> AsyncGenerator[AsyncSession, None]:
    async with DBManager.smaker.begin() as s:
        try:
            yield s
        except:
            await s.rollback()
            raise


@contextmanager
def get_db_sess_sync() -> Generator[Session, None, None]:
    with DBManager.smaker_sync.begin() as sess:
        try:
            yield sess
        except:
            sess.rollback()
            raise
