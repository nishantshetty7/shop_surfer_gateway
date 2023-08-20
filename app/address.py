from fastapi import HTTPException, Depends
import httpx
from utils import authorize
from fastapi import APIRouter
from main import DATA_API

router = APIRouter()


@router.get("/")
async def get_address(payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    address_url = f"{DATA_API}/address/?user_id={user_id}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(address_url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.post("/add/")
async def add_address(request_data: dict, payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data = {"new_address": request_data}
    request_data["user_id"] = user_id

    address_url = f"{DATA_API}/address/add/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(address_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.patch("/edit/")
async def edit_address(request_data: dict, payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data = {"updated_address": request_data}
    request_data["user_id"] = user_id
    
    address_url = f"{DATA_API}/address/edit/"
    
    async with httpx.AsyncClient() as client:
        response = await client.patch(address_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)