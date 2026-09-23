from datetime import datetime
from typing import Any, Optional

from pydantic import UUID4, BaseModel


class SearchResponseSchema(BaseModel):
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