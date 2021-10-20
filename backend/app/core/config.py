from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str
    
    STREAM_SERVER_TOKEN: str
    
    REDIS_URL: str
    DATABASE_URL: str = 'postgresql+asyncpg://midasbot:midasbot@localhost:5432/midasbot'
    
    
    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()