# src/models/users/models.py

from typing import TYPE_CHECKING
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base

if TYPE_CHECKING:
    from components.posts.model import PostsORM


class UsersORM(Base):
    __tablename__ = "users" 

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String) 
    email: Mapped[str] = mapped_column(String, nullable=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    profile_photo_url: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[str] = mapped_column(DateTime, nullable=True)
    

    # --- ДОБАВЛЕННАЯ СВЯЗЬ ---
    # Создаем relationship, которая "соберет" все посты этого пользователя.
    # back_populates="author" указывает на атрибут 'author' в модели PostsORM
    posts: Mapped[list["PostsORM"]] = relationship(back_populates="author")