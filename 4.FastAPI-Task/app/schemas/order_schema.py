from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):

    product_id: str

    quantity: int


class CreateOrderSchema(BaseModel):

    items: List[OrderItem]

    total_amount: float

    address: str


class UpdateOrderStatusSchema(BaseModel):

    status: str