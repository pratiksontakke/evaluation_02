from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from backend.app.models.transaction import TransactionType

class Transaction(BaseModel):
    id: int
    transaction_type: TransactionType
    amount: float
    description: Optional[str] = None
    created_at: datetime
    reference_transaction_id: Optional[int] = None
    recipient_user_id: Optional[int] = None
    user_id: int

    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    transaction_type: TransactionType
    amount: float
    description: Optional[str] = None
    reference_transaction_id: Optional[int] = None
    recipient_user_id: Optional[int] = None
    user_id: int