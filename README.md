# GCP AI FastAPI Project

This is a learning project for building a FastAPI backend with PostgreSQL and a future Google Cloud AI integration.

## Project flow

```text
HTTP request
    -> app/main.py
    -> /api router
    -> services/order/api/routes/order.py
    -> get_db() session dependency
    -> services/order/repositories/order.py
    -> SQLAlchemy models
    -> PostgreSQL
```

When the application imports the database module, SQLAlchemy creates the `orders` and `order_items` tables if they do not already exist. Each order request is validated by Pydantic schemas, passed to the repository, and committed through the SQLAlchemy session.

## Work completed so far

### Day 1: project foundation

- Created the FastAPI entry point in `app/main.py`.
- Added `uv` project configuration and dependency locking in `app/pyproject.toml` and `app/uv.lock`.
- Added the service-oriented structure under `app/services/`.
- Added health and database connectivity endpoints.
- Configured PostgreSQL with SQLAlchemy and `psycopg2-binary`.
- Added a reusable SQLAlchemy `Base`, engine, session factory, and `get_db()` dependency.

### Order service

- Added `Order` and `OrderItem` SQLAlchemy models.
- Added request and response schemas for orders and items.
- Added repository functions to create and retrieve orders.
- Added these endpoints:
  - `GET /health`
  - `GET /db_connection`
  - `POST /api/orders/`
  - `GET /api/orders/`
  - `GET /api/orders/{order_id}`
- Order creation calculates item amounts, subtotal, discount, and net amount. The current discount is always `0`.

## Current status

The FastAPI and order-service code is in place, but the project is still an early learning implementation:

- PostgreSQL must be running and the configured database must exist before the app can start successfully.
- No automated tests have been added yet.
- Customer service folders exist, but customer endpoints and behavior are not implemented.
- Database configuration is currently hard-coded and should move to environment variables.
- Authentication, migrations, validation rules, error handling, and Google Cloud AI features are still planned.

## Tech stack

- Python 3.11+
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- `psycopg2-binary`
- Uvicorn
- pytest and HTTPX for future tests

## Run the application

From the project root:

```bash
cd app
uv sync
uv run uvicorn main:app --reload
```

Open the interactive API documentation at `http://localhost:8000/docs`.

## Quick checks

```bash
curl http://localhost:8000/health
curl http://localhost:8000/db_connection
```

The database URL currently points to the local PostgreSQL database `gcp_ai_fastapi_order`. Update the connection configuration or create that database before using the database-backed endpoints.

## Next steps

1. Add automated tests for health, database connectivity, and order CRUD behavior.
2. Move the PostgreSQL URL to environment-based configuration.
3. Add migrations and stronger request validation.
4. Implement customer functionality and order error handling.
5. Add the Google Cloud AI integration after the core API is stable.
