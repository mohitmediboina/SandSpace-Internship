from bson import ObjectId

from app.config.database import db


class OrderService:

    @staticmethod
    async def create_order(
        user_id,
        data
    ):

        order = {
            "user_id": user_id,
            "items": [item.dict() for item in data.items],
            "total_amount": data.total_amount,
            "address": data.address,
            "status": "pending"
        }

        result = await db.orders.insert_one(order)

        return {
            "message": "Order created",
            "order_id": str(result.inserted_id)
        }

    @staticmethod
    async def get_orders(user_id):

        orders = []

        async for order in db.orders.find({
            "user_id": user_id
        }):

            order["_id"] = str(order["_id"])

            orders.append(order)

        return orders

    @staticmethod
    async def get_single_order(order_id):

        order = await db.orders.find_one({
            "_id": ObjectId(order_id)
        })

        if not order:
            return {
                "message": "Order not found"
            }

        order["_id"] = str(order["_id"])

        return order

    @staticmethod
    async def cancel_order(order_id):

        await db.orders.update_one(
            {"_id": ObjectId(order_id)},
            {
                "$set": {
                    "status": "cancelled"
                }
            }
        )

        return {
            "message": "Order cancelled"
        }

    @staticmethod
    async def update_order_status(
        order_id,
        data
    ):

        await db.orders.update_one(
            {"_id": ObjectId(order_id)},
            {
                "$set": {
                    "status": data.status
                }
            }
        )

        return {
            "message": "Order status updated"
        }

    @staticmethod
    async def delete_order(order_id):

        await db.orders.delete_one({
            "_id": ObjectId(order_id)
        })

        return {
            "message": "Order deleted"
        }

    @staticmethod
    async def get_pending_orders():

        orders = []

        async for order in db.orders.find({
            "status": "pending"
        }):

            order["_id"] = str(order["_id"])

            orders.append(order)

        return orders

    @staticmethod
    async def get_delivered_orders():

        orders = []

        async for order in db.orders.find({
            "status": "delivered"
        }):

            order["_id"] = str(order["_id"])

            orders.append(order)

        return orders