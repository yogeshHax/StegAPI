from fastapi import FastAPI
import uvicorn
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from routers.decode import router as decode_router
from routers.encode import router as encode_router
from routers.utility import router as utility_router
from utils.steg import text_to_binary
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from utils.security import limiter

app = FastAPI(

    title="StegAPI",

    description="Steganography is the practice of concealing messages in text, images, or other media.",

    version="1.0.0"

)


@app.get('/')
def root():
    return {
    "message": "Welcome to the Steganography API"
    }

@app.get('/health')
def health_check():
    return {"status": "healthy"}

@app.get('/methods')
def get_methods():
    return {
        "methods": [
            "LSB (Least Significant Bit)",
            "XOR Encryption",
            "Binary Encoding",
            "RGB Channel Pixel Manipulation",
            "Steganographic Message Embedding",
            "Steganographic Message Extraction",
            "API Key Authentication",
            "Rate Limiting",
            "JSON Persistence Logging",
            "PNG Image Processing",
            "REST API Architecture",
            "OpenAPI / Swagger Documentation"
        ]
    }


app.include_router(encode_router)

app.include_router(decode_router)
app.include_router(utility_router)
@app.get('/binary')
def binary_endpoint():

    result = text_to_binary("Hello, World!")

    return {"binary": result}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
