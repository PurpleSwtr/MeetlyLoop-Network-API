# src/models/posts/models.py

from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base

if TYPE_CHECKING:
    from modules.users.model import UsersORM


class PostsORM(Base):
    __tablename__ = "posts" 

    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["UsersORM"] = relationship(back_populates="posts")
    
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    theme: Mapped[str] = mapped_column(String, nullable=True)


    created_at: Mapped[str] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[str] = mapped_column(DateTime, nullable=True)
