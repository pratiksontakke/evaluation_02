import datetime
from typing import List
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    phone_number: str
    balance: float
    created_at: datetime
    updated_at: datetime
    transactions: List["Transaction"]

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    phone_number: str
    balance: float = 0
    transactions: List["Transaction"]