"""User domain model."""

from __future__ import annotations

from datetime import datetime

from pydantic import EmailStr, Field

from commons.models.base import MongoBaseModel, utc_now


class User(MongoBaseModel):
    """Persisted user profile document."""

    email: EmailStr
    display_name: str | None = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
    last_login_at: datetime | None = None
