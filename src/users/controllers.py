from sqlalchemy import or_
from sqlalchemy.orm import Session
from src.exceptions.custom_exceptions import UserAlreadyExistsException , UserNotFoundException
from src.users.models import UserModel
from src.users.schemas import UserSchema
from src.auth.security import hash_password




def create_user_controller(user: UserSchema, db: Session):

    existing_user = (db.query(UserModel).filter(or_(UserModel.username == user.username,UserModel.email == user.email)).first())

    if existing_user:
        raise UserAlreadyExistsException()

    hashed_password = hash_password(user.password)

    new_user = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



def get_user_by_username_controller(username: str, db: Session):

    user = db.query(UserModel).filter(UserModel.username == username).first()

    if not user:
        raise UserNotFoundException()
    
    return user


def get_all_users_controller(db: Session):
    all_users = db.query(UserModel).all()

    if not all_users:
        raise UserNotFoundException()
    
    return all_users


def update_user_controller(username: str, updated_user: UserSchema, db: Session):

    user = db.query(UserModel).filter(UserModel.username == username).first()

    if not user:
        raise UserNotFoundException()

    existing_user = db.query(UserModel).filter(or_(UserModel.username == updated_user.username, UserModel.email == updated_user.email)).first()

    if existing_user:
        raise UserAlreadyExistsException()


    user.username = updated_user.username
    user.email = updated_user.email
    user.hashed_password = hash_password(updated_user.password)

    db.commit()
    db.refresh(user)

    return user


def delete_user_controller(username: str, db: Session):
    user = db.query(UserModel).filter(UserModel.username == username).first()

    if not user:
        raise UserNotFoundException()

    db.delete(user)
    db.commit()

    return None