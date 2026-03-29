from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from commons.exceptions import DatabaseNotInitializedError


class MongoConnectionManager:
    """Manages Mongo client lifecycle for async apps."""

    def __init__(self, mongo_uri: str, db_name: str):
        self.mongo_uri = mongo_uri
        self.db_name = db_name
        self._client: AsyncIOMotorClient | None = None
        self._db: AsyncIOMotorDatabase | None = None

    async def connect(self) -> AsyncIOMotorDatabase:
        """Initialize Mongo client and return DB handle."""
        if self._db is not None:
            return self._db

        self._client = AsyncIOMotorClient(self.mongo_uri)
        self._db = self._client[self.db_name]
        return self._db

    def get_db(self) -> AsyncIOMotorDatabase:
        """Return initialized DB handle."""
        if self._db is None:
            raise DatabaseNotInitializedError(
                "Database not initialized. Call connect() first."
            )
        return self._db

    async def close(self) -> None:
        """Close Mongo client and clear handles."""
        if self._client is not None:
            self._client.close()
        self._client = None
        self._db = None