# src/models/posts/schemas.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserRead(BaseModel):
    id: int
    nickname: str