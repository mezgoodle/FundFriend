from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./sql_app.db"
    test_database_url: str = "sqlite:///./test.db"
    hash_secret_key: str = (
        "60c045d014f9cf451b7b275b7addb35574517aaa610229e05557cad996dbd3ca"
    )
    hash_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
