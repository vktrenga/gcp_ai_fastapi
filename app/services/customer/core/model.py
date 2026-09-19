# core/models.py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(String, primary_key=True)
    customer_id = Column(String, nullable=False)
    status = Column(String, default="PLACED")

    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String, ForeignKey("orders.order_id"))
    product_id = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
