from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.order.db.database import get_db
from services.order.repositories.order import create_order, get_orders, get_order
from services.order.schemas.order_schema import OrderSchema, OrderSchemaResponse

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderSchema)
def create_order_endpoint(order: OrderSchema, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/", response_model=list[OrderSchemaResponse])
def list_orders_endpoint(db: Session = Depends(get_db)):
    return get_orders(db)

@router.get("/{order_id}", response_model=OrderSchema)
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    return get_order(db, order_id)
