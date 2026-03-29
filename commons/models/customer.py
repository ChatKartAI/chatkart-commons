from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class Customer(BaseModel):
    id: str = Field(..., alias="_id")
    vendor_id: str
    name: str
    phone: str
    email: str | None = None
    total_orders: int = 0
    last_interaction_at: datetime | None = None
    created_at: datetime = Field(default_factory=utc_now)
