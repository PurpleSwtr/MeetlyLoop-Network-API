# backend/src/components/posts/router.py
from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from .schemas import PostRead, PostCreate

from src.api.dependencies import SessionDep
from src.components.posts.models import PostsORM
from src.components.service.auth_service import security

router = APIRouter(prefix="/posts", tags=["📝 Посты"])

@router.get("/get_posts",
            summary="Получить список постов с авторами",
            response_model=list[PostRead])
async def get_posts(session: SessionDep):
    query = (
        select(PostsORM)
        .options(selectinload(PostsORM.author))
        .order_by(PostsORM.created_at.desc())
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    return posts

@router.post(
        "/create_post",
        summary="Создать пост (только для авторизованных)",
        response_model=PostRead
        )
async def create_new_post(
    session: SessionDep, 
    post_data: PostCreate,
    payload: Any = Depends(security.access_token_required) 
):
    user_id = int(payload.sub)

    new_post_data = post_data.model_dump()
    new_post = PostsORM(**new_post_data, user_id=user_id)
    
    session.add(new_post)
    await session.commit()
    
    await session.refresh(new_post, attribute_names=['author'])
    
    return new_post