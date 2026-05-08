from pydantic import BaseModel
from typing import Optional, List


class ProductCreateSchema(BaseModel):

    title: str

    description: str

    price: float

    stock: int

    category: str

    brand: Optional[str] = None


class ProductUpdateSchema(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    price: Optional[float] = None

    stock: Optional[int] = None

    category: Optional[str] = None

    brand: Optional[str] = None

    is_featured: Optional[bool] = None

    is_active: Optional[bool] = None


class ProductImageSchema(BaseModel):

    images: List[str]


class StockUpdateSchema(BaseModel):

    stock: int