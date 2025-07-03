from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # app
    app_name: str = "fastapi_project"

    # mysql
    mysql_db_host: str = "locahost"
    mysql_db_port: int = 3306
    mysql_db_user: str = "root"
    mysql_db_pwd: str = "P@Ssw0rd."

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache()
def get_config():
    return Config()
