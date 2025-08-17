# backend/tests/conftest.py

import asyncio
import pytest
from typing import AsyncGenerator
import subprocess

from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# --- Убираем ВСЕ импорты, которые могут запустить Pydantic или FastAPI ---
# from src.core.config import settings <-- УБРАЛИ
# from src.core.database import get_async_session <-- УБРАЛИ
# test_engine = ... <-- УБРАЛИ
# test_async_session_factory = ... <-- УБРАЛИ

# --- 1. Фикстура для применения миграций (остается без изменений) ---
# Alembic запускается в отдельном процессе и сам прочитает .env.test, так что это нормально.
@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    """
    Применяет миграции перед всеми тестами и откатывает после.
    """
    # УБИРАЕМ ЯВНЫЙ ПУТЬ К КОНФИГУ, Т.К. PYTEST ЗАПУСКАЕТСЯ ИЗ ПАПКИ 'backend',
    # ГДЕ alembic.ini ЛЕЖИТ В КОРНЕ.
    print("\nApplying Alembic migrations...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    yield
    print("\nDowngrading Alembic migrations...")
    subprocess.run(["alembic", "downgrade", "base"], check=True)


# --- 2. НОВАЯ фикстура для создания тестового движка ---
@pytest.fixture(scope="session")
def engine():
    """
    Создает и возвращает SQLAlchemy engine для тестовой сессии.
    Импорт settings происходит внутри, когда переменные уже загружены.
    """
    from src.core.config import settings
    return create_async_engine(settings.DATABASE_URL_ASYNC)


# --- 3. Фикстура для сессии теперь ЗАВИСИТ от фикстуры engine ---
@pytest.fixture(scope="function")
async def db_session(engine) -> AsyncGenerator[AsyncSession, None]:
    """
    Создает сессию к тестовой БД для одного теста, используя общий engine.
    """
    # Создаем фабрику сессий на лету, используя готовый движок
    test_async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
    
    async with test_async_session_factory() as session:
        await session.begin_nested()
        yield session
        await session.rollback()


# --- 4. Фикстура для клиента (ac) остается почти такой же ---
@pytest.fixture(scope="function")
async def ac(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """
    Создает тестовый HTTP-клиент и подменяет зависимость сессии.
    """
    from src.main import app
    from src.core.database import get_async_session
    
    async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
        yield db_session

    app.dependency_overrides[get_async_session] = override_get_async_session

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
    
    app.dependency_overrides.clear()


# --- 5. Фикстура для event loop'а (остается без изменений) ---
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()