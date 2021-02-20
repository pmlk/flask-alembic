import json

import pytest
from flask.wrappers import Response
from flask.testing import FlaskClient

from myapp.app import flask_app


def test_get_users(client: FlaskClient):
    response: Response = client.get("/users")

    assert json.loads(response.data) == {"users": [{"name": "pmlk"}]}


@pytest.fixture
def client() -> FlaskClient:
    return flask_app.test_client()
