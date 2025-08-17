# 📚 Ваш Персональный Справочник для MeetlyLoop

---

| Технология      | Ссылка на документацию                                            |
| -------------------------- | ----------------------------------------------------------------- |
| **Бэкенд**         |                                                                   |
| FastAPI                    | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)             |
| Pydantic                   | [docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/)    |
| AuthX                      | [authx.yezz.me](https://authx.yezz.me/)                           |
| SQLAlchemy 2.0 (ORM)       | [docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)  |
| Alembic (Миграции)         | [alembic.sqlalchemy.org](https://alembic.sqlalchemy.org/en/latest/) |
| PostgreSQL                 | [www.postgresql.org/docs/15/](https://www.postgresql.org/docs/15/) |
| **Фронтенд**       |                                                                   |
| React                      | [react.dev](https://react.dev/)                                   |
| Vite                       | [vitejs.dev](https://vitejs.dev/)                                 |
| React Router               | [reactrouter.com](https://reactrouter.com/en/main)                |
| Axios                      | [axios-http.com/docs/intro](https://axios-http.com/docs/intro)    |
| Zustand                    | [github.com/pmndrs/zustand](https://github.com/pmndrs/zustand)    |
| Redux Toolkit              | [redux-toolkit.js.org](https://redux-toolkit.js.org/)             |
| **Стилизация**     |                                                                   |
| Tailwind CSS               | [tailwindcss.com/docs](https://tailwindcss.com/docs)              |
| Ant Design (AntD)          | [ant.design/components/overview/](https://ant.design/components/overview/) |
| **DevOps & Infra** |                                                                   |
| Docker (Dockerfile)        | [docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/) |
| Docker Compose             | [docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/) |
| GitLab CI/CD               | [docs.gitlab.com/ee/ci/](https://docs.gitlab.com/ee/ci/)          |
| **Тесты и Линтеры**|                                                                   |
| Pytest (Бэкенд)            | [docs.pytest.org](https://docs.pytest.org)                        |
| Vitest (Фронтенд)          | [vitest.dev](https://vitest.dev/)                                 |
| React Testing Library      | [testing-library.com/docs/react-testing-library/intro/](https://testing-library.com/docs/react-testing-library/intro/) |
| ESLint                     | [eslint.org/docs/latest/](https://eslint.org/docs/latest/)        |
| Rich (Python-скрипты)      | [rich.readthedocs.io/](https://rich.readthedocs.io/en/latest/)    |

---


### 🐍 Бэкенд (Python & FastAPI)

Это ваша основная зона работы на сервере.

1.  **FastAPI (Основная документация)**
    *   **Ссылка:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
    *   **Зачем:** Это ваша "библия". Вам сюда за всем: от создания эндпоинтов и обработки запросов до Dependency Injection (`Depends`), работы с фоновыми задачами и WebSocket. Особенно обратите внимание на раздел про асинхронность.
    *   **Когда обращаться:** Постоянно.

2.  **Pydantic (Валидация данных)**
    *   **Ссылка:** [docs.pydantic.dev](https://docs.pydantic.dev/latest/)
    *   **Зачем:** FastAPI использует Pydantic для всех схем (`BaseModel`). Здесь вы найдете информацию о типах полей, валидаторах, вычисляемых полях (`computed_field`) и настройках моделей (`ConfigDict`). Также важна документация по `pydantic-settings` для управления конфигурацией (`BaseSettings`).
    *   **Когда обращаться:** При создании или изменении любой схемы (`schemas.py`).

3.  **AuthX (Аутентификация)**
    *   **Ссылка:** [authx.yezz.me](https://authx.yezz.me/)
    *   **Зачем:** Вы уже используете эту библиотеку. В документации вы найдете, как правильно настроить JWT-токены, защитить эндпоинты (`security.access_token_required`), управлять cookie и, возможно, реализовать Refresh Tokens.
    *   **Когда обращаться:** При реализации задач из `TODO.md` по аутентификации и авторизации.

4.  **Passlib & Python-jose (Безопасность)**
    *   **Passlib:** [passlib.readthedocs.io](https://passlib.readthedocs.io/en/stable/) — для хеширования и проверки паролей. Вам понадобится раздел про `bcrypt`.
    *   **Python-jose:** [python-jose.readthedocs.io](https://python-jose.readthedocs.io/en/latest/) — для ручного создания и валидации JWT-токенов, если `AuthX` не покроет все ваши нужды.
    *   **Когда обращаться:** Когда будете реализовывать `POST /auth/register` и `POST /auth/login`.

5.  **Uvicorn (ASGI-сервер)**
    *   **Ссылка:** [www.uvicorn.org](https://www.uvicorn.org/)
    *   **Зачем:** Для настройки запуска вашего FastAPI-приложения в production. Здесь есть информация о параметрах командной строки (`--workers`, `--log-level`) и программной настройке.
    *   **Когда обращаться:** При подготовке к развертыванию на сервере (задачи из "Фаза 2: Подготовка к Production").

---

### 🗃️ База данных и ORM

Все, что связано с хранением и извлечением данных.

1.  **SQLAlchemy 2.0 (ORM)**
    *   **Ссылка:** [docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)
    *   **Зачем:** Это ключевая документация. Вам особенно важен раздел **Asyncio (Greenlet) Support**, так как вы используете `async_sessionmaker`. Также изучите, как правильно делать "жадную" загрузку (`selectinload`), настраивать связи (`relationship`) и выполнять сложные запросы.
    *   **Когда обращаться:** При работе с моделями (`models.py`) и любыми запросами к БД.

2.  **Alembic (Миграции)**
    *   **Ссылка:** [alembic.sqlalchemy.org/en/latest/](https://alembic.sqlalchemy.org/en/latest/)
    *   **Зачем:** Для управления изменениями схемы БД. Вам нужно знать, как генерировать миграции (`revision --autogenerate`), применять их (`upgrade head`), а также как решать конфликты или писать миграции вручную (`op.execute()`).
    *   **Когда обращаться:** При любом изменении в `models.py`.

3.  **PostgreSQL (Сама СУБД)**
    *   **Ссылка:** [www.postgresql.org/docs/15/](https://www.postgresql.org/docs/15/)
    *   **Зачем:** Хотя SQLAlchemy многое абстрагирует, вам может понадобиться документация по конкретным типам данных PostgreSQL, функциям (`now()`, `timezone()`), ограничениям (`constraints`) или для оптимизации запросов с помощью `EXPLAIN`.
    *   **Когда обращаться:** При решении сложных проблем с БД или для тонкой настройки.

---

### ⚛️ Фронтенд (React & Vite)

Все, что видит и с чем взаимодействует пользователь.

1.  **React (Новая документация)**
    *   **Ссылка:** [react.dev](https://react.dev/)
    *   **Зачем:** Основной ресурс по React. Особенно важны разделы про хуки (`useState`, `useEffect`, `useContext`), управление состоянием и жизненный цикл компонентов.
    *   **Когда обращаться:** Постоянно при написании React-компонентов.

2.  **Vite (Сборщик проекта)**
    *   **Ссылка:** [vitejs.dev](https://vitejs.dev/)
    *   **Зачем:** Для настройки вашего фронтенд-окружения. Вам понадобится раздел про конфигурацию (`vite.config.js`), работу с переменными окружения (`.env` и префикс `VITE_`), а также настройку прокси для API-запросов.
    *   **Когда обращаться:** При изменении настроек сборки или dev-сервера.

3.  **React Router DOM (Навигация)**
    *   **Ссылка:** [reactrouter.com](https://reactrouter.com/en/main)
    *   **Зачем:** Вам предстоит внедрить роутинг (`TODO.md`). Здесь вы найдете все о `BrowserRouter`, `Routes`, `Route`, `Link`, а также о динамических маршрутах (`/users/:id`) и защищенных роутах.
    *   **Когда обращаться:** В самом начале "Фазы 1: Архитектура и Навигация" на фронтенде.

4.  **Axios (HTTP-клиент)**
    *   **Ссылка:** [axios-http.com/docs/intro](https://axios-http.com/docs/intro)
    *   **Зачем:** Для отправки запросов на ваш бэкенд. Вам нужно будет знать, как создавать инстанс с `baseURL`, отправлять `POST/GET/PATCH/DELETE` запросы и, что очень важно, как использовать **interceptors** для автоматического добавления JWT-токена в заголовки.
    *   **Когда обращаться:** При создании API-слоя и при реализации логики входа/выхода.

5.  **Zustand / Redux Toolkit (Управление состоянием)**
    *   **Zustand:** [github.com/pmndrs/zustand](https://github.com/pmndrs/zustand) — простой и легковесный.
    *   **Redux Toolkit:** [redux-toolkit.js.org](https://redux-toolkit.js.org/) — более мощный и структурированный.
    *   **Зачем:** `TODO.md` упоминает выбор менеджера состояния. Изучите оба, чтобы сделать осознанный выбор. Вам нужно будет хранить состояние пользователя, токен, список постов и т.д.
    *   **Когда обращаться:** На этапе "Управление состоянием" в `TODO.md`.

---

### 🎨 Стилизация и UI-компоненты

Внешний вид вашего приложения.

1.  **Tailwind CSS**
    *   **Ссылка:** [tailwindcss.com/docs](https://tailwindcss.com/docs)
    *   **Зачем:** Ваш основной инструмент для стилизации. В документации есть полный список всех utility-классов. Особенно полезен поиск по сайту. Поскольку вы используете alpha-версию, следите за блогом и релиз-ноутами.
    *   **Когда обращаться:** Постоянно при верстке.

2.  **Ant Design (AntD)**
    *   **Ссылка:** [ant.design/components/overview/](https://ant.design/components/overview/)
    *   **Зачем:** Ваша библиотека готовых UI-компонентов. Вам сюда за примерами использования `<Form>`, `<Input>`, `<Button>`, `<Card>`, `<Segmented>` и других. Обратите внимание на раздел про кастомизацию темы (`ConfigProvider`).
    *   **Когда обращаться:** Когда нужно добавить новый интерактивный элемент в интерфейс.

---

### ⚙️ Инфраструктура и DevOps

Все, что обеспечивает запуск и развертывание проекта.

1.  **Docker**
    *   **Dockerfile reference:** [docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
    *   **Зачем:** Для понимания и модификации ваших `Dockerfile`. Здесь описаны все команды (`FROM`, `COPY`, `RUN`, `CMD` и т.д.), а также лучшие практики (например, многоступенчатые сборки, которые вы могли бы использовать).
    *   **Когда обращаться:** При изменении `Dockerfile`.

2.  **Docker Compose**
    *   **Compose file reference:** [docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
    *   **Зачем:** Для понимания и модификации `docker-compose.yml`. Вам важны секции `services`, `volumes`, `depends_on`, `healthcheck` и `environment`.
    *   **Когда обращаться:** При изменении `docker-compose.yml` или добавлении нового сервиса (например, Nginx).

3.  **GitLab CI/CD**
    *   **Ссылка:** [docs.gitlab.com/ee/ci/](https://docs.gitlab.com/ee/ci/)
    *   **Зачем:** Вам предстоит настроить CI/CD пайплайн (`TODO.md`). В этой документации вы найдете все о синтаксисе `.gitlab-ci.yml`, ключевых словах (`stages`, `script`, `artifacts`), предопределенных переменных и работе с GitLab Container Registry.
    *   **Когда обращаться:** При выполнении задач из раздела "Общее (Проект и DevOps)".

---

### 🛠️ Инструменты и Качество Кода

Линтеры, тесты и вспомогательные утилиты.

1.  **Pytest (Тестирование бэкенда)**
    *   **Ссылка:** [docs.pytest.org](https://docs.pytest.org)
    *   **Зачем:** Для написания тестов на Python. Изучите концепции фикстур (`fixtures`) и параметризации. Для вашего проекта будет очень полезен раздел про тестирование FastAPI с использованием `httpx`.
    *   **Когда обращаться:** Когда начнете писать тесты для API.

2.  **Vitest & React Testing Library (Тестирование фронтенда)**
    *   **Vitest:** [vitest.dev](https://vitest.dev/) — быстрый и совместимый с Vite тест-раннер.
    *   **React Testing Library:** [testing-library.com/docs/react-testing-library/intro/](https://testing-library.com/docs/react-testing-library/intro/) — для тестирования компонентов с точки зрения пользователя.
    *   **Зачем:** Для реализации тестирования на фронтенде, как запланировано в `TODO.md`.
    *   **Когда обращаться:** Когда будете писать тесты для React-компонентов.

3.  **ESLint**
    *   **Ссылка:** [eslint.org/docs/latest/](https://eslint.org/docs/latest/)
    *   **Зачем:** Для настройки правил линтинга в `eslint.config.js`.
    *   **Когда обращаться:** При возникновении ошибок линтера или желании добавить/изменить правила проверки кода.

4.  **Rich (для `commit.py`)**
    *   **Ссылка:** [rich.readthedocs.io/](https://rich.readthedocs.io/en/latest/)
    *   **Зачем:** Вы используете эту библиотеку в своем скрипте `utils/commit.py` для красивого вывода в консоль. Документация поможет вам расширить его функционал (например, добавить таблицы или прогресс-бары).
    *   **Когда обращаться:** При доработке вспомогательных скриптов.