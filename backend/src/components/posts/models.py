
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base
from src.core.annotated_types import intpk, created_at, updated_at

if TYPE_CHECKING:
    from src.components.users.models import UsersORM

class PostsORM(Base):
    __tablename__ = "posts" 

    id: Mapped[intpk]
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String, nullable=True)
    theme: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at] 

    repr_cols = ("created_at", "updated_at")

    author: Mapped["UsersORM"] = relationship(back_populates="posts")

   