from fastapi import APIRouter
from fastapi.responses import JSONResponse

user_router = APIRouter()

@user_router.get("/")
def testing_user_routes():
    return JSONResponse(status_code=200, content={"status":"inside user_router"})