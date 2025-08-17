from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from src.api.dependencies import SessionDep
from src.components.users.models import UsersORM
from src.components.auth.schemas import UserAuth
from authx import AuthX, AuthXConfig
from src.core.config import settings

router = APIRouter(prefix="/auth")

config = AuthXConfig()
config.JWT_SECRET_KEY = settings.JWT_KEY
config.JWT_ACCESS_COOKIE_NAME = settings.JWT_ACCESS_COOKIE
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)
                            
@router.post("/login_user",
            tags=["🔒 Авторизация"],
            summary="Залогинить пользователя",)             
async def login_user(
    session: SessionDep, 
    user_data: UserAuth,
    response: Response):
    query = (
        select(UsersORM)
    .where(UsersORM.nickname == user_data.nickname))
    result = await session.execute(query)
    user = result.scalars().one_or_none()
    if user:
        token = security.create_access_token(uid=str(user.id))
        response.set_cookie(    
            key=config.JWT_ACCESS_COOKIE_NAME,
            value=token,
            max_age=86400,
            httponly=True)   
        return {
            "token":token}
    else:
        raise HTTPException(status_code=401, detail = "Unauthorized")


    # session.add(new_user)       

@router.get(path="/protected", 
            dependencies=[Depends (security.access_token_required)],
            tags=["🔒 Авторизация"],
            summary="Получить только авторизованным пользователям",)
def protected():

    return {"data": "TOP SECRET"}