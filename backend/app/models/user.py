import datetime
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]    
    phone_number: Mapped[str]
    balance: Mapped[float]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]

    transactions: Mapped[List["Transaction"]] = relationship(back_populates="user", cascade="all, delete-orphan")


# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(50) UNIQUE NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     phone_number VARCHAR(15),
#     balance DECIMAL(10,2) DEFAULT 0.00,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
