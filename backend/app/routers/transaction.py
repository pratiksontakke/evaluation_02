from fastapi import APIRouter
from fastapi.responses import JSONResponse

transaction_router = APIRouter()

@transaction_router.get("/")
def testing_transaction_routes():
    return JSONResponse(status_code=200, content={"status":"inside transaction_router"})