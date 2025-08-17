from httpx import AsyncClient

async def test_create_and_get_user(ac: AsyncClient):
    # --- Фаза 1: Создание ---
    user_data = {"nickname": "anotheruser", "email": "another@test.com", "description": "about me", "remember_me_flag": "true",}
    response_create = await ac.post("/api/create_user", json=user_data)
    assert response_create.status_code == 200
    created_user_id = response_create.json()["id"]

    # --- Фаза 2: Получение ---
    response_get = await ac.get(f"/api/get_user/{created_user_id}")
    assert response_get.status_code == 200
    assert response_get.json()["nickname"] == "anotheruser"