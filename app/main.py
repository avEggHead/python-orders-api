from fastapi import FastAPI, HTTPException
from app.service import OrderService
from app.datastore import OrderDataStore
from app.models import Order
from typing import List

app = FastAPI()

# Initialize dependencies
datastore = OrderDataStore()
order_service = OrderService(datastore)

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    created_order = order_service.create_order(order)
    return created_order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    order = order_service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/orders/customer/{customer_id}", response_model=List[Order])
def get_orders_by_customer(customer_id: int):
    orders = order_service.get_orders_by_customer(customer_id)
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this customer")
    return orders

@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, updated_order: Order):
    order = order_service.update_order(order_id, updated_order)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.delete("/orders/{order_id}")
def cancel_order(order_id: int):
    success = order_service.cancel_order(order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found or cannot be cancelled")
    return {"detail": "Order cancelled"}
