# Development notes

## Install and sync dependencies

Run these commands from the `app` directory:

```bash
uv sync
```

To add a new dependency, use `uv add package-name`. The dependency is recorded in `pyproject.toml` and `uv.lock`.

## Run the API

```bash
uv run uvicorn main:app --reload
```

The API is available at `http://localhost:8000`. FastAPI's interactive documentation is at `http://localhost:8000/docs`.

## Database prerequisite

The application currently connects to the local PostgreSQL database `gcp_ai_fastapi_order`. Start PostgreSQL and create that database before running the application. Importing the database module creates the `orders` and `order_items` tables when they are missing.

## Useful checks

```bash
uv run pytest
uv run python -m compileall .
```