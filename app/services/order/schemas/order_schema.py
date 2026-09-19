from pydantic import BaseModel
from typing import Any, List

class OrderItemSchema(BaseModel):
    product_id: str
    quantity: int
    price: float

    class Config:
        from_attributes = True

class OrderSchema(BaseModel):
    customer_id: str
    items: List[OrderItemSchema] = []

    class Config:
        from_attributes = True

class OrderItemSchemaResponse(BaseModel):
    product_id: str
    quantity: int
    price: float
    amount:float
    discount:float
    total_amount:float
    class Config:
        from_attributes = True

class OrderSchemaResponse(BaseModel):
    customer_id: str
    id:Any
    cross_amount:float
    net_amount:float
    discount:float
    status:str
    items: List[OrderItemSchemaResponse] = []

    class Config:
        from_attributes = True
