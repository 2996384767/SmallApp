import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


def _cors_origins() -> list[str]:
    value = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    )
    return [origin.strip() for origin in value.split(",") if origin.strip()]


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///aaa_dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = _cors_origins()
