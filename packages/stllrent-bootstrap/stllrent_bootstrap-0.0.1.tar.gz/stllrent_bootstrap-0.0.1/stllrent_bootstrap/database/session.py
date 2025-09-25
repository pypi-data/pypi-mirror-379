import contextlib
from flask import current_app

@contextlib.contextmanager
def get_db_session():
    """
    Provides a database session from the DatabaseManager stored in the
    Flask application context.

    This acts as a bridge between the bootstrap module and the application code,
    allowing easy access to the session within a request context.
    """
    db_manager = current_app.extensions.get("db_manager")
    if not db_manager:
        raise RuntimeError(
            "DatabaseManager not found in the Flask application. "
            "Please ensure it has been correctly configured in create_app."
        )
    
    with db_manager.get_session() as session:
        yield session