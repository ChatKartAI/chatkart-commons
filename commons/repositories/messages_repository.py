"""Mongo repository for messages collection."""

from __future__ import annotations

from pymongo import ASCENDING
from pymongo.collection import Collection

from commons.models.message import Message
from commons.repositories.base import BaseMongoRepository


class MessagesRepository(BaseMongoRepository[Message]):
    """Repository for conversation messages."""

    collection_name = "messages"

    def __init__(self, collection: Collection) -> None:
        super().__init__(collection=collection, model_type=Message)

    def create_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
        metadata: dict | None = None,
    ) -> Message:
        """Create one message for a conversation."""
        return self.create(
            {
                "conversation_id": conversation_id,
                "role": role,
                "content": content,
                "metadata": metadata or {},
            }
        )

    def list_by_conversation(self, conversation_id: str, limit: int = 200) -> list[Message]:
        """Return messages for one conversation in chronological order."""
        return self.find_many(
            {"conversation_id": conversation_id},
            sort=[("created_at", ASCENDING)],
            limit=limit,
        )
