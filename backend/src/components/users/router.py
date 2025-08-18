# src/models/users/router.py

import asyncio
from fastapi import APIRouter, HTTPException, Response, status
from sqlalchemy import or_, select
from src.api.dependencies import SessionDep

from src.components.users.models import UsersORM
from src.components.users.schemas import UserRead, UserCreate, UserAccount

from src.components.service.password_hasher import hash_password

from src.components.service.auth_service import create_token, security

router = APIRouter()

@router.get("/get_users",
            tags=["👥 Пользователи"],
            summary="Получить список пользователей",
            response_model=list[UserRead] # <-- Схема ответа
            )
async def get_users(session: SessionDep):

    query = select(UsersORM)
    result = await session.execute(query)
    users = result.scalars().all()
    print(f"Найденные пользователи: {users}")
    return users

@router.get("/get_user/{user_id}",
            tags=["👥 Пользователи"],
            summary="Получить пользователя",
            response_model=UserAccount # <-- Схема ответа
            )
async def get_single_user(session: SessionDep, user_id: int):
    query = (
        select(UsersORM)
        .where(UsersORM.id == user_id)
    )
    result = await session.execute(query)
    user = result.scalars().one()
    return user

@router.post(
        "/create_user",
        tags=["👥 Пользователи"],
        summary="Создать пользователя",
        response_model=UserRead,
        status_code=status.HTTP_201_CREATED
        )
async def create_new_user(
    session: SessionDep, 
    user_data: UserCreate,
    response: Response
):
    # --- Шаг 1: Проверка на дубликаты (остается без изменений) ---
    query = select(UsersORM).where(
        or_(UsersORM.nickname == user_data.nickname, UsersORM.email == user_data.email)
    )
    if await session.scalar(query):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким никнеймом или email уже существует."
        )

    # --- Шаг 2: Хешируем пароль ---
    hashed_password = await asyncio.to_thread(hash_password, user_data.password)
    
    # --- Шаг 3: Создаем ORM-объект, исключая ненужные поля ---
    # .model_dump(exclude={"password", "remember_me_flag"}) создает словарь
    # без пароля в открытом виде и без флага, который не нужен в БД.
    user_data_for_db = user_data.model_dump(
        exclude={"password", "remember_me_flag"}
    )
    
    new_user = UsersORM(
        **user_data_for_db,
        password=hashed_password # Добавляем хешированный пароль отдельно
    )
    
    # --- Шаг 4: Сохранение в БД (остается без изменений) ---
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    # --- Шаг 5: Создание токена (остается без изменений) ---
    create_token(
        user_id=new_user.id,
        response=response,
        remember_me=user_data.remember_me_flag # Берем флаг напрямую из Pydantic-модели
    )

    return new_user

