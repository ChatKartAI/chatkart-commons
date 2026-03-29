from __future__ import annotations

from commons.repositories.base import BaseRepository
from commons.time_utils import utc_now


class OrderRepository(BaseRepository):
    collection_name = "orders"

    async def find_by_customer(
        self, vendor_id: str, customer_id: str, limit: int = 20
    ) -> list[dict]:
        return await self.find(
            {
                "vendor_id": vendor_id,
                "customer_id": customer_id,
                "deleted_at": None,
            },
            limit=limit,
        )

    async def update_status(self, order_id: str, status: str) -> bool:
        return await self.update(order_id, {"status": status})

    async def update_payment_status(self, order_id: str, payment_status: str) -> bool:
        return await self.update(order_id, {"payment_status": payment_status})

    async def soft_delete(self, order_id: str) -> bool:
        return await self.update(order_id, {"deleted_at": utc_now()})
