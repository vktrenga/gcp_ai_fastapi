from pydantic import BaseModel
from typing import Any, List, Optional

from sqlalchemy import String  

class TenantRequestSchema(BaseModel):
    tenant_name: str
    tenant_domain:Optional[str] = None
    email_id: str
    address: Optional[str] = None
    password: str

class TenantResponseSchema(TenantRequestSchema): 
    tenant_id: Any

    class Config:
        fields = {
            "password": {"exclude":True}
        }