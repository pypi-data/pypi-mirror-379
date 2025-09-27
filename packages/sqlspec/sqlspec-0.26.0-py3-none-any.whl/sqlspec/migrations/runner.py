"""Migration execution engine for SQLSpec.

This module provides separate sync and async migration runners with clean separation
of concerns and proper type safety.
"""

import operator
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Optional, Union, cast, overload

from sqlspec.core.statement import SQL
from sqlspec.migrations.context import MigrationContext
from sqlspec.migrations.loaders import get_migration_loader
from sqlspec.utils.logging import get_logger
from sqlspec.utils.sync_tools import async_, await_

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from sqlspec.driver import AsyncDriverAdapterBase, SyncDriverAdapterBase

__all__ = ("AsyncMigrationRunner", "SyncMigrationRunner", "create_migration_runner")

logger = get_logger("migrations.runner")


class BaseMigrationRunner(ABC):
    """Base migration runner with common functionality shared between sync and async implementations."""

    def __init__(
        self,
        migrations_path: Path,
        extension_migrations: "Optional[dict[str, Path]]" = None,
        context: "Optional[MigrationContext]" = None,
        extension_configs: "Optional[dict[str, dict[str, Any]]]" = None,
    ) -> None:
        """Initialize the migration runner.

        Args:
            migrations_path: Path to the directory containing migration files.
            extension_migrations: Optional mapping of extension names to their migration paths.
            context: Optional migration context for Python migrations.
            extension_configs: Optional mapping of extension names to their configurations.
        """
        self.migrations_path = migrations_path
        self.extension_migrations = extension_migrations or {}
        from sqlspec.loader import SQLFileLoader

        self.loader = SQLFileLoader()
        self.project_root: Optional[Path] = None
        self.context = context
        self.extension_configs = extension_configs or {}

    def _extract_version(self, filename: str) -> "Optional[str]":
        """Extract version from filename.

        Args:
            filename: The migration filename.

        Returns:
            The extracted version string or None.
        """
        # Handle extension-prefixed versions (e.g., "ext_litestar_0001")
        if filename.startswith("ext_"):
            # This is already a prefixed version, return as-is
            return filename

        # Regular version extraction
        parts = filename.split("_", 1)
        return parts[0].zfill(4) if parts and parts[0].isdigit() else None

    def _calculate_checksum(self, content: str) -> str:
        """Calculate MD5 checksum of migration content.

        Args:
            content: The migration file content.

        Returns:
            MD5 checksum hex string.
        """
        import hashlib

        return hashlib.md5(content.encode()).hexdigest()  # noqa: S324

    @abstractmethod
    def load_migration(self, file_path: Path) -> Union["dict[str, Any]", "Coroutine[Any, Any, dict[str, Any]]"]:
        """Load a migration file and extract its components.

        Args:
            file_path: Path to the migration file.

        Returns:
            Dictionary containing migration metadata and queries.
            For async implementations, returns a coroutine.
        """

    def _get_migration_files_sync(self) -> "list[tuple[str, Path]]":
        """Get all migration files sorted by version.

        Returns:
            List of tuples containing (version, file_path).
        """

        migrations = []

        # Scan primary migration path
        if self.migrations_path.exists():
            for pattern in ("*.sql", "*.py"):
                for file_path in self.migrations_path.glob(pattern):
                    if file_path.name.startswith("."):
                        continue
                    version = self._extract_version(file_path.name)
                    if version:
                        migrations.append((version, file_path))

        # Scan extension migration paths
        for ext_name, ext_path in self.extension_migrations.items():
            if ext_path.exists():
                for pattern in ("*.sql", "*.py"):
                    for file_path in ext_path.glob(pattern):
                        if file_path.name.startswith("."):
                            continue
                        # Prefix extension migrations to avoid version conflicts
                        version = self._extract_version(file_path.name)
                        if version:
                            # Use ext_ prefix to distinguish extension migrations
                            prefixed_version = f"ext_{ext_name}_{version}"
                            migrations.append((prefixed_version, file_path))

        return sorted(migrations, key=operator.itemgetter(0))

    def get_migration_files(self) -> "list[tuple[str, Path]]":
        """Get all migration files sorted by version.

        Returns:
            List of (version, path) tuples sorted by version.
        """
        return self._get_migration_files_sync()

    def _load_migration_metadata_common(self, file_path: Path) -> "dict[str, Any]":
        """Load common migration metadata that doesn't require async operations.

        Args:
            file_path: Path to the migration file.

        Returns:
            Partial migration metadata dictionary.
        """
        content = file_path.read_text(encoding="utf-8")
        checksum = self._calculate_checksum(content)
        version = self._extract_version(file_path.name)
        description = file_path.stem.split("_", 1)[1] if "_" in file_path.stem else ""

        return {
            "version": version,
            "description": description,
            "file_path": file_path,
            "checksum": checksum,
            "content": content,
        }

    def _get_context_for_migration(self, file_path: Path) -> "Optional[MigrationContext]":
        """Get the appropriate context for a migration file.

        Args:
            file_path: Path to the migration file.

        Returns:
            Migration context to use, or None to use default.
        """
        context_to_use = self.context
        if context_to_use and file_path.name.startswith("ext_"):
            version = self._extract_version(file_path.name)
            if version and version.startswith("ext_"):
                min_extension_version_parts = 3
                parts = version.split("_", 2)
                if len(parts) >= min_extension_version_parts:
                    ext_name = parts[1]
                    if ext_name in self.extension_configs:
                        context_to_use = MigrationContext(
                            dialect=self.context.dialect if self.context else None,
                            config=self.context.config if self.context else None,
                            driver=self.context.driver if self.context else None,
                            metadata=self.context.metadata.copy() if self.context and self.context.metadata else {},
                            extension_config=self.extension_configs[ext_name],
                        )

        for ext_name, ext_path in self.extension_migrations.items():
            if file_path.parent == ext_path:
                if ext_name in self.extension_configs and self.context:
                    context_to_use = MigrationContext(
                        config=self.context.config,
                        dialect=self.context.dialect,
                        driver=self.context.driver,
                        metadata=self.context.metadata.copy() if self.context.metadata else {},
                        extension_config=self.extension_configs[ext_name],
                    )
                break

        return context_to_use


class SyncMigrationRunner(BaseMigrationRunner):
    """Synchronous migration runner with pure sync methods."""

    def load_migration(self, file_path: Path) -> "dict[str, Any]":
        """Load a migration file and extract its components.

        Args:
            file_path: Path to the migration file.

        Returns:
            Dictionary containing migration metadata and queries.
        """
        # Get common metadata
        metadata = self._load_migration_metadata_common(file_path)
        context_to_use = self._get_context_for_migration(file_path)

        loader = get_migration_loader(file_path, self.migrations_path, self.project_root, context_to_use)
        loader.validate_migration_file(file_path)

        has_upgrade, has_downgrade = True, False

        if file_path.suffix == ".sql":
            version = metadata["version"]
            up_query, down_query = f"migrate-{version}-up", f"migrate-{version}-down"
            self.loader.clear_cache()
            self.loader.load_sql(file_path)
            has_upgrade, has_downgrade = self.loader.has_query(up_query), self.loader.has_query(down_query)
        else:
            try:
                has_downgrade = bool(self._get_migration_sql_sync({"loader": loader, "file_path": file_path}, "down"))
            except Exception:
                has_downgrade = False

        metadata.update({"has_upgrade": has_upgrade, "has_downgrade": has_downgrade, "loader": loader})
        return metadata

    def execute_upgrade(
        self, driver: "SyncDriverAdapterBase", migration: "dict[str, Any]"
    ) -> "tuple[Optional[str], int]":
        """Execute an upgrade migration.

        Args:
            driver: The sync database driver to use.
            migration: Migration metadata dictionary.

        Returns:
            Tuple of (sql_content, execution_time_ms).
        """
        upgrade_sql_list = self._get_migration_sql_sync(migration, "up")
        if upgrade_sql_list is None:
            return None, 0

        start_time = time.time()

        for sql_statement in upgrade_sql_list:
            if sql_statement.strip():
                driver.execute_script(sql_statement)
        execution_time = int((time.time() - start_time) * 1000)
        return None, execution_time

    def execute_downgrade(
        self, driver: "SyncDriverAdapterBase", migration: "dict[str, Any]"
    ) -> "tuple[Optional[str], int]":
        """Execute a downgrade migration.

        Args:
            driver: The sync database driver to use.
            migration: Migration metadata dictionary.

        Returns:
            Tuple of (sql_content, execution_time_ms).
        """
        downgrade_sql_list = self._get_migration_sql_sync(migration, "down")
        if downgrade_sql_list is None:
            return None, 0

        start_time = time.time()

        for sql_statement in downgrade_sql_list:
            if sql_statement.strip():
                driver.execute_script(sql_statement)
        execution_time = int((time.time() - start_time) * 1000)
        return None, execution_time

    def _get_migration_sql_sync(self, migration: "dict[str, Any]", direction: str) -> "Optional[list[str]]":
        """Get migration SQL for given direction (sync version).

        Args:
            migration: Migration metadata.
            direction: Either 'up' or 'down'.

        Returns:
            SQL statements for the migration.
        """
        # If this is being called during migration loading (no has_*grade field yet),
        # don't raise/warn - just proceed to check if the method exists
        if f"has_{direction}grade" in migration and not migration.get(f"has_{direction}grade"):
            if direction == "down":
                logger.warning("Migration %s has no downgrade query", migration.get("version"))
                return None
            msg = f"Migration {migration.get('version')} has no upgrade query"
            raise ValueError(msg)

        file_path, loader = migration["file_path"], migration["loader"]

        try:
            method = loader.get_up_sql if direction == "up" else loader.get_down_sql
            # Check if the method is async and handle appropriately
            import inspect

            if inspect.iscoroutinefunction(method):
                # For async methods, use await_ to run in sync context
                sql_statements = await_(method, raise_sync_error=False)(file_path)
            else:
                # For sync methods, call directly
                sql_statements = method(file_path)

        except Exception as e:
            if direction == "down":
                logger.warning("Failed to load downgrade for migration %s: %s", migration.get("version"), e)
                return None
            msg = f"Failed to load upgrade for migration {migration.get('version')}: {e}"
            raise ValueError(msg) from e
        else:
            if sql_statements:
                return cast("list[str]", sql_statements)
            return None

    def load_all_migrations(self) -> "dict[str, SQL]":
        """Load all migrations into a single namespace for bulk operations.

        Returns:
            Dictionary mapping query names to SQL objects.
        """
        all_queries = {}
        migrations = self.get_migration_files()

        for version, file_path in migrations:
            if file_path.suffix == ".sql":
                self.loader.load_sql(file_path)
                for query_name in self.loader.list_queries():
                    all_queries[query_name] = self.loader.get_sql(query_name)
            else:
                loader = get_migration_loader(file_path, self.migrations_path, self.project_root, self.context)

                try:
                    up_sql = await_(loader.get_up_sql)(file_path)
                    down_sql = await_(loader.get_down_sql)(file_path)

                    if up_sql:
                        all_queries[f"migrate-{version}-up"] = SQL(up_sql[0])
                    if down_sql:
                        all_queries[f"migrate-{version}-down"] = SQL(down_sql[0])

                except Exception as e:
                    logger.debug("Failed to load Python migration %s: %s", file_path, e)

        return all_queries


class AsyncMigrationRunner(BaseMigrationRunner):
    """Asynchronous migration runner with pure async methods."""

    async def get_migration_files(self) -> "list[tuple[str, Path]]":  # type: ignore[override]
        """Get all migration files sorted by version.

        Returns:
            List of (version, path) tuples sorted by version.
        """
        return self._get_migration_files_sync()

    async def load_migration(self, file_path: Path) -> "dict[str, Any]":
        """Load a migration file and extract its components.

        Args:
            file_path: Path to the migration file.

        Returns:
            Dictionary containing migration metadata and queries.
        """
        # Get common metadata
        metadata = self._load_migration_metadata_common(file_path)
        context_to_use = self._get_context_for_migration(file_path)

        loader = get_migration_loader(file_path, self.migrations_path, self.project_root, context_to_use)
        loader.validate_migration_file(file_path)

        has_upgrade, has_downgrade = True, False

        if file_path.suffix == ".sql":
            version = metadata["version"]
            up_query, down_query = f"migrate-{version}-up", f"migrate-{version}-down"
            self.loader.clear_cache()
            await async_(self.loader.load_sql)(file_path)
            has_upgrade, has_downgrade = self.loader.has_query(up_query), self.loader.has_query(down_query)
        else:
            try:
                has_downgrade = bool(
                    await self._get_migration_sql_async({"loader": loader, "file_path": file_path}, "down")
                )
            except Exception:
                has_downgrade = False

        metadata.update({"has_upgrade": has_upgrade, "has_downgrade": has_downgrade, "loader": loader})
        return metadata

    async def execute_upgrade(
        self, driver: "AsyncDriverAdapterBase", migration: "dict[str, Any]"
    ) -> "tuple[Optional[str], int]":
        """Execute an upgrade migration.

        Args:
            driver: The async database driver to use.
            migration: Migration metadata dictionary.

        Returns:
            Tuple of (sql_content, execution_time_ms).
        """
        upgrade_sql_list = await self._get_migration_sql_async(migration, "up")
        if upgrade_sql_list is None:
            return None, 0

        start_time = time.time()

        for sql_statement in upgrade_sql_list:
            if sql_statement.strip():
                await driver.execute_script(sql_statement)
        execution_time = int((time.time() - start_time) * 1000)
        return None, execution_time

    async def execute_downgrade(
        self, driver: "AsyncDriverAdapterBase", migration: "dict[str, Any]"
    ) -> "tuple[Optional[str], int]":
        """Execute a downgrade migration.

        Args:
            driver: The async database driver to use.
            migration: Migration metadata dictionary.

        Returns:
            Tuple of (sql_content, execution_time_ms).
        """
        downgrade_sql_list = await self._get_migration_sql_async(migration, "down")
        if downgrade_sql_list is None:
            return None, 0

        start_time = time.time()

        for sql_statement in downgrade_sql_list:
            if sql_statement.strip():
                await driver.execute_script(sql_statement)
        execution_time = int((time.time() - start_time) * 1000)
        return None, execution_time

    async def _get_migration_sql_async(self, migration: "dict[str, Any]", direction: str) -> "Optional[list[str]]":
        """Get migration SQL for given direction (async version).

        Args:
            migration: Migration metadata.
            direction: Either 'up' or 'down'.

        Returns:
            SQL statements for the migration.
        """
        # If this is being called during migration loading (no has_*grade field yet),
        # don't raise/warn - just proceed to check if the method exists
        if f"has_{direction}grade" in migration and not migration.get(f"has_{direction}grade"):
            if direction == "down":
                logger.warning("Migration %s has no downgrade query", migration.get("version"))
                return None
            msg = f"Migration {migration.get('version')} has no upgrade query"
            raise ValueError(msg)

        file_path, loader = migration["file_path"], migration["loader"]

        try:
            method = loader.get_up_sql if direction == "up" else loader.get_down_sql
            sql_statements = await method(file_path)

        except Exception as e:
            if direction == "down":
                logger.warning("Failed to load downgrade for migration %s: %s", migration.get("version"), e)
                return None
            msg = f"Failed to load upgrade for migration {migration.get('version')}: {e}"
            raise ValueError(msg) from e
        else:
            if sql_statements:
                return cast("list[str]", sql_statements)
            return None

    async def load_all_migrations(self) -> "dict[str, SQL]":
        """Load all migrations into a single namespace for bulk operations.

        Returns:
            Dictionary mapping query names to SQL objects.
        """
        all_queries = {}
        migrations = await self.get_migration_files()

        for version, file_path in migrations:
            if file_path.suffix == ".sql":
                await async_(self.loader.load_sql)(file_path)
                for query_name in self.loader.list_queries():
                    all_queries[query_name] = self.loader.get_sql(query_name)
            else:
                loader = get_migration_loader(file_path, self.migrations_path, self.project_root, self.context)

                try:
                    up_sql = await loader.get_up_sql(file_path)
                    down_sql = await loader.get_down_sql(file_path)

                    if up_sql:
                        all_queries[f"migrate-{version}-up"] = SQL(up_sql[0])
                    if down_sql:
                        all_queries[f"migrate-{version}-down"] = SQL(down_sql[0])

                except Exception as e:
                    logger.debug("Failed to load Python migration %s: %s", file_path, e)

        return all_queries


@overload
def create_migration_runner(
    migrations_path: Path,
    extension_migrations: "dict[str, Path]",
    context: "Optional[MigrationContext]",
    extension_configs: "dict[str, Any]",
    is_async: "Literal[False]" = False,
) -> SyncMigrationRunner: ...


@overload
def create_migration_runner(
    migrations_path: Path,
    extension_migrations: "dict[str, Path]",
    context: "Optional[MigrationContext]",
    extension_configs: "dict[str, Any]",
    is_async: "Literal[True]",
) -> AsyncMigrationRunner: ...


def create_migration_runner(
    migrations_path: Path,
    extension_migrations: "dict[str, Path]",
    context: "Optional[MigrationContext]",
    extension_configs: "dict[str, Any]",
    is_async: bool = False,
) -> "Union[SyncMigrationRunner, AsyncMigrationRunner]":
    """Factory function to create the appropriate migration runner.

    Args:
        migrations_path: Path to migrations directory.
        extension_migrations: Extension migration paths.
        context: Migration context.
        extension_configs: Extension configurations.
        is_async: Whether to create async or sync runner.

    Returns:
        Appropriate migration runner instance.
    """
    if is_async:
        return AsyncMigrationRunner(migrations_path, extension_migrations, context, extension_configs)
    return SyncMigrationRunner(migrations_path, extension_migrations, context, extension_configs)
