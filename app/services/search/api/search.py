from typing import Any, List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pytest import Session

from services.search.db.database import get_db
from services.search.repositories.search_repositories import search
from services.search.core.security import get_current_user
router = APIRouter(prefix='/search', tags=['search'])

@router.get('/') 
def search_product(query:Any, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    tenant_id = current_user.get('tenant_id')
    print(query)
    return search(db, query, tenant_id)

