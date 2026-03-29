"""Mongo repository for users collection."""

from __future__ import annotations

from datetime import datetime, timezone

from pymongo.collection import Collection

from commons.models.user import User
from commons.repositories.base import BaseMongoRepository


class UsersRepository(BaseMongoRepository[User]):
    """Repository focused on user persistence concerns only."""

    collection_name = "users"

    def __init__(self, collection: Collection) -> None:
        super().__init__(collection=collection, model_type=User)

    def get_by_email(self, email: str) -> User | None:
        """Find user by unique email."""
        return self.find_one({"email": email.lower()})

    def create_user(self, email: str, display_name: str | None = None) -> User:
        """Create one user document."""
        return self.create(
            {
                "email": email.lower(),
                "display_name": display_name,
                "is_active": True,
            }
        )

    def touch_last_login(self, user_id: str) -> bool:
        """Update user's `last_login_at` and `updated_at` fields."""
        now = datetime.now(timezone.utc)
        result = self.collection.update_one(
            {"_id": self._to_object_id(user_id)},
            {"$set": {"last_login_at": now, "updated_at": now}},
        )
        return result.modified_count > 0
