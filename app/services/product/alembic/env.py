from alembic import context
from sqlalchemy import create_engine
from db.database import Base, DATABASE_URL  # adjust path

# DATABASE_URL = "postgresql+psycopg2://postgres:rArjun%4026@localhost:5432/gcp_ai_fastapi_product"

engine = create_engine(DATABASE_URL)
target_metadata = Base.metadata

def run_migrations_online():
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
