from typing import List, Optional
from app.models import Order

class OrderDataStore:
    def __init__(self):
        # In-memory mock database
        self.orders = []
    
    def get_all_orders(self) -> List[Order]:
        return self.orders
    
    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return next((order for order in self.orders if order.id == order_id), None)
    
    def add_order(self, order: Order) -> Order:
        self.orders.append(order)
        return order
    
    def cancel_order(self, order_id: int) -> bool:
        order = self.get_order_by_id(order_id)
        if order and order.status == "Pending":
            order.status = "Cancelled"
            return True
        return False
