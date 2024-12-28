from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

ALLOWED_USER_IDS = [934979097, 567345323, 685935327]

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    TG_BOT_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()