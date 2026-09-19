from sqlalchemy.orm import Session
from services.order.core.model import Order, OrderItem
from services.order.schemas.order_schema import OrderSchema, OrderItemSchema

def create_order(db: Session, order_data: OrderSchema):
    db_order = Order(
        customer_id=order_data.customer_id,
        status="PLACED",
        cross_amount=0,
        discount=0,
        net_amount=0
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    cross_amount = 0
    total_discount = 0
    for item in order_data.items:
        amount = item.price * item.quantity
        discount = 0
        total_amount = amount - discount

        total_discount += discount
        cross_amount += amount

        db_item = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price,
            amount=amount,
            discount=discount,
            total_amount=total_amount
        )
        db.add(db_item)

    db_order.discount = total_discount
    db_order.cross_amount = cross_amount
    db_order.net_amount = cross_amount - total_discount
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(Order).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
