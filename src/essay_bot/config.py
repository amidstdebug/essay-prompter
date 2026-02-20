from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    telegram_bot_token: str = Field(alias="TELEGRAM_BOT_TOKEN", min_length=10)
    signup_code: str = Field(alias="SIGNUP_CODE", min_length=8)
    database_url: str = Field(alias="DATABASE_URL", default="sqlite:///./var/essay_bot.db")
    app_timezone: str = Field(alias="APP_TIMEZONE", default="UTC")
    friday_send_hour: int = Field(alias="FRIDAY_SEND_HOUR", default=17, ge=0, le=23)


settings = Settings()
