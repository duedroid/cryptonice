from sqlalchemy import Column, Integer, String

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    api_key = Column(String)
    api_secret = Column(String)