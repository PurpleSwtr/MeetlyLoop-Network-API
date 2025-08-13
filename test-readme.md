
# 🚀 MeetlyLoop: Full-Stack Social Network

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-05998B?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-4.0α-38B2AC?style=for-the-badge&logo=tailwindcss&logoColor=white)

Прототип социальной сети, разработанный с использованием современного стека технологий. Весь проект полностью контейнеризирован с помощью Docker, что обеспечивает быстрый запуск и консистентное окружение для разработки.

---

## 📚 Оглавление

- [🚀 MeetlyLoop: Full-Stack Social Network](#-meetlyloop-full-stack-social-network)
  - [📚 Оглавление](#-оглавление)
  - [✨ Основные технологии](#-основные-технологии)
  - [🏁 Быстрый старт](#-быстрый-старт)
    - [1. Предварительные требования](#1-предварительные-требования)
    - [2. Установка](#2-установка)
    - [3. Запуск и Остановка](#3-запуск-и-остановка)
  - [🛠️ Процесс разработки](#️-процесс-разработки)
  - [📁 Структура проекта](#-структура-проекта)
  - [🆘 Решение проблем](#-решение-проблем)

---

## ✨ Основные технологии

| Категория       | Технология                                                     |
| --------------- | -------------------------------------------------------------- |
| **Бэкенд**      | Python 3.11, FastAPI, Uvicorn                                  |
| **Фронтенд**    | React 18, Vite 5, JavaScript (ESM)                             |
| **База данных**   | PostgreSQL 15, SQLAlchemy 2.0 (ORM), Alembic (миграции)      |
| **Стилизация**    | TailwindCSS 4 (alpha), Ant Design (AntD)                       |
| **Окружение**   | Docker, Docker Compose                                         |
| **Инструменты**   | ESLint (линтинг), Git & GitLab (контроль версий)               |

---

## 🏁 Быстрый старт

Это руководство поможет запустить полный стек приложения (Backend + Frontend + База данных) на новой машине.

### 1. Предварительные требования

1.  Установлен [Git](https://git-scm.com/downloads).
2.  Установлен и **запущен** [Docker Desktop](https://www.docker.com/products/docker-desktop/).
    *   *Убедитесь, что Docker Desktop работает (иконка кита в трее/менюбаре статична).*

### 2. Установка

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
    VITE_API_URL=http://localhost:8000
    ```

### 3. Запуск и Остановка

1.  **Сборка и запуск (первый раз):**
    *   Откройте терминал в корневой папке проекта. **Первый запуск может занять 5-10 минут.**
    ```bash
    docker compose up --build
    ```

2.  **Проверка доступности сервисов:**
    *   **Фронтенд:** `http://localhost:5173`
    *   **Бэкенд API (документация):** `http://localhost:8000/docs`

3.  **Остановка проекта:**
    *   В терминале, где запущено приложение, нажмите `Ctrl + C`.
    *   Для полной остановки и удаления контейнеров:
    ```bash
    docker compose down
    ```

---

## 🛠️ Процесс разработки

Используйте эти команды для ежедневной работы с проектом. **Все команды выполняются из корневой папки.**

| Задача                                             | Команда                                                                |
| -------------------------------------------------- | ---------------------------------------------------------------------- |
| **Запустить все сервисы в фоне**                    | `docker compose up -d`                                                 |
| **Посмотреть все логи**                              | `docker compose logs -f`                                               |
| **Посмотреть логи только бэкенда**                   | `docker compose logs -f backend`                                       |
| **Создать новую миграцию БД**                        | `docker compose exec backend alembic revision --autogenerate -m "..."` |
| **Применить миграции БД вручную**                    | `docker compose exec backend //usr/local/bin/alembic upgrade head`     |
| **Запустить только бэкенд и БД**                     | `docker compose up backend`                                            |
| **Открыть Shell внутри контейнера**                  | `docker compose exec backend bash`                                     |

*   **Примечание:** Команда `//usr/local/bin/alembic` использует двойной слэш для совместимости с терминалом Git Bash в Windows.

---

## 📁 Структура проекта

```
.
├── backend/                  # Исходный код FastAPI-приложения
│   ├── alembic/              # Миграции базы данных
│   ├── src/                  # Основной код приложения
│   ├── Dockerfile            # Инструкция по сборке бэкенда
│   └── requirements.txt      # Python-зависимости
│
├── frontend/                 # Исходный код React-приложения
│   ├── src/                  # Основной код и компоненты
│   ├── Dockerfile            # Инструкция по сборке фронтенда
│   └── package.json          # Node.js-зависимости
│
├── .env                      # Локальная конфигурация и секреты (не в Git!)
├── .gitignore                # Файлы, игнорируемые Git
└── docker-compose.yml        # Главный файл для оркестрации всех сервисов
```

---

## 🆘 Решение проблем

Руководство по решению всех проблем, с которыми мы столкнулись во время настройки.

<details>
  <summary><strong>Ошибка `docker: command not found` или `docker-compose: command not found`</strong></summary>
  
  *   **Причина:** Docker Desktop не запущен или терминал "не знает" о нем.
  *   **Решение:**
    1.  Убедитесь, что **Docker Desktop запущен**.
    2.  **Полностью закройте и заново откройте терминал/VS Code.**
    3.  Используйте современный синтаксис `docker compose` (без дефиса).
</details>

<details>
  <summary><strong>Ошибка (Бэкенд): `Connection refused` при подключении к БД</strong></summary>
  
  *   **Причина:** Бэкенд стартует быстрее, чем база данных успевает подготовиться.
  *   **Решение:** В `docker-compose.yml` для сервиса `db` добавлена секция `healthcheck`, а для `backend` — `depends_on: { db: { condition: service_healthy } }`. Это заставляет бэкенд ждать полной готовности БД.
</details>

<details>
  <summary><strong>Ошибка (Бэкенд): `relation "..." does not exist`</strong></summary>
  
  *   **Причина:** Миграции Alembic не были созданы или применены. База данных пуста, а код уже пытается сделать к ней запрос.
  *   **Решение (Процедура "Чистая миграция"):**
    1.  Полная очистка: `docker compose down --volumes`.
    2.  Удалите все `.py` файлы из `backend/alembic/versions/`.
    3.  Временно измените `command` у `backend` в `docker-compose.yml` на `command: tail -f /dev/null`.
    4.  Запустите все: `docker compose up -d`.
    5.  Сгенерируйте миграцию: `docker compose exec backend alembic revision --autogenerate -m "Initial migration"`.
    6.  **Проверьте**, что сгенерированный файл в `versions/` не пустой и содержит `op.create_table(...)`.
    7.  Примените миграцию: `docker compose exec backend //usr/local/bin/alembic upgrade head`.
    8.  Верните `command` в `docker-compose.yml` в рабочее состояние и перезапустите все с `docker compose up --build`.
</details>

<details>
  <summary><strong>Ошибка (Фронтенд): `TypeError: crypto.hash is not a function`</strong></summary>
  
  *   **Причина:** Несовместимость старых версий Vite/его зависимостей с Node.js в Docker.
  *   **Решение:**
    1.  Обновите зависимости в `frontend/package.json` до последних **стабильных** версий (Vite 5, Tailwind 3/4 и т.д.).
    2.  **Удалите локальные `frontend/node_modules` и `frontend/package-lock.json`**, чтобы гарантировать чистую установку.
    3.  В `frontend/Dockerfile` используйте полный образ, а не `alpine` или `slim` (например, `FROM node:18`).
    4.  Пересоберите проект: `docker compose up --build`.
</details>
