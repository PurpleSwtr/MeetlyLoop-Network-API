
# MeetlyLoop

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-05998B?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-DF2F08?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.0-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-1.12-00A98F?style=for-the-badge&logo=alembic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

Прототип социальной сети. 
Весь проект полностью контейнеризирован с помощью Docker-compose. Также была попытка сделать фронтенд на React, но на тот момент у меня были довольно поверхностные знания в этой области, и попытка была не очень удачной. В дальнейшем я перешёл к изучению другого фреймворка (Vue.js).

### Установка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone <URL_вашего_репозитория>
    cd <название_папки_проекта>
    ```

2.  **Создайте файл конфигурации:**
    *   Скопируйте файл `.env.example` в новый файл с именем `.env`.
    *   *(Если `.env.example` нет, создайте `.env` вручную с содержимым ниже).*

    **Содержимое `.env`:**
    ```ini
    # Переменные для локальной разработки
    POSTGRES_USER=myuser
    POSTGRES_PASSWORD=mypassword
    POSTGRES_DB=mydb
    DB_HOST=db
    DB_PORT=5432
    DB_USER=${POSTGRES_USER}
    DB_PASS=${POSTGRES_PASSWORD}
    DB_NAME=${POSTGRES_DB}
    ECHO_MODE=True
    ```

### Запуск и Остановка

1.  **Сборка и запуск (первый раз):**
    *   Откройте терминал в корневой папке проекта. **Первый запуск может занять 5-10 минут.**
    ```bash
    docker compose up --build
    ```

2.  **Проверка доступности сервисов:**
    *   **Бэкенд API (документация):** `http://localhost:8000/docs`

3.  **Остановка проекта:**
    *   В терминале, где запущено приложение, нажмите `Ctrl + C`.
    *   Для полной остановки и удаления контейнеров:
    ```bash
    docker compose down
    ```