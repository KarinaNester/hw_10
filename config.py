from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "fsdkjfgnskjhri2h4iuh3riuhsfdhsfsh9fhsfsdhf8s7fy8sf"
    ALGORITHM: str = "HS256"
    DEBUG: bool = False
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str ='127.0.0.1'
    DB_PORT: int = '5432'
    MAIL_HOST: str = 'smtp.meta.ua'
    MAIL_PORT: int = '465'
    MAIL_STARTTLS: bool = False
    MAIL_USE_SSL: bool = False
    MAIL_USE_TLS: bool = False
    MAIL_HOST_USER: EmailStr = 'example@meta.ua'
    MAIL_HOST_PASSWORD: str = 'secretPassword'
    DEFAULT_FROM_MAIL: EmailStr = 'example@meta.ua'



    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, v: Any):
        if v not in ["HS256", "HS512"]:
            raise ValueError("algorithm must be HS256 or HS512")
        return v


    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Settings()

