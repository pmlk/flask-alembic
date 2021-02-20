import pytest
from sqlalchemy.orm import Session

from myapp.database import users as db_users
from myapp.database.models import User


def test_add_user(db_session: Session):
    username = "foo"
    db_users.add_user(db_session, username)

    users = db_session.query(User).all()
    assert len(users) == 1
    assert users[0].name == username


def test_get_users(db_session_with_users: Session):
    users = db_users.get_users(db_session_with_users)

    usernames = list(map(lambda user: user.name, users))
    assert len(usernames) == 2
    assert "foo" in usernames
    assert "bar" in usernames


@pytest.fixture()
def db_session_with_users(db_session: Session) -> Session:
    usernames = ["foo", "bar"]
    for username in usernames:
        db_users.add_user(db_session, username)

    return db_session
