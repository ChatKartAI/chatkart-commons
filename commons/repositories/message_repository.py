from __future__ import annotations

from commons.repositories.base import BaseRepository


class MessageRepository(BaseRepository):
    collection_name = "messages"

    async def find_by_session(self, chat_session_id: str, limit: int = 50) -> list[dict]:
        cursor = (
            self.collection.find({"chat_session_id": chat_session_id})
            .sort("created_at", 1)
            .limit(limit)
        )
        return await cursor.to_list(length=limit)

    async def recent_messages(self, chat_session_id: str, limit: int = 10) -> list[dict]:
        cursor = (
            self.collection.find({"chat_session_id": chat_session_id})
            .sort("created_at", -1)
            .limit(limit)
        )
        docs = await cursor.to_list(length=limit)
        docs.reverse()
        return docs
