from fastapi import APIRouter

from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema
)

from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register(
    payload: RegisterSchema
):

    return await AuthService.register_user(payload)


@router.post("/login")
async def login(
    payload: LoginSchema
):

    return await AuthService.login_user(payload)