### 🚀 MeetlyLoop (Full Stack)

Стек:
*   **Бэкенд (`networkAPI_new`):**
    *   **Фреймворк:** FastAPI
    *   **База данных:** PostgreSQL (через `asyncpg` и `psycopg2-binary`)
    *   **ORM:** SQLAlchemy (асинхронный)
    *   **Миграции:** Alembic
    *   **Конфигурация:** Pydantic-Settings (`.env`)
    *   **Инструменты:** `rich` для красивого CLI-скрипта `commit.py` (очень круто!)

*   **Фронтенд (`NetworkFrontend`):**
    *   **Фреймворк:** React
    *   **Сборщик:** Vite
    *   **Стилизация:** TailwindCSS + Ant Design
    *   **Линтинг:** ESLint


## 🚀 Быстрый старт проекта MeetlyLoop

### 1. Предварительные требования

1.  **Установите Git:** [git-scm.com](https://git-scm.com/downloads)
2.  **Установите и запустите Docker Desktop:** [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
    *   *Убедитесь, что Docker Desktop запущен и работает (иконка кита в трее/менюбаре статична).*

### 2. Установка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone <URL_вашего_репозитория>
    cd <название_папки_проекта>
    ```

2.  **Создайте файл конфигурации:**
    *   Найдите в проекте файл `.env.example`.
    *   Скопируйте его и переименуйте копию в `.env`.
    *   *(Если `.env.example` нет, просто создайте файл `.env` и вставьте в него содержимое из шаблона ниже).*

    **Шаблон для `.env`:**
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

### 3. Запуск

1.  **Сборка и запуск контейнеров:**
    *   Откройте терминал в корневой папке проекта.
    *   Выполните команду. **Первый запуск может занять 5-10 минут.**
    ```bash
    docker compose up --build
    ```
    *   Команда запустит все сервисы и будет показывать их логи в реальном времени.

2.  **Проверка:**
    *   **Бэкенд API:** Откройте в браузере `http://localhost:8000/docs`
    *   **Фронтенд:** Откройте в браузере `http://localhost:5173`

### 4. Остановка

*   В терминале, где запущено приложение, нажмите `Ctrl + C`.
*   Чтобы полностью остановить и удалить контейнеры, выполните:
    ```bash
    docker compose down
    ```

---
###  Troubleshooting

*   **Ошибка `docker: command not found`?**
    *   Убедитесь, что Docker Desktop запущен.
    *   Полностью перезапустите терминал.
    *   Используйте `docker compose` (без дефиса).

*   **Что-то не работает?**
    *   Остановите все (`docker compose down`).
    *   Запустите снова, чтобы увидеть свежие логи: `docker compose up`.
    *   Смотрите в терминал — ошибка будет описана там.
