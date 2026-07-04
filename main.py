from fastapi import FastAPI

from src.core.lifespan import lifespan
from src.exceptions.handlers import register_exception_handlers
from src.middleware.request_logger import RequestLoggerMiddleware
from src.users.routers import user_router
from src.auth.routers import auth_router

app = FastAPI(
    title="Production Ready API",
    description="A production-grade FastAPI backend featuring authentication, JWT, logging, middleware, exception handling and modular architecture.",
    version="1.0.0",
    lifespan=lifespan,
    contact={
        "name": "Mehfooz",
        "email": "mehfooz.sde@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Production Ready API",
        "version": app.version,
    }


register_exception_handlers(app)

app.add_middleware(RequestLoggerMiddleware)

app.include_router(user_router)
app.include_router(auth_router)