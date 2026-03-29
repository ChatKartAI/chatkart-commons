from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class OrderStatus(str, Enum):
    PENDING_PAYMENT = "pending_payment"
    PAID = "paid"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class PaymentStatus(str, Enum):
    UNPAID = "unpaid"
    PAID = "paid"
    REFUNDED = "refunded"


class OrderItem(BaseModel):
    variant_id: str
    article_id: str
    quantity: int = 1
    unit_price: float


class Order(BaseModel):
    id: str = Field(..., alias="_id")
    vendor_id: str
    customer_id: str
    status: OrderStatus = OrderStatus.PENDING_PAYMENT
    payment_status: PaymentStatus = PaymentStatus.UNPAID
    items: list[OrderItem] = Field(default_factory=list)
    total_amount: float = 0.0
    currency: str = "INR"
    deleted_at: datetime | None = None
    created_at: datetime = Field(default_factory=utc_now)
