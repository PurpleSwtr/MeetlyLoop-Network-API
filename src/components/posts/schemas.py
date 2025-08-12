# src/models/posts/schemas.py
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.components.users.schemas import UserRead

# Схема для отображения поста
class PostRead(BaseModel):
    id: int
    title: str
    description: str
    theme: str | None
    created_at: datetime | None
    
    # Вложенная схема для автора
    author: UserRead

    model_config = ConfigDict(from_attributes=True)