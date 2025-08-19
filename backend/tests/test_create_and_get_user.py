# backend/tests/test_create_and_get_user.py

from httpx import AsyncClient

async def test_create_and_get_user(ac: AsyncClient):
    # --- Фаза 1: Создание ---
    user_data = {
        "nickname": "anotheruser", 
        "email": "another@test.com", 
        "password": "testpassword123", # <-- ДОБАВЛЕНО ОБЯЗАТЕЛЬНОЕ ПОЛЕ
        "description": "about me", 
        "remember_me_flag": True,
    }
    # Путь к эндпоинту создания пользователя правильный
    response_create = await ac.post("/api/users/create_user", json=user_data)
    
    # Ожидаем статус 201 Created
    assert response_create.status_code == 201 
    created_user_id = response_create.json()["id"]

    # --- Фаза 2: Получение ---
    # Путь к эндпоинту получения пользователя тоже правильный
    response_get = await ac.get(f"/api/users/get_user/{created_user_id}")
    assert response_get.status_code == 200
    assert response_get.json()["nickname"] == "anotheruser"