from typing import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

def get_admin():
    admin_id  = os.getenv('ADMIN_ID')
    admin_password = os.getenv('ADMIN_PASSWORD')
    password = os.getenv('PASSWORD')
    return admin_id,admin_password,password

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
