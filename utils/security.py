from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

from slowapi import Limiter
from slowapi.util import get_remote_address


API_KEY = "stegapi-secret-key"
api_key_header = APIKeyHeader(

    name="x-api-key",

    auto_error=True
)

async def verify_api_key(

    api_key: str = Security(api_key_header)

):
    if api_key != API_KEY:

        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )


limiter = Limiter(key_func=get_remote_address)


