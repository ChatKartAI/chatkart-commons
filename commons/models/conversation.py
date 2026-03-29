"""Conversation domain model."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from commons.models.base import MongoBaseModel, utc_now


class Conversation(MongoBaseModel):
    """Persisted conversation metadata."""

    user_id: str
    title: str | None = None
    archived: bool = False
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
