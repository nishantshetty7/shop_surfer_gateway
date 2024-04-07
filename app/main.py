from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from decouple import config

AUTH_API = config("AUTH_API", default="auth_api")
DATA_API = config("DATA_API", default="data_api")

app = FastAPI()

# Configure CORS settings
origins = [
    "http://localhost:3000",  # Replace with your frontend origin
    "http://localhost:8000", # If running frontend and backend on separate ports
    "https://shopsurfer.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import auth
import inventory
import cart
import orders
import address

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(inventory.router, prefix="/data", tags=["inventory"])
app.include_router(cart.router, prefix="/data/cart", tags=["cart"])
app.include_router(orders.router, prefix="/data/order", tags=["order"])
app.include_router(address.router, prefix="/data/address", tags=["address"])


@app.get("/")
async def root():
    return "ShopSurfer API Gateway"