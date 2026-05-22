from PIL import Image
import json
from datetime import datetime
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from utils.steg import encode_message
import shutil
from fastapi.responses import FileResponse
from fastapi import Depends
from fastapi import Request
from utils.security import verify_api_key
from utils.security import limiter

router = APIRouter()

@router.post(
    "/encode",
    dependencies=[Depends(verify_api_key)]
)

@limiter.limit("5/minute")

async def encode_image(
    request: Request,
    image: UploadFile = File(...),
    secret_message: str = Form(...)
):

   if image.content_type != "image/png":
      raise HTTPException(status_code=400, detail="Only PNG images are supported")

   if len(secret_message.strip()) == 0:
      raise HTTPException(status_code=400, detail="Secret message cannot be empty")

   file_location = f"uploads/{image.filename}"

   with open(file_location, "wb") as buffer:
      shutil.copyfileobj(image.file, buffer)

   img = Image.open(file_location).convert("RGB")
   width, height = img.size
   max_characters = (width * height * 3) // 8

   if len(secret_message) > max_characters:
      raise HTTPException(status_code=400, detail=f"Message too large. Max capacity is {max_characters} characters")

   encoded_image_path = encode_message(
      file_location,
      secret_message
   )

   with open("logs/history.json", "r") as file:

    logs = json.load(file)

   logs.append({

    "type": "encode",

    "filename": image.filename,

    "message_length": len(secret_message),

    "timestamp": str(datetime.now())

   })

   with open("logs/history.json", "w") as file:

    json.dump(logs, file, indent=4)

   return FileResponse(
      path=encoded_image_path,
      media_type="image/png",
      filename="encoded_image.png"
   )


