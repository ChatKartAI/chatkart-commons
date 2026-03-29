from __future__ import annotations

from datetime import timedelta

from commons.repositories.base import BaseRepository
from commons.time_utils import utc_now

RESERVATION_TTL_MINUTES = 15


class StockReservationRepository(BaseRepository):
    collection_name = "stock_reservations"

    async def create_reservation(
        self,
        reservation_id: str,
        variant_id: str,
        vendor_id: str,
        customer_id: str,
        quantity: int = 1,
    ) -> str:
        now = utc_now()
        doc = {
            "_id": reservation_id,
            "variant_id": variant_id,
            "vendor_id": vendor_id,
            "customer_id": customer_id,
            "quantity": quantity,
            "expires_at": now + timedelta(minutes=RESERVATION_TTL_MINUTES),
            "created_at": now,
        }
        return await self.insert(doc)

    async def find_active(self, variant_id: str, customer_id: str) -> dict | None:
        return await self.collection.find_one(
            {
                "variant_id": variant_id,
                "customer_id": customer_id,
                "expires_at": {"$gt": utc_now()},
            }
        )

    async def release(self, reservation_id: str) -> bool:
        return await self.delete(reservation_id)

    async def release_by_customer(self, customer_id: str) -> int:
        result = await self.collection.delete_many({"customer_id": customer_id})
        return result.deleted_count
