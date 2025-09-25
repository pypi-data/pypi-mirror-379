import sys
import logging
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import contextlib

from stllrent_bootstrap.flask.app_settings import BaseAppSettings
from stllrent_bootstrap.database.model.core import Base
from stllrent_bootstrap.flask.app_logger import get_logger

class DatabaseManager:
    """
    Gerenciador centralizado para a configuração e sessão do SQLAlchemy.
    Esta classe é instanciada uma vez por aplicação.
    """
    def __init__(self, settings: BaseAppSettings):
        self.settings = settings
        self.logger = get_logger()
        self.engine = self._create_engine()
        self.SessionLocal = self._create_sessionmaker()

    def _create_engine(self):
        """Cria e retorna a engine do SQLAlchemy com base nas configurações."""
        return create_engine(
            str(self.settings.SQLALCHEMY_DATABASE_URI),
            echo=False,  # Desativado para evitar logs duplicados. O controle será feito via logging.
            pool_size=self.settings.SQLALCHEMY_POOL_SIZE,
            max_overflow=self.settings.SQLALCHEMY_MAX_OVERFLOW,
            pool_recycle=3600 if self.settings.SQLALCHEMY_POOL_RECYCLE else -1
        )

    def _create_sessionmaker(self):
        """Cria e retorna a fábrica de sessões (sessionmaker)."""
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    @contextlib.contextmanager
    def get_session(self):
        """
        Fornece uma sessão do banco de dados gerenciada por um context manager.
        Garante que a sessão seja fechada após o uso.
        """
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def setup_database(self, app: Flask):
        """Configura a aplicação Flask e cria tabelas em ambiente de desenvolvimento."""
        # Configura o logger do SQLAlchemy para usar o mesmo nível da aplicação
        # e evita que ele propague logs para o logger root, prevenindo duplicação.
        sql_alchemy_logger = logging.getLogger('sqlalchemy.engine')
        if self.settings.SQL_ALCHEMY_ECHO:
            # Adiciona os handlers do logger principal ao logger do SQLAlchemy.
            main_app_logger = get_logger()
            for handler in main_app_logger.handlers:
                sql_alchemy_logger.addHandler(handler)
            sql_alchemy_logger.setLevel(self.settings.APP_LOG_LEVEL)
            sql_alchemy_logger.propagate = False  # Agora que tem handler, desativar a propagação evita duplicatas.
        else:
            sql_alchemy_logger.setLevel(logging.WARNING)

        if self.settings.MODEL_DISCOVERY_PATHS and self.settings.FLASK_ENV == 'development':
            self.logger.info("Attempting to create database tables (development mode)...")
            try:
                Base.metadata.create_all(self.engine)
                self.logger.info("Database tables created successfully (or already exist).")
            except Exception as e:
                self.logger.error('DB Create fail with error: %s', str(e), exc_info=True)
                sys.exit(128)
        else:
            self.logger.debug("Database tables creation process will not be executed in this environment or there is no database for this application")
            self.logger.debug(f"Environment: {self.settings.FLASK_ENV}")
            self.logger.debug(f"MODEL_DISCOVERY_PATHS: {self.settings.MODEL_DISCOVERY_PATHS}")
