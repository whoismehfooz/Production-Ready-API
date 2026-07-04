from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, UTC
from jose import jwt, JWTError 
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.exceptions.handlers import InvalidTokenException , InvalidCredentialsException
from src.users.models import UserModel
from src.utils.settings import settings
from fastapi import Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

password_hasher = PasswordHash.recommended()

def hash_password(password: str):
    return password_hasher.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return password_hasher.verify(plain_password, hashed_password)


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        username = payload.get("sub")

        if username is None:
            raise InvalidTokenException()

        return payload

    except JWTError:
        raise InvalidTokenException()
    
    
def get_logged_in_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(token)

    username = payload.get("sub")

    user = (
        db.query(UserModel)
        .filter(UserModel.username == username)
        .first()
    )

    if not user:
        raise InvalidCredentialsException()

    return user