from pydantic import BaseModel
from typing import Optional


class AddToCartSchema(BaseModel):

    product_id: str

    quantity: int


class UpdateCartSchema(BaseModel):

    quantity: int


class ApplyCouponSchema(BaseModel):

    coupon_code: str