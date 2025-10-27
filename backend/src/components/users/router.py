# src/models/users/router.py

import asyncio
from typing import Any
from authx import TokenPayload
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import or_, select
from src.api.dependencies import SessionDep

from src.components.users.models import UsersORM
from src.components.users.schemas import UserRead, UserCreate, UserAccount, UserPublicProfile
from src.components.users import services as user_services
from src.components.service.password_hasher import hash_password

from src.components.service.auth_service import create_token, security


router = APIRouter(prefix="/users", tags=["👥 Пользователи"])

@router.get("/get_users",
            summary="Получить список пользователей",
            response_model=list[UserRead]
            )
async def get_users(session: SessionDep):

    query = select(UsersORM)
    result = await session.execute(query)
    users = result.scalars().all()
    print(f"Найденные пользователи: {users}")
    return users

# FIXME:
"""
    Нельзя в целом получать так пользователя... Так его может получить кто угодно, что в целом опасно...
"""
@router.get("/get_user/{user_id}",
            summary="Получить пользователя",
            response_model=UserPublicProfile
            )
async def get_single_user(session: SessionDep, user_id: int):
    query = (
        select(UsersORM)
        .where(UsersORM.id == user_id)
    )
    result = await session.execute(query)
    user = result.scalars().one()
    return user


@router.get("/me", 
            summary="Получить информацию о текущем пользователе",
            response_model=UserPublicProfile
            )
async def get_current_user(
    session: SessionDep,
    payload: Any = Depends(security.access_token_required)
):
    """
    Возвращает информацию о пользователе, чей JWT токен был предоставлен.
    """
    user_id_from_token = payload.sub
    
    user_id = int(user_id_from_token)
    
    query = select(UsersORM).where(UsersORM.id == user_id)
    user = await session.scalar(query)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден."
        )
        
    return user

@router.post(
        "/create_user",
        summary="Создать пользователя",
        response_model=UserRead,
        status_code=status.HTTP_201_CREATED
        )
async def create_new_user(
    session: SessionDep, 
    user_data: UserCreate,
):
    new_user = await user_services.create_user_account(
        session=session, user_data=user_data
    )
    return new_user

