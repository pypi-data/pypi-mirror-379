"""Database Manager Module for managing database connections and operations."""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, ClassVar
from warnings import deprecated

from sqlalchemy import Engine, MetaData, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    DeclarativeMeta,
    declarative_base as _declared_base,
    scoped_session,
    sessionmaker,
)

from bear_utils.database._db_config import DatabaseConfig, Schemas, from_db_url, get_default_config
from bear_utils.database._extra import DatabaseManagerMeta, _DynamicRecords

if TYPE_CHECKING:
    from collections.abc import Generator

    from pydantic import SecretStr
    from sqlalchemy.orm.session import Session


class Base(DeclarativeBase): ...


def declarative_base(cls: type[DeclarativeBase] = Base) -> DeclarativeMeta:
    """Create a new declarative base class."""
    return _declared_base(cls=cls)


class DatabaseManager(metaclass=DatabaseManagerMeta):
    """A class to manage database connections and operations."""

    _scheme: ClassVar[Schemas] = "sqlite"
    _base_cls: ClassVar[type[DeclarativeBase]] = Base

    @classmethod
    def set_base(cls, base: DeclarativeMeta) -> None:
        """Set the base class for this database class."""
        cls._base = base

    @classmethod
    def get_base(cls) -> DeclarativeMeta:
        """Get the base class for this database class."""
        if cls._base is None:
            cls._base = declarative_base(cls=cls._base_cls)
        return cls._base

    @classmethod
    def clear_base(cls) -> None:
        """Clear the base class for this database class."""
        cls._base = None

    @classmethod
    def set_scheme(cls, scheme: Schemas) -> None:
        """Set the default scheme for the database manager."""
        cls._scheme = scheme

    def __init__(
        self,
        database_config: DatabaseConfig | None = None,
        host: str = "",
        port: int = 0,
        user: str = "",
        password: str | SecretStr = "",
        name: str = "",
        schema: Schemas | None = None,
        db_url: str | SecretStr | None = None,  # Deprecated, STOP USING THIS PARAMETER
    ) -> None:
        """Initialize the DatabaseManager with a database URL or connection parameters."""
        database_config = from_db_url(db_url) if db_url else database_config  # backwards compatibility
        self.config: DatabaseConfig = database_config or get_default_config(
            schema=schema or self._scheme,
            host=host,
            port=port,
            name=name,
            user=user,
            password=password,
        )
        self.dynamic_records: dict[str, _DynamicRecords] = {}
        self.engine: Engine = create_engine(self.config.db_url.get_secret_value(), echo=False)
        self.metadata: MetaData = self.get_base().metadata
        self.SessionFactory: sessionmaker[Session] = sessionmaker(bind=self.engine)
        if self.instance_session is None:
            self.set_session(scoped_session(self.SessionFactory))
        self.session: scoped_session[Session] = self.get_session()
        self.create_tables()

    def register_records[T_Table](self, name: str, tbl_obj: type[T_Table]) -> _DynamicRecords[T_Table]:
        """Register a table class for dynamic record access.

        Args:
            name (str): The name to register the table class under.
            tbl_obj (type[T]): The table class to register.

        Returns:
            DynamicRecords[T]: An instance of DynamicRecords for the table class.
        """
        if name in self.dynamic_records:
            raise ValueError(f"Records for {name} are already registered.")
        records: _DynamicRecords[T_Table] = _DynamicRecords(tbl_obj=tbl_obj, session=self.session)
        self.dynamic_records[name] = records
        return records

    def get_all[T_Table](self, name: str) -> list[T_Table]:  # type: ignore[override]
        """Get all records from a table.

        Args:
            name (str): The name of the registered table class.

        Returns:
            list[T_Table]: A list of all records in the table.
        """
        if name not in self.dynamic_records:
            raise ValueError(f"Records for {name} are not registered.")
        records: _DynamicRecords[T_Table] = self.dynamic_records[name]
        return records.all()

    def count[T_Table](self, name: str) -> int:
        """Count the number of records in a table.

        Args:
            name (str): The name of the registered table class.

        Returns:
            int: The count of records in the table.
        """
        if name not in self.dynamic_records:
            raise ValueError(f"Records for {name} are not registered.")
        records: _DynamicRecords[T_Table] = self.dynamic_records[name]
        return records.count()

    def get[T_Table](self, name: str, **kwargs) -> list[T_Table]:  # type: ignore[override]
        """Get records from a table by a specific variable.

        Args:
            name (str): The name of the registered table class.
            **kwargs: The variable/column name and value to filter by.

        Returns:
            list[T_Table]: A list of records matching the filter.
        """
        if name not in self.dynamic_records:
            raise ValueError(f"Records for {name} are not registered.")
        records: _DynamicRecords[T_Table] = self.dynamic_records[name]
        return records.filter_by(**kwargs)

    def count_by_var[T_Table](self, name: str, **kwargs) -> int:
        """Count the number of records in a table by a specific variable.

        Args:
            name (str): The name of the registered table class.
            **kwargs: The variable/column name and value to filter by.

        Returns:
            int: The count of records matching the filter.
        """
        if name not in self.dynamic_records:
            raise ValueError(f"Records for {name} are not registered.")
        records: _DynamicRecords[T_Table] = self.dynamic_records[name]
        return len(records.filter_by(**kwargs))

    @property
    def instance_session(self) -> scoped_session | None:
        return self.__class__._scoped_session

    @instance_session.setter
    def instance_session(self, value: scoped_session | None) -> None:
        self.__class__._scoped_session = value

    def get_session(self) -> scoped_session:
        """Get the scoped session for this database class."""
        if self.instance_session is None:
            self.instance_session = scoped_session(self.SessionFactory)
        return self.instance_session

    def set_session(self, session: scoped_session) -> None:
        """Set the scoped session for this database class."""
        self.instance_session = session

    @contextmanager
    def open_session(self) -> Generator[Session, Any]:
        """Provide a transactional scope around a series of operations."""
        session: Session = self.session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise

    def close_session(self) -> None:
        """Close the session."""
        if self.instance_session is not None:
            self.session.remove()
        self.instance_session = None

    def create_tables(self) -> None:
        """Create all tables defined by Base"""
        self.metadata.create_all(self.engine)

    def debug_tables(self) -> dict[str, Any]:
        """Get the tables defined in the metadata."""
        base: DeclarativeMeta = self.get_base()
        return base.metadata.tables

    # We are using this instead since it is a more standard name
    def close(self) -> None:
        """Close the session and connection."""
        self.close_session()
        self.engine.dispose()

    @deprecated("Use close() instead, this method will be removed in a future version.")
    def close_all(self) -> None:
        """Close all sessions and connections."""
        self.close()


class SqliteDB(DatabaseManager):
    """SQLite Database Manager, inherits from DatabaseManager and sets the scheme to sqlite."""

    _scheme: ClassVar[Schemas] = "sqlite"


class PostgresDB(DatabaseManager):
    """Postgres Database Manager, inherits from DatabaseManager and sets the scheme to postgresql."""

    _scheme: ClassVar[Schemas] = "postgresql"


class MySQLDB(DatabaseManager):
    """MySQL Database Manager, inherits from DatabaseManager and sets the scheme to mysql."""

    _scheme: ClassVar[Schemas] = "mysql"


# TODO: Do we care about singleton db managers? Had to disable this since the metaclass and singleton base class conflict
# class SingletonDB(DatabaseManager, SingletonBase):
#     """Singleton class for DatabaseManager, uses SingletonBase to inject singleton pattern."""

#     _scheme: ClassVar[Schemas] = "sqlite"


__all__ = ["DatabaseManager", "MySQLDB", "PostgresDB", "SqliteDB"]
