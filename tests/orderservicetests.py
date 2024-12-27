import pytest
from app.models import Order
from app.datastore import OrderDataStore
from app.service import OrderService

@pytest.fixture
def order_service():
    datastore = OrderDataStore()
    service = OrderService(datastore)
    return service

def test_create_order(order_service):
    new_order = Order(id=1, customer_id=1, product="Laptop", quantity=1, status="Pending")
    created_order = order_service.create_order(new_order)
    assert created_order.product == "Laptop"
    assert created_order.status == "Pending"

def test_cancel_order(order_service):
    order = Order(id=2, customer_id=1, product="Phone", quantity=1, status="Pending")
    order_service.create_order(order)
    success = order_service.cancel_order(2)
    assert success == True
    assert order.status == "Cancelled"
