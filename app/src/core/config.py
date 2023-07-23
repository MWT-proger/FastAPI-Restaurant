import os
from logging import config as logging_config

from pydantic_settings import BaseSettings

from core.logger import LOGGING
 

class Postgres:
    USERNAME: str = os.getenv("DB_USER")
    PASSWORD: str = os.getenv("DB_PASSWORD")
    HOST: str = os.getenv("DB_HOST")
    PORT: int = os.getenv("DB_PORT")
    DATABASE: str = os.getenv("DB_NAME")


class Settings(BaseSettings):
    DEBUG: bool = (os.getenv('DEBUG', 'False') == 'True')
    BASE_URL: str = ""
    PROJECT_NAME: str = os.getenv("SERVER_NAME", "ugc_service")
    POSTGRES: Postgres = Postgres()


get_settings = Settings()

if get_settings.DEBUG:
    LOGGING["root"]["level"] = "DEBUG"

logging_config.dictConfig(LOGGING)
