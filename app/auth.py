from fastapi import HTTPException, Request, Response
import httpx
from fastapi import APIRouter
from main import AUTH_API

router = APIRouter()

@router.post("/login")
async def login(payload: dict):
    login_url = f"{AUTH_API}/login/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(login_url, json=payload)
        
        if response.status_code == 200:
            # Extract the specific cookie from the response
            refresh_token = response.cookies.get("jwt")
            
            # Create a response with the specific cookie set as HTTP-only and expires in one hour
            api_response = Response(content=response.text)
            api_response.set_cookie(
                key="jwt",
                value=refresh_token,
                httponly=True,
                expires=3600, 
                secure=True,
                samesite=None
            )
            
            return api_response
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
@router.post("/google/login")
async def google_login(payload: dict):
    login_url = f"{AUTH_API}/google/login/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(login_url, json=payload)
        
        if response.status_code == 200:
            # Extract the specific cookie from the response
            refresh_token = response.cookies.get("jwt")
            
            # Create a response with the specific cookie set as HTTP-only and expires in one hour
            api_response = Response(content=response.text)
            api_response.set_cookie(
                key="jwt",
                value=refresh_token,
                httponly=True,
                expires=3600, 
                secure=True,
                samesite=None
            )
            
            return api_response
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
@router.get("/login/refresh")
async def refresh_access_token(request: Request):
    cookies = request.cookies
    refresh_url = f"{AUTH_API}/login/refresh/"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(refresh_url, cookies=cookies)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
@router.post("/register")
async def register(request_data: dict):
    register_url = f"{AUTH_API}/register/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(register_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
@router.get("/logout")
async def logout(request: Request):
    refresh_token = request.cookies.get("jwt", None)
    if not refresh_token:
        return Response(status_code=204)
    
    try:
        response = Response(status_code=204)
        response.delete_cookie('jwt')
        return response
    except Exception as e:
        return Response(content=str(e), status_code=500)
    
@router.post("/verify/register")
async def verify_register(request_data: dict):
    verify_url = f"{AUTH_API}/verify/register/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(verify_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
@router.post("/resend/register")
async def resend_register(request_data: dict):
    resend_url = f"{AUTH_API}/resend/register/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(resend_url, json=request_data)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())