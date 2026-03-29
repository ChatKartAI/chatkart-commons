from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class ChatMessage(BaseModel):
    id: str = Field(..., alias="_id")
    chat_session_id: str
    sender: str
    content: str
    intent_detected: str | None = None
    entities: dict[str, Any] | None = None
    created_at: datetime = Field(default_factory=utc_now)
