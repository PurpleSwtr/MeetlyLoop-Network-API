# backend/src/components/auth/router.py

# (остальные импорты без изменений)
import asyncio
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from src.api.dependencies import SessionDep
from src.components.users.models import UsersORM
from src.components.auth.schemas import UserLogin
# --- ИЗМЕНЕНИЕ ЗДЕСЬ: импортируем config из auth_service ---
from src.components.service.auth_service import create_token, security, config
from src.components.service.password_hasher import verify_password


router = APIRouter(prefix="/auth", tags=["🔒 Авторизация"])

# (эндпоинт /token остается без изменений)
@router.post("/token", summary="Получить JWT токен (залогиниться)")             
async def login_for_access_token(
    session: SessionDep, 
    user_data: UserLogin,
    response: Response
):
    # ... (код без изменений)
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

    return create_token(user_id=user.id, response=response, remember_me=user_data.remember_me_flag)

# --- НОВЫЙ ЭНДПОИНТ ДЛЯ ВЫХОДА ---
@router.post("/logout", summary="Выйти из системы и удалить cookie")
def logout(response: Response):
    """
    Удаляет httpOnly cookie у пользователя.
    """
    response.delete_cookie(config.JWT_ACCESS_COOKIE_NAME)
    return {"status": "ok", "message": "Successfully logged out"}


# (эндпоинт /protected остается без изменений)
@router.get(path="/protected", dependencies=[Depends(security.access_token_required)])
def protected():
    return {"data": "TOP SECRET"}