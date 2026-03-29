"""Mongo repository for conversations collection."""

from __future__ import annotations

from pymongo import DESCENDING
from pymongo.collection import Collection

from commons.models.conversation import Conversation
from commons.repositories.base import BaseMongoRepository


class ConversationsRepository(BaseMongoRepository[Conversation]):
    """Repository for reading and writing conversation metadata."""

    collection_name = "conversations"

    def __init__(self, collection: Collection) -> None:
        super().__init__(collection=collection, model_type=Conversation)

    def create_conversation(self, user_id: str, title: str | None = None) -> Conversation:
        """Create one conversation for a user."""
        return self.create({"user_id": user_id, "title": title, "archived": False})

    def list_by_user(self, user_id: str, limit: int = 50) -> list[Conversation]:
        """List conversations for a user ordered by newest update first."""
        return self.find_many(
            {"user_id": user_id},
            sort=[("updated_at", DESCENDING)],
            limit=limit,
        )

    def archive(self, conversation_id: str) -> bool:
        """Set conversation archived flag to true."""
        return self.update_by_id(conversation_id, {"archived": True})
