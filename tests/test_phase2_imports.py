def test_phase2_imports() -> None:
    from commons.models import Article, ArticleVariant, Order
    from commons.repositories import (
        ArticleRepository,
        ArticleVariantRepository,
        OrderRepository,
    )

    assert Article is not None
    assert ArticleVariant is not None
    assert Order is not None
    assert ArticleRepository is not None
    assert ArticleVariantRepository is not None
    assert OrderRepository is not None
