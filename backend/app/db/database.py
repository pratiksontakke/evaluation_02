import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import Session

load_dotenv()

SUPABASE_URI = os.dotenv("SUPABASE_URI")

print(f"SUPABASE_URI: {SUPABASE_URI}")

engine = create_engine(SUPABASE_URI)

def get_session():
    with Session(engine) as session:
        yield session

class Base(DeclarativeBase):
    pass

def create_db_and_tables():
    Base.metadata.create_all(engine)