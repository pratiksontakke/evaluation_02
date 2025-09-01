from datetime import datetime
from pydantic import BaseModel

class Transaction(BaseModel):
    id: int
    transaction_type: str
    amount: float
    description: str
    created_at: datetime
    updated_at: datetime
    reference_transaction_id: int
    recipient_user_id: int
    user_id: int
    user: "User"

    class Config:
        from_attributes = True