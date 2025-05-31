from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Configuration settings
    TOKEN_TELEGRAM: str

    @property
    def telegram_token(self) -> str:
        return self.TOKEN_TELEGRAM
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

settings = Settings()
