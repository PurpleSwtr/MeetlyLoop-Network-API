# src/models/posts/schemas.py
from typing import Optional
from pydantic import BaseModel, ConfigDict

class UserRead(BaseModel):
    id: int
    nickname: str

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    nickname: str
    email: str
    password_hash: str
    description: Optional[str]

class UserAccount(BaseModel):
    nickname: str
    email: str
    description: Optional[str]