# backend/tests/test_API.py

import pytest
from httpx import AsyncClient


async def test_get_users_empty(ac: AsyncClient):
    """Тест проверяет, что при пустой БД возвращается пустой список."""
    response = await ac.get("/api/get_users") # <-- Путь теперь должен быть полным, с /api

    assert response.status_code == 200
    assert response.json() == [] # Ожидаем пустой список, т.к. БД чиста