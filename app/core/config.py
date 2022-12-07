from pydantic import BaseSettings, validator

from app import BASE_DIR


class Settings(BaseSettings):
    ENV: str = None
    API_KEY: str

    class Config:
        env_file = BASE_DIR.joinpath('.env')
        env_file_encoding = 'utf8'
        case_sensitive = True

    @validator("API_KEY", pre=True)
    def value_can_not_be_blank(cls, v: str) -> str:
        if len(v) == 0:
            raise ValueError(v)
        return v

    @classmethod
    def dummy_values(cls):
        return {key: key for key in cls.__fields__.keys()}
