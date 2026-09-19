from email.mime import text

from fastapi import Depends, FastAPI
from pytest import Session
from pytest import Session
from app.services.customer.api.customer import router as customer_router
from app.services.customer.db.database import get_db 
from sqlalchemy import text

app = FastAPI()
app.include_router(customer_router, prefix="/api")


@app.get("/start")
async def start():
    return {"status": "Customer Starting Endpoint"}

