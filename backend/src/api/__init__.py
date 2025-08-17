# __init__.py
from fastapi import APIRouter 
from src.components.users.router import router as users_router
from src.components.posts.router import router as posts_router
from src.components.auth.router import router as auth_router


main_router = APIRouter()

main_router.include_router(users_router)
main_router.include_router(posts_router)
main_router.include_router(auth_router)


