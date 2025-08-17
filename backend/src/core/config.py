# core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    ECHO_MODE: bool
    JWT_KEY: str
    JWT_ACCESS_COOKIE: str
    @property
    def DATABASE_URL_ASYNC(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_SYNC(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def ECHO_MODE_OPTION(self) -> bool:
        return self.ECHO_MODE

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
