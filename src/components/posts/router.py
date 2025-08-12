from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from .schemas import PostRead, PostCreate

from src.api.dependencies import SessionDep
from src.components.posts.models import PostsORM

router = APIRouter()

@router.get("/get_posts",
            tags=["📝 Посты"],
            summary="Получить список постов с авторами",
            response_model=list[PostRead]) # <-- Схема ответа
async def get_posts(session: SessionDep):
    query = (
        select(PostsORM)
        .options(selectinload(PostsORM.author)) # "жадно" загружает связанных авторов
        .order_by(PostsORM.created_at.desc()) # сортирует посты, чтобы новые были сверху
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    print(f"Найденные посты: {posts}")
    return posts


@router.get("/get_posts/user/{user_id}",
            tags=["📝 Посты"],
            summary="Получить список постов пользователя",
            response_model=list[PostRead]) # <-- Схема ответа
async def get_posts_user(session: SessionDep, user_id: int):
    query = (
        select(PostsORM)
        .where(PostsORM.user_id == user_id)
        .options(selectinload(PostsORM.author))
        .order_by(PostsORM.created_at.desc())
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    print(f"Найденные посты: {posts}")
    return posts


@router.post(
        "/create_post",
        tags=["📝 Посты"],
        summary="Создать пост",
        response_model=PostRead
        )
async def create_new_post(session: SessionDep, post_data: PostCreate):
    new_post = PostsORM(**post_data.model_dump())
    session.add(new_post)
    await session.commit()

    query = (
        select(PostsORM)
        .where(PostsORM.id == new_post.id)
        .options(selectinload(PostsORM.author))
    )
    result = await session.execute(query)

    created_post_with_author = result.scalars().one()

    return created_post_with_author