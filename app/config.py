import os
from typing import Optional
from functools import lru_cache
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pg_user: str = os.getenv("POSTGRES_USER", "")
    pg_pass: str = os.getenv("POSTGRES_PASSWORD", "")
    pg_host: str = os.getenv("POSTGRES_HOST", "")
    pg_database: str = os.getenv("POSTGRES_DB", "")
    db_url: Optional[PostgresDsn] = f"postgresql://{pg_user}:{pg_pass}@{pg_host}:5432/{pg_database}"

    # rabbit_user: str = os.getenv("RABBITMQ_USER", "")
    # rabbit_pass: str = os.getenv("RABBITMQ_PASSWORD", "")
    # rabbit_host: str = os.getenv("RABBITMQ_HOST", "")

    # client_queue: str = os.getenv("CLIENT_QUEUE", "")
    # network_queue: str = os.getenv("NETWORK_QUEUE", "")


@lru_cache()
def get_settings():
    settings = Settings()
    return settings
