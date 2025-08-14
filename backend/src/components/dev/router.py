from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.api.dependencies import SessionDep

router = APIRouter()
