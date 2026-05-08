from motor.motor_asyncio import AsyncIOMotorClient

from app.config.settings import (
    MONGO_URL,
    DATABASE_NAME
)

client = AsyncIOMotorClient(MONGO_URL)

db = client[DATABASE_NAME]