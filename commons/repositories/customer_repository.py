from __future__ import annotations

from commons.repositories.base import BaseRepository


class CustomerRepository(BaseRepository):
    collection_name = "customers"

    async def find_by_phone(self, vendor_id: str, phone: str) -> dict | None:
        return await self.collection.find_one({"vendor_id": vendor_id, "phone": phone})

    async def find_by_vendor(self, vendor_id: str, limit: int = 100) -> list[dict]:
        return await self.find({"vendor_id": vendor_id}, limit=limit)

    async def increment_orders(self, customer_id: str) -> bool:
        result = await self.collection.update_one(
            {"_id": customer_id}, {"$inc": {"total_orders": 1}}
        )
        return result.modified_count > 0
