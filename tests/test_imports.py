def test_imports_work() -> None:
    from commons.db.connection import MongoConnectionManager
    from commons.db.index_manager import ensure_indexes
    from commons.repositories.base import BaseRepository

    assert MongoConnectionManager is not None
    assert ensure_indexes is not None
    assert BaseRepository is not None