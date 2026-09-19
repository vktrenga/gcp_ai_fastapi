from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "postgresql://postgres:rArjun%4026@localhost:5432/gcp_ai_fastapi_order"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class Base(DeclarativeBase):
    pass


def create_tables():
    from services.order.core.model import Order, OrderItem  # noqa: F401
    Base.metadata.create_all(bind=engine)


create_tables()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()