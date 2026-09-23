SELECT format('CREATE DATABASE %I', database_name)
FROM (VALUES
  ('gcp_ai_fastapi_customer'),
  ('gcp_ai_fastapi_order'),
  ('gcp_ai_fastapi_product'),
  ('gcp_ai_fastapi_tenant')
) AS databases(database_name)
WHERE NOT EXISTS (
  SELECT FROM pg_database WHERE datname = database_name
)
\gexec

\connect gcp_ai_fastapi_customer
CREATE EXTENSION IF NOT EXISTS vector;

\connect gcp_ai_fastapi_order
CREATE EXTENSION IF NOT EXISTS vector;

\connect gcp_ai_fastapi_product
CREATE EXTENSION IF NOT EXISTS vector;

\connect gcp_ai_fastapi_tenant
CREATE EXTENSION IF NOT EXISTS vector;