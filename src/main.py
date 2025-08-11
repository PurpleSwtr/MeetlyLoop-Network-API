# # app/main.py

# import asyncio
# from typing import Annotated

# from fastapi import FastAPI, Depends
# from fastapi.middleware.cors import CORSMiddleware

# from sqlalchemy import select, insert

# from src.core.database import sync_engine, async_engine, sync_session_factory, get_async_session

# from src.models.users.model import UsersORM
# from src.models.posts.model import PostsORM


# from src.api import main_router

# app = FastAPI(
#     title="My Network API",


# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # <-- правильный параметр
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(main_router)

# @app.get("/",
#         tags=["💻 Root"],
#         summary="Главная страничка")
# def read_root():
#     return {"message": "API is running. Welcome!"}

# src/main.py

import asyncio
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from sqlalchemy import select, insert

from src.core.database import sync_engine, async_engine, sync_session_factory, get_async_session

from src.modules.users.model import UsersORM
from src.modules.posts.model import PostsORM

from src.api import main_router

app = FastAPI(
    title="My Network API",
)

# app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)

@app.get("/",
        tags=["💻 Frontend"],
        summary="Главная страница (Frontend)",
        response_class=HTMLResponse)
def read_root():
    try:
        with open("frontend/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Frontend file not found. Please create frontend/index.html</h1>", status_code=404)