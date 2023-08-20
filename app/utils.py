from fastapi import HTTPException, Header
import jwt
from decouple import config

SECRET_KEY = config("SECRET_KEY", default="secret")

async def authorize(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Extract the token from the "Bearer" format
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except (jwt.InvalidTokenError, jwt.DecodeError, IndexError):
        raise HTTPException(status_code=400, detail="Token invalid")