from bson import ObjectId

from app.config.database import db


class ProductService:

    @staticmethod
    async def create_product(data):

        result = await db.products.insert_one(
            data.dict()
        )

        return {
            "message": "Product created",
            "id": str(result.inserted_id)
        }

    @staticmethod
    async def get_all_products():

        products = []

        async for product in db.products.find():

            product["_id"] = str(product["_id"])

            products.append(product)

        return products

    @staticmethod
    async def get_single_product(product_id):

        product = await db.products.find_one({
            "_id": ObjectId(product_id)
        })

        if not product:
            return {
                "message": "Product not found"
            }

        product["_id"] = str(product["_id"])

        return product

    @staticmethod
    async def update_product(
        product_id,
        data
    ):

        update_data = {
            k: v
            for k, v in data.dict().items()
            if v is not None
        }

        await db.products.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": update_data}
        )

        return {
            "message": "Product updated"
        }

    @staticmethod
    async def delete_product(product_id):

        await db.products.delete_one({
            "_id": ObjectId(product_id)
        })

        return {
            "message": "Product deleted"
        }

    @staticmethod
    async def search_products(keyword):

        products = []

        async for product in db.products.find({
            "title": {
                "$regex": keyword,
                "$options": "i"
            }
        }):

            product["_id"] = str(product["_id"])

            products.append(product)

        return products

    @staticmethod
    async def get_products_by_category(category):

        products = []

        async for product in db.products.find({
            "category": category
        }):

            product["_id"] = str(product["_id"])

            products.append(product)

        return products

    @staticmethod
    async def update_stock(
        product_id,
        data
    ):

        await db.products.update_one(
            {"_id": ObjectId(product_id)},
            {
                "$set": {
                    "stock": data.stock
                }
            }
        )

        return {
            "message": "Stock updated"
        }

    @staticmethod
    async def update_product_images(
        product_id,
        data
    ):

        await db.products.update_one(
            {"_id": ObjectId(product_id)},
            {
                "$set": {
                    "images": data.images
                }
            }
        )

        return {
            "message": "Images updated"
        }

    @staticmethod
    async def get_featured_products():

        products = []

        async for product in db.products.find({
            "is_featured": True
        }):

            product["_id"] = str(product["_id"])

            products.append(product)

        return products

    @staticmethod
    async def get_active_products():

        products = []

        async for product in db.products.find({
            "is_active": True
        }):

            product["_id"] = str(product["_id"])

            products.append(product)

        return products

    @staticmethod
    async def deactivate_product(product_id):

        await db.products.update_one(
            {"_id": ObjectId(product_id)},
            {
                "$set": {
                    "is_active": False
                }
            }
        )

        return {
            "message": "Product deactivated"
        }