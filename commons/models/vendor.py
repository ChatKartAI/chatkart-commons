from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class PlanType(str, Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class VendorStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class Vendor(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    plan_type: PlanType = PlanType.FREE
    phone: str
    email: str | None = None
    status: VendorStatus = VendorStatus.ACTIVE
    created_at: datetime = Field(default_factory=utc_now)
