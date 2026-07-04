from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database.db import Base, engine
from src.core.logging import logger




@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code

    logger.info("Application is starting....")
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized successfully....")

    yield 
    # Shutdown code

    logger.info("Application is shutting down....")
    