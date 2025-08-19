# src/core/exceptions.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status
from authx.exceptions import MissingTokenError

async def missing_token_exception_handler(request: Request, exc: MissingTokenError):
    """
    Обрабатывает ошибку отсутствия токена от authx.
    Возвращает 401 Unauthorized.
    """
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": "Authentication token is missing"},
    )

# 2. Полностью удаляем обработчик для InvalidTokenError
# async def invalid_token_exception_handler(...): -> УДАЛЕНО

def register_exception_handlers(app: FastAPI) -> None:
    """
    Регистрирует все кастомные обработчики исключений в приложении FastAPI.
    """
    app.add_exception_handler(MissingTokenError, missing_token_exception_handler)
    # 3. Убираем регистрацию лишнего обработчика
    # app.add_exception_handler(InvalidTokenError, ...) -> УДАЛЕНО