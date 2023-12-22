from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_name: str = ""
    user: str = ""
    host: str = ""
    port: str = ""
    password: str = ""
    secret_key: str = ""
    algorithm: str = ""
    access_token_expire_minutes: int = 0
   
    class Config:
        env_file = ".env"


settings = Settings()
