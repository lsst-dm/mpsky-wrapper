"""Configuration definition."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from safir.logging import LogLevel, Profile

__all__ = ["Config", "config"]


class Config(BaseSettings):
    """Configuration for mpsky-wrapper."""

    name: str = Field("mpsky-wrapper", title="Name of application")

    path_prefix: str = Field(
        "/mpsky-wrapper", title="URL prefix for application"
    )

    profile: Profile = Field(
        Profile.development, title="Application logging profile"
    )

    log_level: LogLevel = Field(
        LogLevel.INFO, title="Log level of the application's logger"
    )

    model_config = SettingsConfigDict(
        env_prefix="MPSKY_WRAPPER_", case_sensitive=False
    )


config = Config()
"""Configuration for mpsky-wrapper."""
