from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pytest import Session

from services.product.db.database import get_db
from services.product.repositories.product_repositories import create_product, get_list, get_product, update_product
from services.product.schemas.product_schemas import ProductCreateSchema, ProductResponseSchema, ProductUpdateSchema
from services.product.core.security import get_current_user
router = APIRouter(prefix='/products', tags=['products'])

@router.post('/') 
def create(data:ProductCreateSchema, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    data.tenant_id = current_user.get('tenant_id')
    return create_product(db, data)

@router.patch("/{product_id}", response_model=ProductResponseSchema)
def update(
    product_id: str,
    data: ProductUpdateSchema,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return update_product(db, product_id, data, tenant_id=current_user.get('tenant_id'))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{product_id}", response_model=ProductResponseSchema)
def get(
    product_id: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return get_product(db, product_id, tenant_id=current_user.get('tenant_id'))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=List[ProductResponseSchema])
def get(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        
        return get_list(db, tenant_id=current_user.get('tenant_id'))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))