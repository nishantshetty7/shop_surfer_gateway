from fastapi import HTTPException, Depends
import httpx
from utils import authorize
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from fastapi.encoders import jsonable_encoder
from main import DATA_API

class Item(BaseModel):
    is_selected: bool
    product: dict
    quantity: int

router = APIRouter()

@router.get("/")
async def get_cart(payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    cart_url = f"{DATA_API}/cart/?user_id={user_id}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(cart_url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.post("/add/")
async def add_cart_item(request_data: dict, payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data = {"cart_item": request_data}
    request_data["user_id"] = user_id

    cart_url = f"{DATA_API}/cart/add/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(cart_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

@router.post("/merge/")
async def merge_cart(request_data: List[Item], payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data = jsonable_encoder(request_data) 
    request_data = {"cart_items": request_data}
    request_data["user_id"] = user_id

    cart_url = f"{DATA_API}/cart/merge/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(cart_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.patch("/update/")
async def update_cart_item(request_data: dict, payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data = {"cart_item": request_data}
    request_data["user_id"] = user_id

    cart_url = f"{DATA_API}/cart/update/"
    
    async with httpx.AsyncClient() as client:
        response = await client.patch(cart_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.delete("/delete/")
async def delete_cart_item(request_data: dict, payload: dict = Depends(authorize)):
    user_id = payload.get("user_id", None)
    request_data["user_id"] = user_id
    cart_url = f"{DATA_API}/cart/delete/"
    
    async with httpx.AsyncClient() as client:
        response = await client.delete(cart_url, params=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
