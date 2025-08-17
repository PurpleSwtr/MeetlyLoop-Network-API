# src/models/users/router.py

from fastapi import APIRouter
from sqlalchemy import select
from src.api.dependencies import SessionDep
from src.components.users.models import UsersORM
from src.components.users.schemas import UserRead, UserCreate, UserAccount

router = APIRouter()

@router.get("/get_users",
            tags=["👥 Пользователи"],
            summary="Получить список пользователей",
            response_model=list[UserRead] # <-- Схема ответа
            )
async def get_users(session: SessionDep):

    query = select(UsersORM)
    result = await session.execute(query)
    users = result.scalars().all()
    print(f"Найденные пользователи: {users}")
    return users

@router.get("/get_user/{user_id}",
            tags=["👥 Пользователи"],
            summary="Получить пользователя",
            response_model=UserAccount # <-- Схема ответа
            )
async def get_single_user(session: SessionDep, user_id: int):
    query = (
        select(UsersORM)
        .where(UsersORM.id == user_id)
    )
    result = await session.execute(query)
    user = result.scalars().one()
    return user

@router.post(
        "/create_user",
        tags=["👥 Пользователи"],
        summary="Создать пользователя",
        response_model=UserRead
        )
async def create_new_user(
    session: SessionDep, 
    user_data: UserCreate
    ):
    # 1. Превращаем Pydantic-схему в обычный словарь
    user_data_dict = user_data.model_dump()
    
    # 2. "Вытаскиваем" флаг из словаря. Теперь в user_data_dict его нет.
    remember_me = user_data_dict.pop("remember_me_flag")
    
    # --- Вот здесь ты можешь использовать флаг для своей логики ---
    print(f"Флаг 'Запомнить меня' получен: {remember_me}")
    if remember_me:
        print("Нужно будет сгенерировать долгоживущий токен!")
    else:
        print("Нужно будет сгенерировать короткоживущий токен.")
    # -------------------------------------------------------------

    # 3. Создаем объект ORM только с теми данными, что остались в словаре
    new_user = UsersORM(**user_data_dict)
    
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    # 4. ВАЖНО: Добавляем флаг обратно в объект перед отправкой ответа
    # Так как response_model=UserRead требует этот флаг, мы должны его "прикрепить"
    # к объекту new_user перед тем, как FastAPI его вернет.
    setattr(new_user, "remember_me_flag", remember_me)

    return new_user

