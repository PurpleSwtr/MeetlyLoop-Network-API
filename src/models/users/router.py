# src/models/users/router.py

from fastapi import APIRouter
from sqlalchemy import select, insert

from src.api.dependencies import SessionDep
from src.models.users.model import UsersORM

router = APIRouter()

@router.get("/get_users",
            tags=["👥 Пользователи"],
            summary="Получить список пользователей")
async def get_users(session: SessionDep):
    query = select(UsersORM)
    result = await session.execute(query)
    users = result.scalars().all()
    return users

@router.post("/create_user",
            tags=["👥 Пользователи"],
            summary="Создать пользователя")
async def create_new_user(session: SessionDep, nickname:str, email:str, password_hash:str, description:str):
    stmt = insert(UsersORM).values(nickname=nickname, email=email, password_hash=password_hash, description=description)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success", "nickname": nickname}

