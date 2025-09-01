from sqlalchemy.orm.session import Session

from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
class UserService:
    def __init__(self):
        pass

    @staticmethod
    def create_user(create_user: UserCreate, db: Session):
        user = User(
            username=create_user.username,
            email=create_user.email,
            password=create_user.password,
            phone_number=create_user.phone_number,
            balance=create_user.balance,
            transactions=[]
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def get_user_by_id(user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()

    