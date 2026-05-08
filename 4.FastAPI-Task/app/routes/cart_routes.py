from fastapi import (
    APIRouter,
    Depends
)

from app.schemas.cart_schema import (
    AddToCartSchema,
    UpdateCartSchema,
    ApplyCouponSchema
)

from app.services.cart_service import (
    CartService
)

from app.dependencies.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/add")
async def add_to_cart(
    payload: AddToCartSchema,
    user=Depends(get_current_user)
):

    return await CartService.add_to_cart(
        user["user_id"],
        payload
    )


@router.get("/")
async def get_cart(
    user=Depends(get_current_user)
):

    return await CartService.get_cart(
        user["user_id"]
    )


@router.patch("/update/{product_id}")
async def update_cart_item(
    product_id: str,
    payload: UpdateCartSchema,
    user=Depends(get_current_user)
):

    return await CartService.update_cart_item(
        user["user_id"],
        product_id,
        payload
    )


@router.delete("/remove/{product_id}")
async def remove_cart_item(
    product_id: str,
    user=Depends(get_current_user)
):

    return await CartService.remove_cart_item(
        user["user_id"],
        product_id
    )


@router.delete("/clear")
async def clear_cart(
    user=Depends(get_current_user)
):

    return await CartService.clear_cart(
        user["user_id"]
    )


@router.get("/count")
async def get_cart_count(
    user=Depends(get_current_user)
):

    return await CartService.get_cart_count(
        user["user_id"]
    )


@router.post("/apply-coupon")
async def apply_coupon(
    payload: ApplyCouponSchema,
    user=Depends(get_current_user)
):

    return await CartService.apply_coupon(
        user["user_id"],
        payload
    )


@router.get("/total")
async def get_cart_total(
    user=Depends(get_current_user)
):

    return await CartService.get_cart_total(
        user["user_id"]
    )