import uuid
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from services.product.db.database import Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), nullable=False)

    product_name = Column(String, nullable=False)
    product_description = Column(String, nullable=False)

    # Additional useful fields
    category = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    sku = Column(String, unique=True, nullable=True)  # stock keeping unit
    price = Column(Float, nullable=False, default=0.0)
    currency = Column(String, default="INR")
    stock_quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

    # Audit fields
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

