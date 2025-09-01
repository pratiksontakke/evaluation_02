import datetime
from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    phone_number: str
    balance: float
    created_at: datetime
    updated_at: datetime
    transactions: Optional[list["Transaction"]] = None 

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    phone_number: str
    balance: Optional[float] = 0

class UserUpdate(BaseModel):
    username: str
    email: str
    password: str
    phone_number: str
    balance: Optional[float] = 0