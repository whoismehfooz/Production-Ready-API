from fastapi import APIRouter , Depends , status
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.auth.schemas import TokenSchema , LoginSchema
from src.users.models import UserModel
from src.auth.controllers import login_user_controller
from src.auth.security import get_logged_in_user




auth_router = APIRouter(prefix='/auth', tags=['Authentication'])

@auth_router.post('/login',response_model=TokenSchema, status_code=status.HTTP_200_OK)
async def login_user_endpoint(data: LoginSchema, db: Session = Depends(get_db)):
    return login_user_controller(db,data)


@auth_router.get('/me',status_code=status.HTTP_200_OK)
async def get_logged_in_user_endpoint(current_user: UserModel = Depends(get_logged_in_user)):
    return {
        "id":current_user.id,
        "username":current_user.username,
        "email":current_user.email,
        "is_active":current_user.is_active,
        "crreated_at":current_user.created_at
    }