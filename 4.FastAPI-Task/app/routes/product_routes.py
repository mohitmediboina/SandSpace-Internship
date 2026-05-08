from fastapi import (
    APIRouter,
    Query
)

from app.schemas.product_schema import (
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductImageSchema,
    StockUpdateSchema
)

from app.services.product_service import (
    ProductService
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
async def create_product(
    payload: ProductCreateSchema
):

    return await ProductService.create_product(
        payload
    )


@router.get("/")
async def get_all_products():

    return await ProductService.get_all_products()


@router.get("/{product_id}")
async def get_single_product(
    product_id: str
):

    return await ProductService.get_single_product(
        product_id
    )


@router.patch("/{product_id}")
async def update_product(
    product_id: str,
    payload: ProductUpdateSchema
):

    return await ProductService.update_product(
        product_id,
        payload
    )


@router.delete("/{product_id}")
async def delete_product(
    product_id: str
):

    return await ProductService.delete_product(
        product_id
    )


@router.get("/search/")
async def search_products(
    keyword: str = Query(...)
):

    return await ProductService.search_products(
        keyword
    )


@router.get("/category/{category}")
async def get_products_by_category(
    category: str
):

    return await ProductService.get_products_by_category(
        category
    )


@router.patch("/{product_id}/stock")
async def update_stock(
    product_id: str,
    payload: StockUpdateSchema
):

    return await ProductService.update_stock(
        product_id,
        payload
    )


@router.patch("/{product_id}/images")
async def update_product_images(
    product_id: str,
    payload: ProductImageSchema
):

    return await ProductService.update_product_images(
        product_id,
        payload
    )


@router.get("/featured/list")
async def get_featured_products():

    return await ProductService.get_featured_products()


@router.get("/active/list")
async def get_active_products():

    return await ProductService.get_active_products()


@router.patch("/deactivate/{product_id}")
async def deactivate_product(
    product_id: str
):

    return await ProductService.deactivate_product(
        product_id
    )