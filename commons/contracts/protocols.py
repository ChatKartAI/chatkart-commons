"""Protocol definitions to keep repository typing stable."""

from __future__ import annotations

from typing import Any, Protocol

from pydantic import BaseModel


class RepositoryProtocol(Protocol):
    """Contract implemented by concrete Mongo repositories."""

    model_type: type[BaseModel]

    def get_by_id(self, document_id: str) -> BaseModel | None:
        """Fetch one document by its Mongo identifier."""

    def create(self, payload: dict[str, Any]) -> BaseModel:
        """Insert one document and return the hydrated model."""

    def update_by_id(self, document_id: str, update: dict[str, Any]) -> bool:
        """Apply updates to one document and return success state."""

    def delete_by_id(self, document_id: str) -> bool:
        """Delete one document and return success state."""
