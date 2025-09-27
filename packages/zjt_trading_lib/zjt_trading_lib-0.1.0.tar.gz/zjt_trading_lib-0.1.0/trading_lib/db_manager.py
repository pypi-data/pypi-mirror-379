from sqlalchemy.orm import sessionmaker


class DBManager:
    smaker: sessionmaker | None = None
    smaker_sync: sessionmaker | None = None
