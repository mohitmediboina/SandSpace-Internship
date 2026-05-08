from pydantic import (
    BaseModel,
    EmailStr
)

from typing import Optional


class CreateUserSchema(BaseModel):

    name: str

    email: EmailStr

    password: str

    phone: Optional[str] = None


class UpdateUserSchema(BaseModel):

    name: Optional[str] = None

    phone: Optional[str] = None

    profile_image: Optional[str] = None


class ChangePasswordSchema(BaseModel):

    old_password: str

    new_password: str