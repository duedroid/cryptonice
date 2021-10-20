from sqlalchemy import Boolean, Column, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from db.base_class import Base


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(String)
    pair = Column(String, nullable=False)
    side = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)
    amount = Column(DECIMAL, nullable=False)
    amount_bridge = Column(DECIMAL, nullable=False)
    profit = Column(DECIMAL)
    profit_bridge = Column(DECIMAL)
    order_data = Column(JSONB, default=dict)

    is_force_sell = Column(Boolean, default=False)
    is_buy_order_sell = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='orders')