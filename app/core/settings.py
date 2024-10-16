from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

current_directory = Path(__file__).parent
root_directory = Path(__file__).parent.parent.parent
dotenv_path = root_directory / ".env"
load_dotenv(dotenv_path=dotenv_path)


class RDBName(Enum):
    SQLITE = "sqlite+pysqlite"

    def __str__(self):
        return self.value


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True,  # 대소문자 구분 허용
        env_file=".env",  # settings env file name
        env_file_encoding="utf-8",  # setting env file encoding
    )
    # API_V1_STR: str = "/api/v1"

    # 디버그 모드
    # DEBUG: bool = False
    DEBUG: bool = True

    DB_TYPE: str

    # 차후 DB 적용시 입력
    # DB_NAME: str
    # DB_USER: str
    # DB_PASSWORD: str
    # DB_HOST: str
    # DB_PORT: str

    # MLFLOW_TRACKING_URI: str
    # MLFLOW_TRACKING_USERNAME: str
    # MLFLOW_TRACKING_PASSWORD: str
    # MLFLOW_EXPERIMENT_NAME: str

    # OBJECT_STORAGE_URI: str
    # OBJECT_STORAGE_ACCESS_KEY: str
    # OBJECT_STORAGE_SECRET_KEY: str

    # HUGGINGFACE_TOKEN: str

    # MILVUS_DB_USERNAME: str
    # MILVUS_DB_PASSWORD: str
    # MILVUS_DB_HOST: str
    # MILVUS_DB_PORT: str
    # MILVUS_DB_NAME: str
    # MILVUS_ADMIN_PORT: str

    USER_MODELS: dict[str, dict] = {}

    @property
    def get_db_uri(self) -> str:
        """Environment variables로부터 DB 정보를 받아와 URI를 반환 (차후 DB 적용시 입력)"""
        # return f"{self.DB_TYPE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"{self.DB_TYPE}:///sqlite.db"

    @property
    def get_clean_rdb_type(self) -> str:
        return RDBName(self.DB_TYPE).name

    @property
    def user_models(self) -> dict[str, dict]:
        return self.USER_MODELS

    def add_user_model(self, key: str, value: Any):
        self.USER_MODELS[key] = value


@lru_cache
def get_settings():
    return Settings()
