# src/models/posts/schemas.py
from pydantic import BaseModel

class UserRead(BaseModel):
    id: int
    nickname: str

