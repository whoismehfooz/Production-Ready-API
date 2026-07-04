from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.users.controllers import create_user_controller , get_user_by_username_controller , get_all_users_controller, update_user_controller, delete_user_controller
from src.users.schemas import UserResponseSchema, UserSchema
from src.users.models import UserModel
from src.auth.security import get_logged_in_user


user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@user_router.post("/",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
async def register_user_endpoint(user: UserSchema,db: Session = Depends(get_db)):
    return create_user_controller(user, db)



@user_router.get('/{username}', response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_user_endpoint(username: str, db: Session = Depends(get_db), current_user: UserModel = Depends(get_logged_in_user)):
    return get_user_by_username_controller(username, db)


@user_router.get('/', response_model=List[UserResponseSchema], status_code=status.HTTP_200_OK)
async def get_all_users_endpoint( db: Session = Depends(get_db), current_user: UserModel = Depends(get_logged_in_user)):
    return get_all_users_controller(db)


@user_router.put('/{username}', response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def update_user_endpoint(username: str, updated_user: UserSchema, current_user: UserModel = Depends(get_logged_in_user), db: Session = Depends(get_db)):
    return update_user_controller(username, updated_user, db)


@user_router.delete('/{username}', status_code=status.HTTP_200_OK)
async def delete_user_endpoint(username: str, current_user: UserModel = Depends(get_logged_in_user), db: Session = Depends(get_db)):
    delete_user_controller(username, db)
    return {"message": "User deleted successfully"}