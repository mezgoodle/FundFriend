from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./sql_app.db"
    test_database_url: str = "sqlite:///./test.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
