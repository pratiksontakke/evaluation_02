from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from backend.app.models.transaction import Transaction
from backend.app.models.user import User
from backend.app.schemas.transaction import TransactionCreate


class TransactionService:
    def __init__(self):
        pass

    @staticmethod
    def create_transaction(create_transaction: TransactionCreate, db: Session):
        transaction = Transaction(
            transaction_type=create_transaction.transaction_type,
            amount=create_transaction.amount,
            description=create_transaction.description,
            reference_transaction_id=create_transaction.reference_transaction_id,
            recipient_user_id=create_transaction.recipient_user_id,
            user_id=create_transaction.user_id,
            user=create_transaction.user)
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction

    @staticmethod
    def get_transaction_by_id(transaction_id: int, db: Session):
        return db.query(Transaction).filter(Transaction.id == transaction_id).first()

    @staticmethod
    def view_balance(user_id: int, db: Session):
        return db.query(Transaction).filter(Transaction.user_id == user_id).all()

    @staticmethod
    def add_balance(user_id: int, amount: float, db: Session):
        return db.query(User).filter(User.id == user_id).update({"balance": User.balance + amount})

    @staticmethod
    def withdraw_balance(user_id: int, amount: float, db: Session):
        current_balance = db.query(User).filter(User.id == user_id).first().balance
        if current_balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        return db.query(User).filter(User.id == user_id).update({"balance": User.balance - amount})

    @staticmethod
    def transfer_balance(sender_id: int, receiver_id: int, amount: float, db: Session):
        sender = db.query(User).filter(User.id == sender_id).first()
        receiver = db.query(User).filter(User.id == receiver_id).first()
        if sender.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        sender.balance -= amount
        receiver.balance += amount
        db.commit()
        db.refresh(sender)
        db.refresh(receiver)
        return sender, receiver