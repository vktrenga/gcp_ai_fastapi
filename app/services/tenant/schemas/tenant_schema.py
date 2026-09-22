import re
from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator

class TenantBaseSchema(BaseModel):
    tenant_name: str
    domain_name: Optional[str] = None
    email_id:  EmailStr 
    address: Optional[str] = None

class TenantRequestSchema(TenantBaseSchema):
    password: str   # only request includes password
    
    @field_validator("password")
    def validate_password_strength(cls, value: str):
        # At least 8 chars, one uppercase, one lowercase, one digit, one special char
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(pattern, value):
            raise ValueError(
                "Password must be at least 8 characters long, "
                "include uppercase, lowercase, number, and special character."
            )
        return value

    # Domain name validator
    @field_validator("domain_name")
    def validate_domain(cls, value: Optional[str]):
        if value is None:
            return value
        # Simple domain regex (example.com, sub.example.org)
        pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid domain name format.")
        return value

class TenantResponseSchema(TenantBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    tenant_id: Any  # only response includes tenant_id


class LoginRequestSchema(BaseModel):
    email_id:EmailStr
    password:str

class LoginResponseSchema(BaseModel):
    access_token : str
    token_type: str
    