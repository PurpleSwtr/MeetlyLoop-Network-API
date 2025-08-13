from typing import Annotated, AsyncGenerator

from sqlalchemy import String, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import sessionmaker, DeclarativeBase

from .config import settings

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Связи не используются в repr(), поскольку они могут привести к неожиданным загрузкам."""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()): # <--- Правильно: __table__
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"[{col}: {getattr(self, col)}]")
        return f"<{self.__class__.__name__} {', '.join(cols)}>" # <--- Правильно: self.__class__.__name__


sync_engine = create_engine(
    url=settings.DATABASE_URL_SYNC,
    echo=settings.ECHO_MODE_OPTION,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNC,
    echo=settings.ECHO_MODE_OPTION,
)

sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)



# Функция-зависимость для получения сессии в эндпоинтах FastAPI
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
