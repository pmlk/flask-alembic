from contextlib import contextmanager
from typing import ContextManager

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from myapp.database.base import Base
from myapp import app


@pytest.fixture(autouse=True)
def db_session(monkeypatch) -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    @contextmanager
    def _db_session() -> ContextManager[Session]:
        try:
            yield session
        finally:
            pass

    monkeypatch.setattr(app, "_db_session", _db_session)

    yield session

    Base.metadata.drop_all(engine)
    session.close()
