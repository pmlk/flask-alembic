from flask import Flask


flask_app = Flask(__name__)


@flask_app.route("/users")
def get_users():
    return {"users": [{"name": "pmlk"}]}
