from fastapi import HTTPException, Depends
import httpx
from utils import authorize
from fastapi import APIRouter
from main import DATA_API

router = APIRouter()

@router.post("/place/")
async def place_order(request_data: dict, payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data["user_id"] = user_id
    order_url = f"{DATA_API}/order/place/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(order_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)