from app.datastore import OrderDataStore
from app.models import Order
from typing import Optional

class OrderService:
    def __init__(self, datastore: OrderDataStore):
        self.datastore = datastore
    
    def create_order(self, order: Order) -> Order:
        return self.datastore.add_order(order)
    
    def get_order(self, order_id: int) -> Order:
        return self.datastore.get_order_by_id(order_id)
    
    def get_orders_by_customer(self, customer_id: int):
        return [order for order in self.datastore.get_all_orders() if order.customer_id == customer_id]
    
    def update_order(self, order_id: int, updated_order: Order) -> Optional[Order]:
        existing_order = self.datastore.get_order_by_id(order_id)
        if existing_order:
            existing_order.product = updated_order.product
            existing_order.quantity = updated_order.quantity
            existing_order.status = updated_order.status
            return existing_order
        return None

    def cancel_order(self, order_id: int) -> bool:
        return self.datastore.cancel_order(order_id)
