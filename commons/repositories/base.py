from __future__ import annotations

from typing import Any

from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase


class BaseRepository:
    """Base repository with common CRUD helpers."""

    collection_name: str = ""

    def __init__(self, db: AsyncIOMotorDatabase):
        if not self.collection_name:
            raise ValueError("collection_name must be defined in subclass.")
        self._db = db

    @property
    def collection(self) -> AsyncIOMotorCollection:
        return self._db[self.collection_name]

    async def find_by_id(self, doc_id: str) -> dict[str, Any] | None:
        return await self.collection.find_one({"_id": doc_id})

    async def find(self, query: dict[str, Any], limit: int = 50) -> list[dict[str, Any]]:
        cursor = self.collection.find(query).limit(limit)
        return await cursor.to_list(length=limit)

    async def insert(self, document: dict[str, Any]) -> str:
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)

    async def update(self, doc_id: str, update_fields: dict[str, Any]) -> bool:
        result = await self.collection.update_one({"_id": doc_id}, {"$set": update_fields})
        return result.modified_count > 0

    async def delete(self, doc_id: str) -> bool:
        result = await self.collection.delete_one({"_id": doc_id})
        return result.deleted_count > 0

    async def count(self, query: dict[str, Any] | None = None) -> int:
        return await self.collection.count_documents(query or {})