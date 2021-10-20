from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    bridge = Column(String)
    api_key = Column(String)
    api_secret = Column(String)

    max_open_trades = Column(Integer, default=0)
    current_open_trades = Column(Integer, default=0)
    is_bot_active = Column(Integer, default=False)

    orders = relationship('Order', back_populates='user')