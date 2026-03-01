from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import time
import random

app = FastAPI(title="ContractIQ Synthetic Demo App", version="1.0.0")

# --- Models ---
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

class Order(BaseModel):
    order_id: str
    user_id: int
    amount: float
    status: str

# --- Synthetic Database ---
users_db = [
    {"id": 1, "name": "Vamsee Srirama", "email": "vamsee@example.com", "age": 35},
    {"id": 2, "name": "Agent X", "email": "agentx@contractiq.ai", "age": 2}
]

orders_db = []

# --- API Endpoints ---

@app.get("/users", response_model=List[User])
async def get_users():
    return users_db

@app.post("/users", response_model=User)
async def create_user(user: User):
    users_db.append(user.dict())
    return user

@app.get("/orders/{user_id}", response_model=List[Order])
async def get_orders(user_id: int):
    user_orders = [o for o in orders_db if o["user_id"] == user_id]
    return user_orders

@app.post("/orders", response_model=Order)
async def create_order(order: Order):
    time.sleep(0.1)
    orders_db.append(order.dict())
    return order

@app.get("/config")
async def get_config():
    return {"version": "1.0.0", "features": ["auth", "billing", "agentic-qe"]}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
