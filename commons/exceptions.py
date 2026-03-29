class CommonsError(Exception):
    """Base exception for chatkart-commons."""


class DatabaseNotInitializedError(CommonsError):
    """Raised when a DB operation is attempted before initialization."""