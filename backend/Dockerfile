# ./backend/Dockerfile

# --- СТУПЕНЬ 1: Сборщик Фронтенда (The Frontend Builder) ---
# Мы используем образ Node.js, даем ему псевдоним "frontend-builder"
FROM node:18 AS frontend-builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем ИСХОДНЫЙ код фронтенда в этот временный контейнер
COPY ./frontend /app

# Устанавливаем зависимости и ЗАПУСКАЕМ СБОРКУ
RUN npm install
RUN npm run build


# --- СТУПЕНЬ 2: Финальный Бэкенд-сервер (The Final Backend) ---
# Начинаем с чистого листа, с образа Python, как и раньше
FROM python:3.11-slim

WORKDIR /code

# Копируем зависимости бэкенда и устанавливаем их
COPY ./backend/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Копируем исходный код бэкенда
COPY ./backend /code

# --- ГЛАВНЫЙ МОМЕНТ! ---
# Копируем папку `dist` из контейнера-сборщика (frontend-builder)
# в наш финальный контейнер, где FastAPI сможет ее найти.
COPY --from=frontend-builder /app/dist /code/dist

# Команда запуска остается в docker-compose.yml