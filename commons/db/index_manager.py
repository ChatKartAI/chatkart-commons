from motor.motor_asyncio import AsyncIOMotorDatabase


async def ensure_indexes(db: AsyncIOMotorDatabase) -> None:
    """Create required indexes for ChatKart collections.

    Keep this minimal initially; expand as repositories are migrated.
    """
    await db.customers.create_index([("vendor_id", 1), ("phone", 1)], unique=True)
    await db.articles.create_index([("vendor_id", 1), ("category", 1)])
    await db.articles.create_index(
        [("vendor_id", 1), ("title", "text"), ("description", "text")]
    )
    await db.article_variants.create_index([("article_id", 1), ("vendor_id", 1)])
    await db.orders.create_index([("vendor_id", 1), ("customer_id", 1)])
    await db.stock_reservations.create_index("expires_at", expireAfterSeconds=0)
    await db.chat_sessions.create_index([("vendor_id", 1), ("customer_id", 1)])
    await db.session_articles.create_index(
        [("live_session_id", 1), ("article_id", 1)],
        unique=True,
    )