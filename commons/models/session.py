from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class ChatSessionState(str, Enum):
    START = "start"
    BROWSING = "browsing"
    ASKING_DETAILS = "asking_details"
    CART_BUILDING = "cart_building"
    CHECKOUT_STARTED = "checkout_started"
    AWAITING_PAYMENT = "awaiting_payment"
    PAYMENT_CONFIRMED = "payment_confirmed"
    POST_PURCHASE_SUPPORT = "post_purchase_support"
    ESCALATED_TO_HUMAN = "escalated_to_human"


class LiveSession(BaseModel):
    id: str = Field(..., alias="_id")
    vendor_id: str
    title: str = ""
    active: bool = True
    created_at: datetime = Field(default_factory=utc_now)
    expires_at: datetime | None = None


class SessionArticle(BaseModel):
    live_session_id: str
    article_id: str


class ChatSession(BaseModel):
    id: str = Field(..., alias="_id")
    vendor_id: str
    customer_id: str
    live_session_id: str | None = None
    state: ChatSessionState = ChatSessionState.START
    cart_active: bool = False
    human_escalated: bool = False
    created_at: datetime = Field(default_factory=utc_now)
    last_activity_at: datetime = Field(default_factory=utc_now)
