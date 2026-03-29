from __future__ import annotations

from commons.repositories.base import BaseRepository


class ArticleRepository(BaseRepository):
    collection_name = "articles"

    async def search(self, vendor_id: str, query: str, limit: int = 10) -> list[dict]:
        return await self.find(
            {
                "vendor_id": vendor_id,
                "$text": {"$search": query},
            },
            limit=limit,
        )

    async def find_by_vendor(self, vendor_id: str, limit: int = 50) -> list[dict]:
        return await self.find({"vendor_id": vendor_id}, limit=limit)

    async def find_by_category(
        self, vendor_id: str, category: str, limit: int = 20
    ) -> list[dict]:
        return await self.find(
            {"vendor_id": vendor_id, "category": category},
            limit=limit,
        )

    async def find_by_ids(self, article_ids: list[str]) -> list[dict]:
        cursor = self.collection.find({"_id": {"$in": article_ids}})
        return await cursor.to_list(length=len(article_ids))

    async def find_by_id_for_vendor(self, article_id: str, vendor_id: str) -> dict | None:
        return await self.collection.find_one({"_id": article_id, "vendor_id": vendor_id})


class ArticleVariantRepository(BaseRepository):
    collection_name = "article_variants"

    async def find_by_article(self, article_id: str) -> list[dict]:
        return await self.find({"article_id": article_id}, limit=100)

    async def find_by_vendor(self, vendor_id: str, limit: int = 100) -> list[dict]:
        return await self.find({"vendor_id": vendor_id}, limit=limit)

    async def find_by_id_for_vendor(self, variant_id: str, vendor_id: str) -> dict | None:
        return await self.collection.find_one({"_id": variant_id, "vendor_id": vendor_id})

    async def decrement_stock(self, variant_id: str, quantity: int = 1) -> bool:
        result = await self.collection.update_one(
            {"_id": variant_id, "stock_quantity": {"$gte": quantity}},
            {"$inc": {"stock_quantity": -quantity}},
        )
        return result.modified_count > 0

    async def increment_stock(self, variant_id: str, quantity: int = 1) -> bool:
        result = await self.collection.update_one(
            {"_id": variant_id},
            {"$inc": {"stock_quantity": quantity}},
        )
        return result.modified_count > 0
