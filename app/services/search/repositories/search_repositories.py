from datetime import datetime
from typing import Any
import uuid

from pytest import Session
from sqlalchemy import text
from services.search.core.embedding_service import EmbeddingService
from services.search.schemas.search_schemas import SearchResponseSchema
def to_pgvector(embedding: list[float]) -> str:
    return f"ARRAY[{','.join(str(x) for x in embedding)}]::vector"

def search(
    db: Session,
    query: str,
    tenant_id: uuid.UUID,
    top_k: int = 5,
):
    # Generate embedding
    embedding_service = EmbeddingService()
    embedding = embedding_service.create_embedding(query)  # returns list[float]

    # Convert embedding to Postgres vector string
    embedding_str = to_pgvector(embedding)

    # Build SQL with embedding injected as literal
    sql = f"""
        WITH query AS (
            SELECT {embedding_str} AS embedding
        )
        SELECT product_id,
               product_name,
               product_description,
               category,
               brand,
               sku,
               price,
               currency,
               stock_quantity,
               is_active,
               (products.embedding <-> query.embedding) AS score
        FROM products, query
        WHERE tenant_id = :tenant_id
          AND is_active = true
        ORDER BY score ASC
        LIMIT :top_k;
    """

    rows = db.execute(
        text(sql),
        {"tenant_id": str(tenant_id), "top_k": top_k}
    ).fetchall()
    results = []
    for row in rows:
        results.append({
            "product_id": str(row[0]),
            "product_name": row[1],
            "product_description": row[2],
            "category": row[3],
            "brand": row[4],
            "sku": row[5],
            "price": row[6],
            "currency": row[7],
            "stock_quantity": row[8],
            "is_active": row[9],
            "score": float(row[10]),
        })

    return results

    product = db.query(Product).filter(
            Product.tenant_id == tenant_id
    ).all()
    return product