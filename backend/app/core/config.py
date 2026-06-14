from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BitForge API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str = "postgresql://bitforge:bitforge@localhost:5432/bitforge"
    REDIS_URL: str = "redis://localhost:6379/0"

    SECRET_KEY: str = "dev_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "ap-south-1"
    S3_BUCKET: str = "bitforge-waveforms"

    GROQ_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
