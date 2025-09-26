"""
Centralized configuration management for the Jetio framework.

This module uses Pydantic's `BaseSettings` to manage application settings,
allowing for configuration via environment variables or a `.env` file. This
approach provides a robust and type-safe way to handle configuration.
"""

# Centralized configuration management using Pydantic's BaseSettings.
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Determine the project root directory (which is two levels up from this file's location)
# config.py -> jetio/ -> project_root/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    """
    Manages application-wide settings.

    It automatically reads from environment variables or a .env file.
    This provides a single source of truth for configuration values like
    database URLs and secret keys.

    Attributes:
        DATABASE_URL: The connection string for the application's database.
                      Defaults to an async SQLite database in the local directory.
        SECRET_KEY: A secret key for cryptographic signing (e.g., for JWTs).
                    It is crucial to override the default value in production.
    """
    DATABASE_URL: str = "sqlite+aiosqlite:///./jetio.db" # Async driver
    SECRET_KEY: str = "a_default_secret_key_that_should_be_changed"
    DOMAIN: str = "http://127.0.0.1:8000"

    # Mail settings moved here for simplicity
    MAIL_MODE: str = "console"  # Can be 'smtp' or 'console'
    MAIL_USERNAME: str = "default_user"
    MAIL_PASSWORD: str = "default_pass"
    MAIL_FROM: str = "default@example.com"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.example.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    MAIL_USE_CREDENTIALS: bool = True
    MAIL_VALIDATE_CERTS: bool = True
    # Pydantic settings configuration.
    # `env_file` specifies a file to load environment variables from.
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env", 
        env_file_encoding='utf-8',
        # Ignore any extra environment variables that don't match fields in this model.
        extra='ignore'
    )

# Creating a single, importable instance of the settings to be used across the application.
settings = Settings()