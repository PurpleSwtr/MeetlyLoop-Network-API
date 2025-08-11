# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy import URL, create_engine, text
# from sqlalchemy.exc import SQLAlchemyError
# from .config import settings
# from users.models import metadata_obj

from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase


from .config import settings

class Base(DeclarativeBase):
    pass

sync_engine = create_engine(
    url=settings.DATABASE_URL_SYNC,
    echo=True,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNC,
    echo=True,
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

# async def test():
#     async with engine.connect() as conn:
#         res = await conn.execute(text("SELECT 1"))
#         print(f"res: {res.all()=}")

# Функция-зависимость для получения сессии в эндпоинтах FastAPI
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
