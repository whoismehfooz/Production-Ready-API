from fastapi import status
from sqlalchemy.orm import Session
from src.users.models import UserModel
from src.auth.schemas import LoginSchema
from src.exceptions.custom_exceptions import UserNotFoundException , InvalidCredentialsException
from src.auth.security import verify_password, create_access_token




def login_user_controller( db: Session, data: LoginSchema):
    user = db.query(UserModel).filter(UserModel.username == data.username).first()
    if not user:
        raise UserNotFoundException()
    if not verify_password(data.password, user.hashed_password):
        raise InvalidCredentialsException()
    access_token = create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
        }