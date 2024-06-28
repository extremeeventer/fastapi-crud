from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    db_type: str
    db_mode: str
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    jwt_secret: str
    jwt_algorithm: str
    jwt_expire: int

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
