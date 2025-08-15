# src/models/users/router.py

from fastapi import APIRouter
from sqlalchemy import select
from src.api.dependencies import SessionDep
from src.components.users.models import UsersORM
from src.components.users.schemas import UserRead, UserCreate, UserAccount

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
        response_model=UserRead
        )
async def create_new_user(
    session: SessionDep, 
    user_data: UserCreate
    ):
    new_user = UsersORM(**user_data.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

