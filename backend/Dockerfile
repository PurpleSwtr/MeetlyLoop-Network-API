# ./backend/Dockerfile

# --- СТУПЕНЬ 1: Сборщик Фронтенда (The Frontend Builder) ---
FROM node:18-alpine AS frontend-builder
WORKDIR /app

# 1. Копируем ТОЛЬКО файлы с зависимостями
COPY frontend/package.json frontend/package-lock.json* ./

# 2. Устанавливаем зависимости. Этот шаг будет кэширован, пока package.json не изменится.
RUN npm install

# 3. Теперь копируем весь остальной код фронтенда
COPY frontend/ ./

# 4. Запускаем сборку. Этот шаг будет выполняться при любом изменении кода.
RUN npm run build


# --- СТУПЕНЬ 2: Финальный Бэкенд-сервер (The Final Backend) ---
FROM python:3.11-slim-bookworm
WORKDIR /code

# По аналогии, сначала зависимости бэкенда
COPY backend/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Затем остальной код бэкенда
COPY backend/ /code/

# Копируем свежесобранный фронтенд из первой ступени
COPY --from=frontend-builder /app/dist /code/dist