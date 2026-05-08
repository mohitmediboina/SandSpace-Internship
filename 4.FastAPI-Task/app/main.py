from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router
from app.routes.product_routes import router as product_router
from app.routes.cart_routes import router as cart_router
from app.routes.order_routes import router as order_router
from app.routes.upload_routes import router as upload_router
from app.routes.admin_routes import router as admin_router

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")
app.include_router(cart_router, prefix="/api/v1")
app.include_router(order_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "API Running"}