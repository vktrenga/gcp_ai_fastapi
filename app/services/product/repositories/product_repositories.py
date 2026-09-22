from ast import List
from datetime import datetime
import uuid

from pytest import Session
from services.product.core.product_model import Product
from services.product.core.embedding_service import EmbeddingService
from services.product.schemas.product_schemas import ProductCreateSchema, ProductResponseSchema, ProductUpdateSchema
def create_product(db: Session, data: ProductCreateSchema) -> ProductResponseSchema:

    embedding_text = f"""
            Product: {data.product_name}
            Description: {data.product_description}
            Category: {data.category or ""}
            Brand: {data.brand or ""}
            SKU: {data.sku or ""}
            Price: {data.price or ""}
            Stock: {data.stock_quantity or ""}
        """
    embedding_service =  EmbeddingService ()
    embedding = embedding_service.create_embedding(embedding_text)

    new_product = Product(
        tenant_id=data.tenant_id,
        product_name=data.product_name,
        product_description=data.product_description,
        category=data.category,
        brand=data.brand,
        sku=data.sku,
        price=data.price,
        currency=data.currency,
        stock_quantity=data.stock_quantity,
        is_active=data.is_active,
        embedding=embedding,

    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def update_product(db: Session, product_id, data: ProductUpdateSchema, tenant_id) -> ProductResponseSchema:
    # Find product by ID + tenant
        product = db.query(Product).filter(
            Product.product_id == product_id,
            Product.tenant_id == tenant_id
        ).first()

        if not product:
            raise Exception("Product not found or not owned by tenant")

        # Apply only provided fields
        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)

        product.updated_at = datetime.utcnow()
        embedding_text = f"""
                    Product: {product.product_name}
                    Description: {product.product_description}
                    Category: {product.category or ""}
                    Brand: {product.brand or ""}
                    SKU: {product.sku or ""}
                    Price: {product.price}
                    Stock: {product.stock_quantity or ""}
                """
        embedding_service =  EmbeddingService ()
        embedding = embedding_service.create_embedding(embedding_text)
        print(embedding)
        product.embedding = embedding
        db.commit()
        db.refresh(product)
        return product

def get_product(db: Session, product_id,  tenant_id):
    product = db.query(Product).filter(
            Product.product_id == product_id,
            Product.tenant_id == tenant_id
    ).first()
    return product

def get_list(db: Session, tenant_id):
    product = db.query(Product).filter(
            Product.tenant_id == tenant_id
    ).all()
    return product