from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from src.utils.settings import settings


Base = declarative_base()

engine = create_engine(settings.DB_CONNECTION, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session 
    finally:
        session.close()