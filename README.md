# GCP AI FastAPI Project

FastAPI backend for tenant-aware product management and product search, backed by PostgreSQL and SQLAlchemy. The project is structured as independent services under `app/services/` and is prepared for Google Cloud AI integrations.

## Project flow

```text
HTTP request
    -> app/main.py
    -> /api router
    -> tenant, product, or search service
    -> service database and repository
    -> PostgreSQL
```

The application creates the tenant and product tables on startup. Product and search requests use the authenticated tenant from the access token so data remains tenant-scoped.

## Current project scope

### Product service

Manages products belonging to the authenticated tenant.

- `POST /api/products/` - create a product
- `GET /api/products/` - list the tenant's products
- `GET /api/products/{product_id}` - retrieve a product
- `PATCH /api/products/{product_id}` - update a product

Products support names, descriptions, categories, brands, SKUs, pricing, inventory, active status, and optional embeddings.

### Search service

Provides authenticated, tenant-scoped product search through:

- `GET /api/search/`

The search service uses the query and tenant identity to retrieve matching products. Embedding support is implemented in the service structure for AI-assisted search.

### Tenant service

Handles tenant registration and authentication:

- `POST /api/tenant/register` - create a tenant
- `POST /api/tenant/login` - obtain an access token

Tenant registration validates email, domain, and password strength. The returned access token is used to authenticate product and search requests.

## Shared endpoints

- `GET /health` - application health check
- `GET /db_connection` - database connectivity check

## Current status

- PostgreSQL must be running and the configured databases must exist before the application can start successfully.
- Database configuration is currently hard-coded and should move to environment variables.
- Authentication and tenant scoping are in place for product and search requests.
- Alembic migration files exist for tenant and product schema changes.
- Automated test coverage is still being expanded.
- Google Cloud AI integration remains a planned extension of the embedding-based search flow.

## Tech stack

- Python 3.11+
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- `psycopg2-binary`
- Uvicorn
- pytest and HTTPX

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

The database URLs currently point to local PostgreSQL databases configured by each service. Update the connection configuration or create the required databases before using the database-backed endpoints.
