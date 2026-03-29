from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class StockReservation(BaseModel):
    id: str = Field(..., alias="_id")
    variant_id: str
    vendor_id: str
    customer_id: str
    quantity: int = 1
    expires_at: datetime
    created_at: datetime = Field(default_factory=utc_now)
