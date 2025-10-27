# src/components/users/services.py

import asyncio

from fastapi import HTTPException, status
from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.components.users.models import UsersORM
from src.components.users.schemas import UserCreate
from src.components.service.password_hasher import hash_password

async def create_user_account(
    session: AsyncSession, 
    user_data: UserCreate
) -> UsersORM:
    """
    Сервисная функция для создания аккаунта пользователя.
    """
    query = select(UsersORM).where(
        or_(UsersORM.nickname == user_data.nickname, UsersORM.email == user_data.email)
    )
    if await session.scalar(query):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким никнеймом или email уже существует."
        )

    hashed_password = await asyncio.to_thread(hash_password, user_data.password)
    user_data_for_db = user_data.model_dump(exclude={"password", "remember_me_flag"})
    new_user = UsersORM(
        **user_data_for_db,
        password=hashed_password
    )
    
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)


    return new_user