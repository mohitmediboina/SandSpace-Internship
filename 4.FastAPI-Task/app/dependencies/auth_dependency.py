from fastapi import Header
from jose import jwt

from app.config.settings import (
    JWT_SECRET,
    JWT_ALGORITHM
)


async def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:
        return None

    token = authorization.split(" ")[1]

    payload = jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM]
    )

    return payload