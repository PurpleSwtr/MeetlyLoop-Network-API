# src/models/posts/models.py

import datetime
from typing import TYPE_CHECKING, Annotated, Dict, List, Optional, Union
from sqlalchemy import ForeignKey, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base
from src.core.annotated_types import intpk, created_at, updated_at
if TYPE_CHECKING:
    from components.users.model import UsersORM

class PostsORM(Base):
    __tablename__ = "posts" 

    id: Mapped[intpk]
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    author: Mapped["UsersORM"] = relationship(back_populates="posts")
    
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    theme: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 

