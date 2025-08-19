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
    password: str
    description: Optional[str]
    remember_me_flag: bool


class UserAccount(BaseModel):
    nickname: str
    email: str
    password: str
    description: Optional[str]

class UserPublicProfile(BaseModel):
    id: int
    nickname: str
    description: Optional[str]    
