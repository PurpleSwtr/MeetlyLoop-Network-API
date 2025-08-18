# src/components/dev/router.py

from fastapi import APIRouter, HTTPException, status
from src.core.database import Base, async_engine
from src.core.config import settings 

router = APIRouter(prefix="/dev")

@router.delete("/reset_database",
        tags=["🚧 [DEV TOOLS ONLY]"],
        summary="УДАЛИТЬ И ПЕРЕСОЗДАТЬ ВСЕ ТАБЛИЦЫ В БАЗЕ",
        )
async def reset_database_dev():
    """
    Полностью очищает базу данных, удаляя все таблицы, и создает их заново.
    **ВНИМАНИЕ: Эта операция необратима и удалит все данные.**
    Доступна только когда `DEV_MODE=True` в настройках окружения.
    """
    if not settings.DEV_MODE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint is only available in development/test mode."
        )

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    return {"status": "ok", "message": "Database has been reset successfully."}