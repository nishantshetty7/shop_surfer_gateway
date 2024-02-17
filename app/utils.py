from fastapi import HTTPException, Header
import jwt
from decouple import config

AUTH_SECRET_KEY = config("AUTH_SECRET_KEY", default="secret")

async def authorize(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Extract the token from the "Bearer" format
        # print("TOKEN", token)
        payload = jwt.decode(token, AUTH_SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except (jwt.InvalidTokenError, jwt.DecodeError, IndexError):
        raise HTTPException(status_code=400, detail="Token invalid")