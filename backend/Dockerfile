# ./backend/Dockerfile

FROM node:18-alpine AS frontend-builder
WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* ./

RUN npm install

COPY frontend/ ./

RUN npm run build


FROM python:3.11-slim-bookworm
WORKDIR /code

COPY backend/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY backend/ /code/

COPY --from=frontend-builder /app/dist /code/dist