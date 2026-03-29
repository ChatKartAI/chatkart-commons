from __future__ import annotations

from commons.repositories.base import BaseRepository


class VendorRepository(BaseRepository):
    collection_name = "vendors"

    async def find_active(self, limit: int = 50) -> list[dict]:
        return await self.find({"status": "active"}, limit=limit)
