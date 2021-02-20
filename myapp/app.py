from contextlib import contextmanager
from typing import ContextManager

from flask import Flask
from sqlalchemy.orm import Session

from myapp.database.base import SessionLocal
from myapp.database import users as db_users

flask_app = Flask(__name__)


@contextmanager
def _db_session() -> ContextManager[Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@flask_app.route("/users")
def get_users():
    with _db_session() as session:
        users = db_users.get_users(session)

    user_dicts = list(map(lambda user: {"name": user.name}, users))

    return {"users": user_dicts}


@flask_app.route("/users/add/<name>")
def add_user(name: str):
    with _db_session() as session:
        db_users.add_user(session, name)

    return "OK"
