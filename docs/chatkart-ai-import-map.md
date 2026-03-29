# chatkart-ai migration import map

Use this map when migrating imports from `chatkart-ai` to `chatkart-commons`.

## Repository imports

- `backend.db.repositories.article_repo.ArticleRepository` -> `commons.repositories.article_repository.ArticleRepository`
- `backend.db.repositories.article_repo.ArticleVariantRepository` -> `commons.repositories.article_repository.ArticleVariantRepository`
- `backend.db.repositories.customer_repo.CustomerRepository` -> `commons.repositories.customer_repository.CustomerRepository`
- `backend.db.repositories.order_repo.OrderRepository` -> `commons.repositories.order_repository.OrderRepository`
- `backend.db.repositories.session_repo.LiveSessionRepository` -> `commons.repositories.session_repository.LiveSessionRepository`
- `backend.db.repositories.session_repo.SessionArticleRepository` -> `commons.repositories.session_repository.SessionArticleRepository`
- `backend.db.repositories.session_repo.ChatSessionRepository` -> `commons.repositories.session_repository.ChatSessionRepository`
- `backend.db.repositories.message_repo.MessageRepository` -> `commons.repositories.message_repository.MessageRepository`
- `backend.db.repositories.stock_repo.StockReservationRepository` -> `commons.repositories.stock_repository.StockReservationRepository`
- `backend.db.repositories.vendor_repo.VendorRepository` -> `commons.repositories.vendor_repository.VendorRepository`

## Model imports

- `backend.db.models.Article` -> `commons.models.article.Article`
- `backend.db.models.ArticleVariant` -> `commons.models.article.ArticleVariant`
- `backend.db.models.Customer` -> `commons.models.customer.Customer`
- `backend.db.models.Order` -> `commons.models.order.Order`
- `backend.db.models.OrderItem` -> `commons.models.order.OrderItem`
- `backend.db.models.ChatSession` -> `commons.models.session.ChatSession`
- `backend.db.models.ChatSessionState` -> `commons.models.session.ChatSessionState`
- `backend.db.models.LiveSession` -> `commons.models.session.LiveSession`
- `backend.db.models.SessionArticle` -> `commons.models.session.SessionArticle`
- `backend.db.models.Message` -> `commons.models.chat_message.ChatMessage`
- `backend.db.models.StockReservation` -> `commons.models.stock.StockReservation`
- `backend.db.models.Vendor` -> `commons.models.vendor.Vendor`
- `backend.db.models.PlanType` -> `commons.models.vendor.PlanType`
- `backend.db.models.VendorStatus` -> `commons.models.vendor.VendorStatus`

## Wiring

- Keep `MongoConnectionManager` startup/shutdown in app lifespan.
- Pass `db` into repository constructors: `Repo(manager.get_db())`.
