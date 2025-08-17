import asyncio
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from src.api.dependencies import SessionDep

from src.components.users.models import UsersORM
from src.components.auth.schemas import UserLogin

from backend.src.components.service.auth_service import create_token, security
from src.components.service.password_hasher import verify_password


router = APIRouter(prefix="/auth")


                            
@router.post("/login_user",
            tags=["🔒 Авторизация"],
            summary="Залогинить пользователя",)             
async def login_user(
    session: SessionDep, 
    user_data: UserLogin,
    response: Response):
    query = (
        select(UsersORM)
    .where(UsersORM.email == user_data.email))
    user = await session.scalar(query)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Неверный логин или пароль")


    is_password_valid = await asyncio.to_thread(                            
        verify_password, user_data.password ,user.password
    )

    if not is_password_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Неверный логин или пароль")

    return create_token(user_id=user.id, response=response)

    # session.add(new_user)       

@router.get(path="/protected", 
            dependencies=[Depends (security.access_token_required)],
            tags=["🔒 Авторизация"],
            summary="Получить только авторизованным пользователям",)
def protected():

    return {"data": "TOP SECRET"}