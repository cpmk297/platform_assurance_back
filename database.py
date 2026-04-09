from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


SQL_DB_URL = "postgresql://postgres:02501434@localhost:5432/assurances_db"
engine = create_engine(url= SQL_DB_URL)
SessionLocal = sessionmaker(bind= engine, autoflush= False)
Base = declarative_base()

def get_db():

    db = SessionLocal()

    try: 
        yield db
    finally:
        db.close()