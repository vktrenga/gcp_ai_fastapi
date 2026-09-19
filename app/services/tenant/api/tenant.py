from fastapi import APIRouter, Depends
from pytest import Session
from services.tenant.repositories.tenant_repositories import tenant_registration, tenant_login
from services.tenant.db.database import get_db 
from services.tenant.schemas.tenant_schema import LoginRequestSchema, LoginResponseSchema, TenantRequestSchema, TenantResponseSchema 

router = APIRouter(prefix="/tenant", tags=["Tenant"])

@router.post('/register', response_model= TenantResponseSchema)
def register(tenant_data: TenantRequestSchema, db: Session = Depends(get_db)):
    return tenant_registration(db, tenant_data)

@router.post('/login', response_model= LoginResponseSchema)
def login(login_data:LoginRequestSchema, db: Session= Depends(get_db)):
    return tenant_login(db,login_data)