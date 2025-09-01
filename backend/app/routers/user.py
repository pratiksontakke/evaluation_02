from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from backend.app.db.database import get_session
from backend.app.schemas.user import UserCreate
from backend.app.service.userService import UserService

user_router = APIRouter()

@user_router.get("/")
def testing_user_routes():
    return JSONResponse(status_code=200, content={"status":"inside user_router"})

@user_router.post("/")
def create_user(create_user: UserCreate, db: Session = Depends(get_session)):
    return UserService.create_user(create_user, db);

@user_router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_session)):
    return UserService.get_user_by_id(user_id, db);
    

