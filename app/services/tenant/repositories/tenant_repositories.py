


from fastapi import HTTPException

import uuid

from pytest import Session

from services.tenant.core.security import create_access_token
from services.tenant.core.tenant_model import Tenant
from services.tenant.schemas.tenant_schema import LoginRequestSchema, TenantRequestSchema, TenantResponseSchema


def tenant_registration(db: Session, tenant_data: TenantRequestSchema):
    existing = db.query(Tenant).filter(Tenant.email_id == tenant_data.email_id).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail={
                "field": "email_id",
                "error": f"Email '{tenant_data.email_id}' is already registered.",
                "hint": "Use a different email address."
            }
        )
    tenant_record = Tenant(
        tenant_id = str(uuid.uuid4()),
        tenant_name = tenant_data.tenant_name,
        email_id = tenant_data.email_id,
        address = tenant_data.address,
        domain_name = tenant_data.domain_name,
    )
    tenant_record.set_password(tenant_data.password)
    db.add(tenant_record)
    db.commit()
    db.refresh(tenant_record)

    return tenant_record


def tenant_login(db: Session, login_data:LoginRequestSchema):
    existing = db.query(Tenant).filter(Tenant.email_id == login_data.email_id).first()
    if not existing:
        raise HTTPException(
            status_code=401,
            detail={
                "error": "User is not existing",
            }
        )
    if not existing.check_password(login_data.password):
        raise HTTPException(
            status_code=401,
            detail={"error": "Invalid password"}
        )
    token_data = {
        "sub": str(existing.tenant_id),
        "email": existing.email_id,
    }
    token = create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}
    
