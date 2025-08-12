# src/models/posts/schemas.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from src.components.users.schemas import UserRead

class PostRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    theme: Optional[str]
    updated_at: Optional[datetime]
    
    # Вложенная схема для автора
    author: UserRead

    model_config = ConfigDict(from_attributes=True)

class PostCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str]
    theme: Optional[str] 