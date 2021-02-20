from sqlalchemy import Column, String

from myapp.database.base import Base


class User(Base):
    __tablename__ = "users"

    name = Column(String, primary_key=True, index=True, unique=True)
