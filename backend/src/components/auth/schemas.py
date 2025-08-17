# src/models/auth/schemas.py
from typing import Optional
from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str