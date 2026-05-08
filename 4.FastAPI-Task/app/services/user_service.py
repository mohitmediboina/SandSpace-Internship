from bson import ObjectId

from app.config.database import db

from app.utils.hashing import (
    hash_password,
    verify_password
)


class UserService:

    @staticmethod
    async def create_user(data):

        existing_user = await db.users.find_one({
            "email": data.email
        })

        if existing_user:
            return {
                "message": "User already exists"
            }

        user = {
            "name": data.name,
            "email": data.email,
            "password": hash_password(data.password),
            "phone": data.phone,
            "is_admin": False,
            "is_blocked": False
        }

        result = await db.users.insert_one(user)

        return {
            "message": "User created",
            "id": str(result.inserted_id)
        }

    @staticmethod
    async def get_all_users():

        users = []

        async for user in db.users.find():

            user["_id"] = str(user["_id"])

            user.pop("password")

            users.append(user)

        return users

    @staticmethod
    async def get_single_user(user_id):

        user = await db.users.find_one({
            "_id": ObjectId(user_id)
        })

        if not user:
            return {
                "message": "User not found"
            }

        user["_id"] = str(user["_id"])

        user.pop("password")

        return user

    @staticmethod
    async def update_user(
        user_id,
        data
    ):

        update_data = {
            k: v
            for k, v in data.dict().items()
            if v is not None
        }

        await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )

        return {
            "message": "User updated"
        }

    @staticmethod
    async def delete_user(user_id):

        await db.users.delete_one({
            "_id": ObjectId(user_id)
        })

        return {
            "message": "User deleted"
        }

    @staticmethod
    async def change_password(
        user_id,
        data
    ):

        user = await db.users.find_one({
            "_id": ObjectId(user_id)
        })

        if not user:
            return {
                "message": "User not found"
            }

        is_valid = verify_password(
            data.old_password,
            user["password"]
        )

        if not is_valid:
            return {
                "message": "Old password incorrect"
            }

        new_password = hash_password(
            data.new_password
        )

        await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "password": new_password
                }
            }
        )

        return {
            "message": "Password changed"
        }

    @staticmethod
    async def block_user(user_id):

        await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "is_blocked": True
                }
            }
        )

        return {
            "message": "User blocked"
        }

    @staticmethod
    async def unblock_user(user_id):

        await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "is_blocked": False
                }
            }
        )

        return {
            "message": "User unblocked"
        }