FROM python:3.11-slim

WORKDIR /app

ENV DATABASE_HOST=host.docker.internal

COPY app/pyproject.toml app/uv.lock* ./

RUN pip install --no-cache-dir uv

RUN uv sync --no-dev

COPY app/ .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]