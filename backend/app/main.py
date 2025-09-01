from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

from backend.app.db.database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/")
def home():
    return RedirectResponse("/docs")

@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"status":"Healthy"})

