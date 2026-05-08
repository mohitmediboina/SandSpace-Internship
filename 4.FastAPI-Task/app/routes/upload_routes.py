from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

router = APIRouter(
    prefix="/uploads",
    tags=["Uploads"]
)


@router.post("/product-image")
async def upload_product_image(
    file: UploadFile = File(...)
):

    file_path = f"app/uploads/products/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "filename": file.filename
    }