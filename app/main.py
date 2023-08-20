from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

AUTH_API = "http://localhost:8001/user"
DATA_API = "http://localhost:8002/api"

app = FastAPI()

# Configure CORS settings
origins = [
    "http://localhost:3000",  # Replace with your frontend origin
    "http://localhost:8000",  # If running frontend and backend on separate ports
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

app.include_router(auth.router, prefix="/user", tags=["auth"])
app.include_router(inventory.router, prefix="/api", tags=["inventory"])
app.include_router(cart.router, prefix="/api/cart", tags=["cart"])
app.include_router(orders.router, prefix="/api/order", tags=["order"])
app.include_router(address.router, prefix="/api/address", tags=["address"])


@app.get("/")
async def root():
    return "ShopSurfer API Gateway"