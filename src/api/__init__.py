# __init__.py
from fastapi import APIRouter 
from src.modules.users.router import router as users_router
from src.modules.posts.router import router as posts_router


main_router = APIRouter()

main_router.include_router(users_router)
main_router.include_router(posts_router)

