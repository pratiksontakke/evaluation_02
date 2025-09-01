from re import T
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from backend.app.db.database import get_session
from backend.app.schemas.transaction import TransactionCreate
from backend.app.service.transactionService import TransactionService

transaction_router = APIRouter()

@transaction_router.post("/")
def create_transaction(create_transaction: TransactionCreate, db: Session = Depends(get_session)):
    return TransactionService.create_transaction(create_transaction, db)

@transaction_router.get("/{transaction_id}")
def get_transaction_by_id(transaction_id: int, db: Session = Depends(get_session)):
    return TransactionService.get_transaction_by_id(transaction_id, db)

@transaction_router.get("/view-balance/{user_id}")
def view_balance(user_id: int, db: Session = Depends(get_session)):
    return TransactionService.view_balance(user_id, db)

@transaction_router.post("/add-balance/{user_id}")
def add_balance(user_id: int, amount: float, db: Session = Depends(get_session)):
    return TransactionService.add_balance(user_id, amount, db)

@transaction_router.post("/withdraw-balance/{user_id}")
def withdraw_balance(user_id: int, amount: float, db: Session = Depends(get_session)):
    return TransactionService.withdraw_balance(user_id, amount, db)

@transaction_router.post("/transfer-balance/{sender_id}/{receiver_id}")
def transfer_balance(sender_id: int, receiver_id: int, amount: float, db: Session = Depends(get_session)):
    return TransactionService.transfer_balance(sender_id, receiver_id, amount, db)