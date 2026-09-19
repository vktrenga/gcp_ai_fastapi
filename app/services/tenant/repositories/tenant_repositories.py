


import uuid

from pytest import Session

from services.tenant.core.tenant_model import Tenant
from services.tenant.schemas.tenant_schema import TenantRequestSchema, TenantResponseSchema


def tenant_registration(db: Session, tenant_data: TenantRequestSchema):
    tenant_record = Tenant(
        tenant_id = str(uuid.uuid4()),
        tenant_name = tenant_data.tenant_name,
        email_id = tenant_data.email_id,
        address = tenant_data.address,
        domain_name = tenant_data.address,
    )
    tenant_record.set_password(tenant_data.password)
    db.add(tenant_record)
    db.commit()
    db.refresh(tenant_record)

    return tenant_record

