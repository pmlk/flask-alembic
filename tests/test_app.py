import json

import pytest
from flask.wrappers import Response
from flask.testing import FlaskClient
from sqlalchemy.orm import Session

from myapp.app import flask_app
from myapp.database import users as db_users


def test_get_users(client: FlaskClient, db_session: Session):
    username = "pmlk"
    db_users.add_user(db_session, username)

    response: Response = client.get("/users")

    assert json.loads(response.data) == {"users": [{"name": username}]}


def test_add_user(client: FlaskClient, db_session: Session):
    username = "foo"

    client.get(f"/users/add/{username}")
    users = db_users.get_users(db_session)
    assert any(username == user.name for user in users)


@pytest.fixture
def client() -> FlaskClient:
    return flask_app.test_client()
