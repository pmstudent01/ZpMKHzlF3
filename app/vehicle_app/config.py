"""Application configuration loaded from the environment."""

from __future__ import annotations

import os
from dataclasses import dataclass

try:
    # Optional: load variables from a local .env file if python-dotenv is present.
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # pragma: no cover - dotenv is optional at runtime
    pass


DEFAULT_BASE_URL = "http://localhost:4500"


@dataclass(frozen=True)
class Config:
    """Runtime configuration for the Vehicle Service app."""

    base_url: str = DEFAULT_BASE_URL
    api_key: str | None = None

    @classmethod
    def from_env(cls) -> "Config":
        """Build a Config from environment variables."""
        base_url = os.getenv("VEHICLE_BASE_URL", DEFAULT_BASE_URL).strip()
        api_key = os.getenv("VEHICLE_API_KEY", "").strip() or None
        return cls(base_url=base_url or DEFAULT_BASE_URL, api_key=api_key)
