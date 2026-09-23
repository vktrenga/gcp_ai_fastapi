from datetime import datetime
from typing import Any, Optional

from pydantic import UUID4, BaseModel


class ProductBase(BaseModel):
    product_name: str
    product_description: str
    category: Optional[str] = None
    brand: Optional[str] = None
    sku: Optional[str] = None
    price: float
    currency: Optional[str] = "INR"
    stock_quantity: Optional[int] = 0
    is_active: Optional[bool] = True

class ProductCreateSchema(ProductBase):
    """Schema for creating a product"""
    tenant_id: Optional[UUID4] = None
    pass

class ProductUpdateSchema(BaseModel):
    """Schema for updating a product"""
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    stock_quantity: Optional[int] = None
    is_active: Optional[bool] = None

class ProductResponseSchema(BaseModel):
    product_id: UUID4
    tenant_id: UUID4
    product_name: str
    product_description: str
    category: Optional[str]
    brand: Optional[str]
    sku: Optional[str]
    price: float
    currency: str
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    embedding: Optional[Any]

    class Config:
        from_attributes = True