import datetime
from sqlalchemy import ForeignKey, func
import enum
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.database import Base
from backend.app.models.user import User

class TransactionType(str, enum.Enum):
    CREDIT="credit"
    DEBIT="debit"
    TRANSFER_IN="transfer_in"
    TRANSFER_OUT="transfer_out"

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_type: Mapped[TransactionType]
    amount: Mapped[float]
    description:  Mapped[Optional[str]] 

    reference_transaction_id: Mapped[Optional[int]] = mapped_column(ForeignKey("transactions.id"), nullable=True)
    recipient_user_id: Mapped[Optional[int]] =  mapped_column(ForeignKey("users.id"), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="transactions", foreign_keys=[user_id])

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


# CREATE TABLE transactions (
#     id SERIAL PRIMARY KEY,
#     user_id INTEGER REFERENCES users(id),
#     transaction_type VARCHAR(20) NOT NULL, -- 'CREDIT', 'DEBIT', 'TRANSFER_IN', 'TRANSFER_OUT'
#     amount DECIMAL(10,2) NOT NULL,
#     description TEXT,
#     reference_transaction_id INTEGER REFERENCES transactions(id), -- For linking transfer transactions
#     recipient_user_id INTEGER REFERENCES users(id), -- For transfers
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

