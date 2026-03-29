"""Message domain model."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from commons.models.base import MongoBaseModel, utc_now


class Message(MongoBaseModel):
    """Persisted message document for a conversation."""

    conversation_id: str
    role: str
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)
