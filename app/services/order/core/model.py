# core/models.py
from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from services.order.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, index=True)
    status = Column(String, default="pending")
    cross_amount = Column(Float, default=0)
    discount = Column(Float, default=0)   # ✅ use Float not float
    net_amount = Column(Float, default=0) # ✅ use Float not float

    # Relationship with OrderItem
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float, default=0)
    amount = Column(Float, default=0)
    discount = Column(Float, default=0)   # ✅ typo fixed (decofault → default)
    total_amount = Column(Float, default=0)

    # Relationship with Order
    order = relationship("Order", back_populates="items")
