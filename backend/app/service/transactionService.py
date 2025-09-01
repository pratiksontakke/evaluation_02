from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from backend.app.models.transaction import Transaction, TransactionType
from backend.app.models.user import User
from backend.app.schemas.transaction import TransactionCreate


class TransactionService:
    def __init__(self):
        pass

    @staticmethod
    def create_transaction(create_transaction: TransactionCreate, db: Session):
        transaction = Transaction(**create_transaction.model_dump())
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction

    @staticmethod
    def get_transaction_by_id(transaction_id: int, db: Session):
        transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return transaction

    @staticmethod
    def view_balance(user_id: int, db: Session):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user_id": user.id, "balance": user.balance}

    @staticmethod
    def add_balance(user_id: int, amount: float, db: Session):
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be positive")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user.balance += amount
        
        transaction = Transaction(
            user_id=user_id,
            transaction_type=TransactionType.CREDIT,
            amount=amount,
            description=f"Credit of {amount} to account."
        )
        db.add(transaction)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def withdraw_balance(user_id: int, amount: float, db: Session):
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be positive")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if user.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        
        user.balance -= amount
        
        transaction = Transaction(
            user_id=user_id,
            transaction_type=TransactionType.DEBIT,
            amount=amount,
            description=f"Debit of {amount} from account."
        )
        db.add(transaction)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def transfer_balance(sender_id: int, receiver_id: int, amount: float, db: Session):
        if sender_id == receiver_id:
            raise HTTPException(status_code=400, detail="Sender and receiver cannot be the same user")
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be positive")

        sender = db.query(User).filter(User.id == sender_id).first()
        receiver = db.query(User).filter(User.id == receiver_id).first()

        if not sender or not receiver:
            raise HTTPException(status_code=404, detail="Sender or receiver not found")
        if sender.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        
        sender.balance -= amount
        receiver.balance += amount

        # Create transaction for sender
        transfer_out = Transaction(
            user_id=sender_id,
            transaction_type=TransactionType.TRANSFER_OUT,
            amount=amount,
            description=f"Transfer to user {receiver_id}",
            recipient_user_id=receiver_id
        )
        db.add(transfer_out)
        db.flush()  # Use flush to get the ID for the next transaction

        # Create transaction for receiver
        transfer_in = Transaction(
            user_id=receiver_id,
            transaction_type=TransactionType.TRANSFER_IN,
            amount=amount,
            description=f"Transfer from user {sender_id}",
            reference_transaction_id=transfer_out.id
        )
        db.add(transfer_in)
        
        db.commit()
        db.refresh(sender)
        db.refresh(receiver)
        return {"status": "success", "sender_new_balance": sender.balance}