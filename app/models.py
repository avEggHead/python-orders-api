from pydantic import BaseModel

class Order(BaseModel):
    id: int
    customer_id: int
    product: str
    quantity: int
    status: str
