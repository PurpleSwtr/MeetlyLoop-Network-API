# src/models/users/models.py

from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.annotated_types import intpk, created_at, updated_at
from src.core.database import Base

if TYPE_CHECKING:
    from src.components.posts.models import PostsORM

class UsersORM(Base):
    __tablename__ = "users" 

    id: Mapped[intpk]
    nickname: Mapped[str] = mapped_column(String) 
    email: Mapped[str] = mapped_column(String, nullable=True)
    password: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    profile_photo_url: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    repr_cols = ()

    posts: Mapped[list["PostsORM"]] = relationship(back_populates="author")