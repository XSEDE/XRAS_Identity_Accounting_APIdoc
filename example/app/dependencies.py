from fastapi import Header, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey

api_keys = [
    "key"
]  # This is encrypted in the database
API_KEY = "key"
API_KEY_NAME = "XA-API-KEY"
api_key = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

async def get_xa_requester(xa_requester: str = Header(...)):
    if xa_requester != "XRAS":
        raise HTTPException(status_code=403, detail="Invalid XA-REQUESTER value.")


async def get_api_key(api_key_header: str = Security(api_key)):
    #TODO change this to a secure implementation
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Invalid XA-API-KEY.")
