from app.config.database import db

from app.utils.hashing import (
    hash_password,
    verify_password
)

from app.utils.jwt import create_access_token


class AuthService:

    @staticmethod
    async def register_user(data):

        existing_user = await db.users.find_one({
            "email": data.email
        })

        if existing_user:
            return {
                "message": "User already exists"
            }

        hashed_password = hash_password(data.password)

        user = {
            "name": data.name,
            "email": data.email,
            "password": hashed_password,
            "is_admin": False
        }

        result = await db.users.insert_one(user)

        return {
            "message": "User created",
            "id": str(result.inserted_id)
        }

    @staticmethod
    async def login_user(data):

        user = await db.users.find_one({
            "email": data.email
        })

        if not user:
            return {
                "message": "Invalid credentials"
            }

        is_valid = verify_password(
            data.password,
            user["password"]
        )

        if not is_valid:
            return {
                "message": "Invalid credentials"
            }

        token = create_access_token({
            "user_id": str(user["_id"])
        })

        return {
            "access_token": token
        }