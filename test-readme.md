# 🚀 MeetlyLoop (Full-Stack Project)

Социальная сеть, разработанная с использованием современного стека технологий, включающего FastAPI для бэкенда и React для фронтенда. Весь проект полностью контейнеризирован с помощью Docker для легкого запуска и масштабирования.

## ✨ Основные технологии

| Категория      | Технология                                                              |
| -------------- | ----------------------------------------------------------------------- |
| **Бэкенд**     | Python 3.11, FastAPI, Uvicorn                                           |
| **Фронтенд**   | React 18, Vite 5, JavaScript (ESM)                                      |
| **База данных**  | PostgreSQL 15, SQLAlchemy 2.0 (ORM), Alembic (миграции)               |
| **Стилизация**   | TailwindCSS 3, Ant Design (AntD)                                        |
| **Окружение**  | Docker, Docker Compose                                                  |
| **Инструменты**  | ESLint (линтинг), Git & GitLab (контроль версий)                        |

---

## 🚀 Быстрый старт

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

## 🛠️ Ежедневная разработка

| Задача                                             | Команда                                            |
| -------------------------------------------------- | -------------------------------------------------- |
| **Запустить все сервисы в фоне**                    | `docker compose up -d`                             |
| **Посмотреть все логи**                              | `docker compose logs -f`                           |
| **Посмотреть логи только бэкенда**                   | `docker compose logs -f backend`                   |
| **Создать новую миграцию БД**                        | `docker compose exec backend alembic revision --autogenerate -m "..."` |
| **Применить миграции БД вручную**                    | `docker compose exec backend alembic upgrade head` |

---

###  Troubleshooting

*   **Ошибка `docker: command not found`?**
    *   Убедитесь, что Docker Desktop запущен.
    *   Полностью перезапустите терминал.
    *   Используйте `docker compose` (без дефиса).

*   **Что-то не работает после изменений?**
    *   Остановите все (`docker compose down`).
    *   Пересоберите и запустите заново: `docker compose up --build`.