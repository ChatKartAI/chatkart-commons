from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from commons.time_utils import utc_now


class Article(BaseModel):
    id: str = Field(..., alias="_id")
    vendor_id: str
    title: str
    description: str = ""
    price: float
    currency: str = "INR"
    stock_quantity: int = 0
    category: str = ""
    image_url: str | None = None
    embedding_vector: list[float] | None = None
    created_at: datetime = Field(default_factory=utc_now)


class ArticleVariant(BaseModel):
    id: str = Field(..., alias="_id")
    article_id: str
    vendor_id: str
    color: str | None = None
    size: str | None = None
    price_override: float | None = None
    stock_quantity: int = 0
    sku: str | None = None
    created_at: datetime = Field(default_factory=utc_now)
