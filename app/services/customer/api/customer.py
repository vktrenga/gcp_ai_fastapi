from fastapi import APIRouter
router = APIRouter()

@router.get("/orders")
async def get_orders():
    return {"orders": []}


@router.post("/orders")
async def create_order():
    return {"orders": []}

@router.get("/orders/customers/{customer_id}")
async def get_customer_orders(customer_id: str):
    return {"orders": {'customer_id': customer_id}}