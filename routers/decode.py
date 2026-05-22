from fastapi import APIRouter, HTTPException, UploadFile, File
import shutil
from utils.security import verify_api_key
from utils.security import limiter
from fastapi import Depends
from utils.steg import decode_message
import json
from datetime import datetime

router = APIRouter()

@router.post(
    "/decode",
    dependencies=[Depends(verify_api_key)]
)
async def decode_image(
    image: UploadFile=File(...)
):
    

    if image.content_type != "image/png":
        raise HTTPException(
            status_code=400,
            detail="Only PNG images are supported"
        )
    
    file_location = f"uploads/{image.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    decoded_message = decode_message(file_location)

    with open("logs/history.json", "r") as file:

        logs = json.load(file)
    
    logs.append({
        "type": "decode",
        "filename": image.filename,
        "timestamp": datetime.now().isoformat()
    })

    with open("logs/history.json", "w") as file:
        json.dump(logs, file, indent=4)


    return {
        "message": "Image decoded successfully",
        "filename": image.filename,
        "decoded_message": decoded_message,
    }
