import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from myapp.database.base import Base


@pytest.fixture(autouse=True)
def db_session(monkeypatch) -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    yield session

    Base.metadata.drop_all(engine)
    session.close()
