# ./backend/Dockerfile

# 1. Используем официальный образ Python
FROM python:3.11-slim

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# 3. Устанавливаем системные зависимости, если они нужны (например, для psycopg2)
# В случае с -slim образом это может понадобиться.
# RUN apt-get update && apt-get install -y ...

# 4. Копируем файл с зависимостями и устанавливаем их (оптимизация кэширования)
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Копируем весь остальной код приложения (Alembic, app и т.д.)
COPY . /code

# Команда запуска будет в docker-compose.yml, чтобы легко управлять миграциями.