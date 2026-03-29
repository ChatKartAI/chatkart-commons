from __future__ import annotations

from commons.repositories.base import BaseRepository
from commons.time_utils import utc_now


class LiveSessionRepository(BaseRepository):
    collection_name = "sessions"

    async def find_active(self, vendor_id: str) -> dict | None:
        return await self.collection.find_one({"vendor_id": vendor_id, "active": True})


class SessionArticleRepository(BaseRepository):
    collection_name = "session_articles"

    async def get_article_ids(self, live_session_id: str) -> list[str]:
        docs = await self.find({"live_session_id": live_session_id}, limit=500)
        return [d["article_id"] for d in docs]

    async def add_mapping(self, live_session_id: str, article_id: str) -> str:
        return await self.insert(
            {"live_session_id": live_session_id, "article_id": article_id}
        )


class ChatSessionRepository(BaseRepository):
    collection_name = "chat_sessions"

    async def find_active(self, vendor_id: str, customer_id: str) -> dict | None:
        return await self.collection.find_one(
            {"vendor_id": vendor_id, "customer_id": customer_id},
            sort=[("created_at", -1)],
        )

    async def update_state(self, session_id: str, state: str) -> bool:
        return await self.update(session_id, {"state": state, "last_activity_at": utc_now()})

    async def set_escalated(self, session_id: str) -> bool:
        return await self.update(
            session_id,
            {
                "human_escalated": True,
                "state": "escalated_to_human",
                "last_activity_at": utc_now(),
            },
        )
