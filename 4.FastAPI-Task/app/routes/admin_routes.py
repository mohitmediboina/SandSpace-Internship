from fastapi import APIRouter

from app.config.database import db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users")
async def get_users():

    users = []

    async for user in db.users.find():

        user["_id"] = str(user["_id"])

        users.append(user)

    return users