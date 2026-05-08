from fastapi import (
    APIRouter,
    Depends
)

from app.schemas.order_schema import (
    CreateOrderSchema,
    UpdateOrderStatusSchema
)

from app.services.order_service import (
    OrderService
)

from app.dependencies.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
async def create_order(
    payload: CreateOrderSchema,
    user=Depends(get_current_user)
):

    return await OrderService.create_order(
        user["user_id"],
        payload
    )


@router.get("/")
async def get_orders(
    user=Depends(get_current_user)
):

    return await OrderService.get_orders(
        user["user_id"]
    )


@router.get("/{order_id}")
async def get_single_order(
    order_id: str
):

    return await OrderService.get_single_order(
        order_id
    )


@router.patch("/{order_id}/cancel")
async def cancel_order(
    order_id: str
):

    return await OrderService.cancel_order(
        order_id
    )


@router.patch("/{order_id}/status")
async def update_order_status(
    order_id: str,
    payload: UpdateOrderStatusSchema
):

    return await OrderService.update_order_status(
        order_id,
        payload
    )


@router.delete("/{order_id}")
async def delete_order(
    order_id: str
):

    return await OrderService.delete_order(
        order_id
    )


@router.get("/pending/list")
async def get_pending_orders():

    return await OrderService.get_pending_orders()


@router.get("/delivered/list")
async def get_delivered_orders():

    return await OrderService.get_delivered_orders()