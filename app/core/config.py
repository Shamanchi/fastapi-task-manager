from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_url: str = 'postgresql://user:pass@localhost:5432/tasks'
    secret_key: str = 'your_secret_key_change_in_production'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30
    redis_url: str = 'redis://localhost:6379/0'
    log_level: str = 'INFO'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'


settings = Settings()