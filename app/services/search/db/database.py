from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg2://postgres:rArjun%4026@localhost:5432/gcp_ai_fastapi_product"
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autoflush=False, 
    autocommit=False,
    bind=engine
    ) 

class Base(DeclarativeBase):
    pass


def create_tables():
    from services.product.core.product_model import Product  # noqa: F401
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()