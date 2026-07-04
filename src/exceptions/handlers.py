from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse
from src.exceptions.custom_exceptions import UserNotFoundException , UserAlreadyExistsException , InvalidCredentialsException, InvalidTokenException



def register_exception_handlers(app: FastAPI):

    @app.exception_handler(UserNotFoundException)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": exc.message}
        )
    
    @app.exception_handler(UserAlreadyExistsException)
    async def user_already_exists_exception_handler(
        request: Request,
        exc: UserAlreadyExistsException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "message": exc.message
            }
        )
    
    @app.exception_handler(InvalidCredentialsException)
    async def invalid_credentials_exception_handler(
        request: Request,
        exc: InvalidCredentialsException
    ):
        return JSONResponse(
            status_code=401,
            content={
                "message": exc.message
            }
        )
    
    @app.exception_handler(InvalidTokenException)
    async def invalid_token_exeption_handler(
        request: Request,
        exc: InvalidTokenException
    ):
        return JSONResponse(
            status_code=401,
            content={"message": exc.message}
        )