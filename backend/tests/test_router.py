# tests/components/users/test_router.py
from httpx import AsyncClient

async def test_create_user(ac: AsyncClient):
    # 1. Подготовка данных
    user_data = {
        "nickname": "testuser",
        "email": "test@example.com",
        "password_hash": "somehash", # Пока просто строка
        "description": "A test user",
        "remember_me_flag": True
    }
    
    # 2. Выполнение запроса
    response = await ac.post("/api/create_user", json=user_data)
    
    # 3. Проверка результата
    assert response.status_code == 200 # Или 201, в зависимости от вашей логики
    
    response_data = response.json()
    assert response_data["nickname"] == "testuser"
    assert "id" in response_data # Убедимся, что ID был присвоен