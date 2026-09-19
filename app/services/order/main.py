from email.mime import text

from fastapi import Depends, FastAPI
from pytest import Session
from pytest import Session
from app.services.order.api.order import router as order_router
from app.services.order.db.database import get_db
from sqlalchemy import text

app = FastAPI()
app.include_router(order_router, prefix="/api")


@app.get("/start")
async def start():
    return {"status": "Order Starting Endpoint"}

