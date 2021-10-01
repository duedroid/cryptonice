from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'CryptoNice API'
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str
    REDIS_URL: str
    DATABASE_URL: str = 'sqlite+aiosqlite:///./data/db.sqlite3'
    
    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()