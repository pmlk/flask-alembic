from typing import List

from sqlalchemy.orm import Session

from myapp.database.models import User


def add_user(session: Session, name: str):
    user = User(name=name)
    session.add(user)
    session.commit()


def get_users(session: Session) -> List[User]:
    return session.query(User).all()
