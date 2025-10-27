# backend/src/main.py
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse 

from src.api import main_router

from src.core.config import settings
from src.core.exceptions import register_exception_handlers

app = FastAPI(
    title="My Network API",
)
register_exception_handlers(app)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/api")


if not settings.TEST_MODE:
    app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

    @app.get("/", include_in_schema=False,
            tags=["💻 Frontend"],
            summary="Главная страница (Frontend)",
            )
    def read_root():
        return FileResponse("dist/index.html")

    @app.get("/{path:path}", include_in_schema=False)
    async def catch_all(path: str):
        if not path.startswith("api/"):
            return FileResponse("dist/index.html")