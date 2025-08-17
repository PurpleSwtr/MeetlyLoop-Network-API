# src/models/auth/schemas.py
from typing import Optional
from pydantic import BaseModel


class UserAuth(BaseModel):
    nickname: str
    email: str
    password_hash: str