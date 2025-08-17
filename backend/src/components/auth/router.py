from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from src.api.dependencies import SessionDep

from src.components.users.models import UsersORM
from src.components.auth.schemas import UserAuth
from src.components.auth.router import create_token, security

router = APIRouter(prefix="/auth")


                            
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
        return create_token(user_id=user.id, response=response)
    else:
        raise HTTPException(status_code=401, detail = "Unauthorized")


    # session.add(new_user)       

@router.get(path="/protected", 
            dependencies=[Depends (security.access_token_required)],
            tags=["🔒 Авторизация"],
            summary="Получить только авторизованным пользователям",)
def protected():

    return {"data": "TOP SECRET"}