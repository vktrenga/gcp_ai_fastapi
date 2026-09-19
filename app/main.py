from email.mime import text

from fastapi import Depends, FastAPI
from pytest import Session
from pytest import Session
from services.order.api.order import router as order_router
from services.order.db.database import get_db as order_get_db
from sqlalchemy import text


### tenant  Start
from services.tenant.api.tenant import router as tenant_router
from services.tenant.db.database import create_tables as create_tenant_tables


app = FastAPI()
create_tenant_tables()


### router registration

app.include_router(order_router, prefix="/api")
app.include_router(tenant_router, prefix='/api')

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/db_connection")
async def db_connection_check(db: Session = Depends(order_get_db)):
    #return {"status": "connected"}  
    result = db.execute(text("SELECT 1"))
    return {
        "message": "Database connection is working",
        "result": result.scalar()
    }