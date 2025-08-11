# from fastapi import APIRouter
# from sqlalchemy import select, insert

# from src.api.dependencies import SessionDep
# from src.models.posts.model import PostsORM

# router = APIRouter()

# @router.get("/get_posts",
#             tags=["📝 Посты"],
#             summary="Получить список постов")
# async def get_posts(session: SessionDep):
#     query = select(PostsORM)
#     result = await session.execute(query)
#     posts = result.scalars().all()
#     return posts

# @router.post("/create_post",
#             tags=["📝 Посты"],
#             summary="Создать пост")
# async def create_new_post(session: SessionDep, user_id: int, title: str, description: str, theme: str): 
#     stmt = insert(PostsORM).values(
#         user_id=user_id,
#         title=title,
#         description=description,
#         theme=theme
#     )
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "success", "title": title}

from fastapi import APIRouter
from sqlalchemy import select, insert
# --- ДОБАВЛЕННЫЕ ИМПОРТЫ ---
from sqlalchemy.orm import selectinload
from typing import List
from .schemas import PostRead
# --- КОНЕЦ ДОБАВЛЕНИЙ ---

from src.api.dependencies import SessionDep
from src.models.posts.model import PostsORM

router = APIRouter()

# --- ИЗМЕНЕННЫЙ ЭНДПОИНТ ---
@router.get("/get_posts",
            tags=["📝 Посты"],
            summary="Получить список постов с авторами",
            response_model=List[PostRead]) # <-- Указываем схему ответа
async def get_posts(session: SessionDep):
    # .options(selectinload(PostsORM.author)) - "жадно" загружает связанных авторов
    # .order_by(...) - сортирует посты, чтобы новые были сверху
    query = (
        select(PostsORM)
        .options(selectinload(PostsORM.author))
        .order_by(PostsORM.created_at.desc())
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    return posts
# --- КОНЕЦ ИЗМЕНЕНИЙ ---

@router.post("/create_post",
            tags=["📝 Посты"],
            summary="Создать пост")
async def create_new_post(session: SessionDep, user_id: int, title: str, description: str, theme: str | None = None):
    # Добавляем created_at при создании
    from datetime import datetime
    stmt = insert(PostsORM).values(
        user_id=user_id,
        title=title,
        description=description,
        theme=theme,
        created_at=datetime.utcnow() # <-- Добавляем время создания
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": "success", "title": title}