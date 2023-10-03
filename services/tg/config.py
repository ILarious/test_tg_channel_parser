from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramSettings(BaseSettings):
    TG_API_ID: int
    TG_API_HASH: str
    TG_STRING_SESSION: str

    model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env", extra='ignore')


tg_settings: TelegramSettings = TelegramSettings()
