from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Churn Prediction API"
    APP_ENV: str = "dev"  # dev | staging | prod
    API_V1_PREFIX: str = "/api/v1"
    ALLOWED_ORIGINS: list[str] = ["*"]  # tighten in prod
    MODEL_DIR: str = "models"
    MODEL_FILE: str = "random_forest_tuned.pkl"
    SCALER_FILE: str = "scaler.pkl"
    XCOLUMNS_FILE: str = "X_columns.pkl"
    API_KEY: str | None = None  # optional simple auth
    ENABLE_METRICS: bool = True

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
