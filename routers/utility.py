from fastapi import APIRouter, Depends, UploadFile, File
from PIL import Image
from utils.security import verify_api_key
from utils.security import limiter
from fastapi import Depends
router = APIRouter()

@router.get('/health')
def health_check():
    return {"status": "healthy",
            "api" : "StegAPI"
            }


@router.get('/formats')
def supported_formats():
    return {
        "supported_formats": [
            "PNG",
        ]
    }
@router.post(
    "/capacity",
    dependencies=[Depends(verify_api_key)]
)
def image_capacity(
    image : UploadFile = File(...)
):
    temp_path = f"uploads/{image.filename}"

    with open(temp_path, "wb") as file:
        file.write(image.file.read())

    img = Image.open(temp_path).convert("RGB")

    width, height = img.size
    total_pixels = width * height
    max_characters = (total_pixels * 3) // 8

    return {
        "filename": image.filename,
        "width": width,
        "height": height,
        "total_pixels": total_pixels,
        "max_characters": max_characters
    }

@router.post("/image-info")
def image_info(
    image: UploadFile = File(...)
):

    temp_path = f"uploads/{image.filename}"

    with open(temp_path, "wb") as file:
        file.write(image.file.read())

    img = Image.open(temp_path)

    width, height = img.size

    return {

        "filename": image.filename,

        "format": img.format,

        "mode": img.mode,

        "width": width,

        "height": height
    }

@router.get("/stats")
def stats():

    import json
    with open("logs/history.json", "r") as file:
        logs = json.load(file)
    
    return {
        "total_operations": len(logs),
        "operations": logs
    }






