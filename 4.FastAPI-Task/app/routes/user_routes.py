from fastapi import (
    APIRouter,
    Depends
)

from app.schemas.user_schema import (
    CreateUserSchema,
    UpdateUserSchema,
    ChangePasswordSchema
)

from app.services.user_service import (
    UserService
)

from app.dependencies.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
async def create_user(
    payload: CreateUserSchema
):

    return await UserService.create_user(
        payload
    )


@router.get("/")
async def get_all_users():

    return await UserService.get_all_users()


@router.get("/{user_id}")
async def get_single_user(
    user_id: str
):

    return await UserService.get_single_user(
        user_id
    )


@router.patch("/{user_id}")
async def update_user(
    user_id: str,
    payload: UpdateUserSchema
):

    return await UserService.update_user(
        user_id,
        payload
    )


@router.delete("/{user_id}")
async def delete_user(
    user_id: str
):

    return await UserService.delete_user(
        user_id
    )


@router.patch("/change-password")
async def change_password(
    payload: ChangePasswordSchema,
    user=Depends(get_current_user)
):

    return await UserService.change_password(
        user["user_id"],
        payload
    )


@router.patch("/block/{user_id}")
async def block_user(
    user_id: str
):

    return await UserService.block_user(
        user_id
    )


@router.patch("/unblock/{user_id}")
async def unblock_user(
    user_id: str
):

    return await UserService.unblock_user(
        user_id
    )