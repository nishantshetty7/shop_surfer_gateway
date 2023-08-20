from fastapi import HTTPException
import httpx
from fastapi import APIRouter
from main import DATA_API

router = APIRouter()

@router.get("/products/{slug}/")
async def get_products(slug: str):
    data_url = f"{DATA_API}/products/{slug}/"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(data_url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.get("/product/{slug}/")
async def product_detail(slug: str):
    data_url = f"{DATA_API}/product/{slug}/"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(data_url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.get("/top_categories/")
async def get_top_categories():
    data_url = f"{DATA_API}/top_categories/"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(data_url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        