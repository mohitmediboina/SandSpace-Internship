from jose import jwt
from datetime import datetime, timedelta

from app.config.settings import (
    JWT_SECRET,
    JWT_ALGORITHM
)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=7)

    to_encode.update({
        "exp": expire
    })

    return jwt.encode(
        to_encode,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )