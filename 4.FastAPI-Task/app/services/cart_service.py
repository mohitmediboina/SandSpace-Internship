from bson import ObjectId

from app.config.database import db


class CartService:

    @staticmethod
    async def add_to_cart(
        user_id,
        data
    ):

        cart_item = {
            "user_id": user_id,
            "product_id": data.product_id,
            "quantity": data.quantity
        }

        await db.carts.insert_one(cart_item)

        return {
            "message": "Added to cart"
        }

    @staticmethod
    async def get_cart(user_id):

        cart_items = []

        async for item in db.carts.find({
            "user_id": user_id
        }):

            item["_id"] = str(item["_id"])

            cart_items.append(item)

        return cart_items

    @staticmethod
    async def update_cart_item(
        user_id,
        product_id,
        data
    ):

        await db.carts.update_one(
            {
                "user_id": user_id,
                "product_id": product_id
            },
            {
                "$set": {
                    "quantity": data.quantity
                }
            }
        )

        return {
            "message": "Cart updated"
        }

    @staticmethod
    async def remove_cart_item(
        user_id,
        product_id
    ):

        await db.carts.delete_one({
            "user_id": user_id,
            "product_id": product_id
        })

        return {
            "message": "Item removed"
        }

    @staticmethod
    async def clear_cart(user_id):

        await db.carts.delete_many({
            "user_id": user_id
        })

        return {
            "message": "Cart cleared"
        }

    @staticmethod
    async def get_cart_count(user_id):

        count = await db.carts.count_documents({
            "user_id": user_id
        })

        return {
            "count": count
        }

    @staticmethod
    async def apply_coupon(
        user_id,
        data
    ):

        return {
            "message": f"Coupon {data.coupon_code} applied"
        }

    @staticmethod
    async def get_cart_total(user_id):

        cart_items = []

        total = 0

        async for item in db.carts.find({
            "user_id": user_id
        }):

            product = await db.products.find_one({
                "_id": ObjectId(item["product_id"])
            })

            if product:

                total += (
                    product["price"] * item["quantity"]
                )

                cart_items.append(item)

        return {
            "items": cart_items,
            "total": total
        }