"""Base classes for SQLSpec migrations.

This module provides abstract base classes for migration components.
"""

import hashlib
import operator
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Generic, Optional, TypeVar, cast

from sqlspec._sql import sql
from sqlspec.builder import Delete, Insert, Select
from sqlspec.builder._ddl import CreateTable
from sqlspec.loader import SQLFileLoader
from sqlspec.migrations.loaders import get_migration_loader
from sqlspec.utils.logging import get_logger
from sqlspec.utils.module_loader import module_to_os_path
from sqlspec.utils.sync_tools import await_

__all__ = ("BaseMigrationCommands", "BaseMigrationRunner", "BaseMigrationTracker")


logger = get_logger("migrations.base")

DriverT = TypeVar("DriverT")
ConfigT = TypeVar("ConfigT")


class BaseMigrationTracker(ABC, Generic[DriverT]):
    """Base class for migration version tracking."""

    __slots__ = ("version_table",)

    def __init__(self, version_table_name: str = "ddl_migrations") -> None:
        """Initialize the migration tracker.

        Args:
            version_table_name: Name of the table to track migrations.
        """
        self.version_table = version_table_name

    def _get_create_table_sql(self) -> CreateTable:
        """Get SQL builder for creating the tracking table.

        Returns:
            SQL builder object for table creation.
        """
        return (
            sql.create_table(self.version_table)
            .if_not_exists()
            .column("version_num", "VARCHAR(32)", primary_key=True)
            .column("description", "TEXT")
            .column("applied_at", "TIMESTAMP", default="CURRENT_TIMESTAMP", not_null=True)
            .column("execution_time_ms", "INTEGER")
            .column("checksum", "VARCHAR(64)")
            .column("applied_by", "VARCHAR(255)")
        )

    def _get_current_version_sql(self) -> Select:
        """Get SQL builder for retrieving current version.

        Returns:
            SQL builder object for version query.
        """
        return sql.select("version_num").from_(self.version_table).order_by("version_num DESC").limit(1)

    def _get_applied_migrations_sql(self) -> Select:
        """Get SQL builder for retrieving all applied migrations.

        Returns:
            SQL builder object for migrations query.
        """
        return sql.select("*").from_(self.version_table).order_by("version_num")

    def _get_record_migration_sql(
        self, version: str, description: str, execution_time_ms: int, checksum: str, applied_by: str
    ) -> Insert:
        """Get SQL builder for recording a migration.

        Args:
            version: Version number of the migration.
            description: Description of the migration.
            execution_time_ms: Execution time in milliseconds.
            checksum: MD5 checksum of the migration content.
            applied_by: User who applied the migration.

        Returns:
            SQL builder object for insert.
        """
        return (
            sql.insert(self.version_table)
            .columns("version_num", "description", "execution_time_ms", "checksum", "applied_by")
            .values(version, description, execution_time_ms, checksum, applied_by)
        )

    def _get_remove_migration_sql(self, version: str) -> Delete:
        """Get SQL builder for removing a migration record.

        Args:
            version: Version number to remove.

        Returns:
            SQL builder object for delete.
        """
        return sql.delete().from_(self.version_table).where(sql.version_num == version)

    @abstractmethod
    def ensure_tracking_table(self, driver: DriverT) -> Any:
        """Create the migration tracking table if it doesn't exist."""
        ...

    @abstractmethod
    def get_current_version(self, driver: DriverT) -> Any:
        """Get the latest applied migration version."""
        ...

    @abstractmethod
    def get_applied_migrations(self, driver: DriverT) -> Any:
        """Get all applied migrations in order."""
        ...

    @abstractmethod
    def record_migration(
        self, driver: DriverT, version: str, description: str, execution_time_ms: int, checksum: str
    ) -> Any:
        """Record a successfully applied migration."""
        ...

    @abstractmethod
    def remove_migration(self, driver: DriverT, version: str) -> Any:
        """Remove a migration record."""
        ...


class BaseMigrationRunner(ABC, Generic[DriverT]):
    """Base class for migration execution."""

    extension_configs: "dict[str, dict[str, Any]]"

    def __init__(
        self,
        migrations_path: Path,
        extension_migrations: "Optional[dict[str, Path]]" = None,
        context: "Optional[Any]" = None,
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
        self.loader = SQLFileLoader()
        self.project_root: Optional[Path] = None
        self.context = context
        self.extension_configs = extension_configs or {}

    def _extract_version(self, filename: str) -> Optional[str]:
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

        return hashlib.md5(content.encode()).hexdigest()  # noqa: S324

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

    def _load_migration_metadata(self, file_path: Path) -> "dict[str, Any]":
        """Load migration metadata from file.

        Args:
            file_path: Path to the migration file.

        Returns:
            Migration metadata dictionary.
        """

        # Check if this is an extension migration and update context accordingly
        context_to_use = self.context
        if context_to_use and file_path.name.startswith("ext_"):
            # Try to extract extension name from the version
            version = self._extract_version(file_path.name)
            if version and version.startswith("ext_"):
                # Parse extension name from version like "ext_litestar_0001"
                min_extension_version_parts = 3
                parts = version.split("_", 2)
                if len(parts) >= min_extension_version_parts:
                    ext_name = parts[1]
                    if ext_name in self.extension_configs:
                        # Create a new context with the extension config
                        from sqlspec.migrations.context import MigrationContext

                        context_to_use = MigrationContext(
                            dialect=self.context.dialect if self.context else None,
                            config=self.context.config if self.context else None,
                            driver=self.context.driver if self.context else None,
                            metadata=self.context.metadata.copy() if self.context and self.context.metadata else {},
                            extension_config=self.extension_configs[ext_name],
                        )

        # For extension migrations, check by path
        for ext_name, ext_path in self.extension_migrations.items():
            if file_path.parent == ext_path:
                if ext_name in self.extension_configs and self.context:
                    from sqlspec.migrations.context import MigrationContext

                    context_to_use = MigrationContext(
                        dialect=self.context.dialect,
                        config=self.context.config,
                        driver=self.context.driver,
                        metadata=self.context.metadata.copy() if self.context.metadata else {},
                        extension_config=self.extension_configs[ext_name],
                    )
                break

        loader = get_migration_loader(file_path, self.migrations_path, self.project_root, context_to_use)
        loader.validate_migration_file(file_path)
        content = file_path.read_text(encoding="utf-8")
        checksum = self._calculate_checksum(content)
        version = self._extract_version(file_path.name)
        description = file_path.stem.split("_", 1)[1] if "_" in file_path.stem else ""

        has_upgrade, has_downgrade = True, False

        if file_path.suffix == ".sql":
            up_query, down_query = f"migrate-{version}-up", f"migrate-{version}-down"
            self.loader.clear_cache()
            self.loader.load_sql(file_path)
            has_upgrade, has_downgrade = self.loader.has_query(up_query), self.loader.has_query(down_query)
        else:
            try:
                has_downgrade = bool(await_(loader.get_down_sql, raise_sync_error=False)(file_path))
            except Exception:
                has_downgrade = False

        return {
            "version": version,
            "description": description,
            "file_path": file_path,
            "checksum": checksum,
            "has_upgrade": has_upgrade,
            "has_downgrade": has_downgrade,
            "loader": loader,
        }

    def _get_migration_sql(self, migration: "dict[str, Any]", direction: str) -> "Optional[list[str]]":
        """Get migration SQL for given direction.

        Args:
            migration: Migration metadata.
            direction: Either 'up' or 'down'.

        Returns:
            SQL object for the migration.
        """
        if not migration.get(f"has_{direction}grade"):
            if direction == "down":
                logger.warning("Migration %s has no downgrade query", migration["version"])
                return None
            msg = f"Migration {migration['version']} has no upgrade query"
            raise ValueError(msg)

        file_path, loader = migration["file_path"], migration["loader"]

        try:
            method = loader.get_up_sql if direction == "up" else loader.get_down_sql
            sql_statements = await_(method, raise_sync_error=False)(file_path)

        except Exception as e:
            if direction == "down":
                logger.warning("Failed to load downgrade for migration %s: %s", migration["version"], e)
                return None
            msg = f"Failed to load upgrade for migration {migration['version']}: {e}"
            raise ValueError(msg) from e
        else:
            if sql_statements:
                return cast("list[str]", sql_statements)
            return None

    @abstractmethod
    def get_migration_files(self) -> Any:
        """Get all migration files sorted by version."""
        ...

    @abstractmethod
    def load_migration(self, file_path: Path) -> Any:
        """Load a migration file and extract its components."""
        ...

    @abstractmethod
    def execute_upgrade(self, driver: DriverT, migration: "dict[str, Any]") -> Any:
        """Execute an upgrade migration."""
        ...

    @abstractmethod
    def execute_downgrade(self, driver: DriverT, migration: "dict[str, Any]") -> Any:
        """Execute a downgrade migration."""
        ...

    @abstractmethod
    def load_all_migrations(self) -> Any:
        """Load all migrations into a single namespace for bulk operations."""
        ...


class BaseMigrationCommands(ABC, Generic[ConfigT, DriverT]):
    """Base class for migration commands."""

    extension_configs: "dict[str, dict[str, Any]]"

    def __init__(self, config: ConfigT) -> None:
        """Initialize migration commands.

        Args:
            config: The SQLSpec configuration.
        """
        self.config = config
        migration_config = getattr(self.config, "migration_config", {}) or {}

        self.version_table = migration_config.get("version_table_name", "ddl_migrations")
        self.migrations_path = Path(migration_config.get("script_location", "migrations"))
        self.project_root = Path(migration_config["project_root"]) if "project_root" in migration_config else None
        self.include_extensions = migration_config.get("include_extensions", [])
        self.extension_configs = self._parse_extension_configs()

    def _parse_extension_configs(self) -> "dict[str, dict[str, Any]]":
        """Parse extension configurations from include_extensions.

        Supports both string format (extension name) and dict format
        (extension name with configuration).

        Returns:
            Dictionary mapping extension names to their configurations.
        """
        configs = {}

        for ext_config in self.include_extensions:
            if isinstance(ext_config, str):
                # Simple string format: just the extension name
                ext_name = ext_config
                ext_options = {}
            elif isinstance(ext_config, dict):
                # Dict format: {"name": "litestar", "session_table": "custom_sessions"}
                ext_name_raw = ext_config.get("name")
                if not ext_name_raw:
                    logger.warning("Extension configuration missing 'name' field: %s", ext_config)
                    continue
                # Assert for type narrowing: ext_name_raw is guaranteed to be str here
                assert isinstance(ext_name_raw, str)
                ext_name = ext_name_raw
                ext_options = {k: v for k, v in ext_config.items() if k != "name"}
            else:
                logger.warning("Invalid extension configuration format: %s", ext_config)
                continue

            # Apply default configurations for known extensions
            if ext_name == "litestar" and "session_table" not in ext_options:
                ext_options["session_table"] = "litestar_sessions"

            configs[ext_name] = ext_options

        return configs

    def _discover_extension_migrations(self) -> "dict[str, Path]":
        """Discover migration paths for configured extensions.

        Returns:
            Dictionary mapping extension names to their migration paths.
        """

        extension_migrations = {}

        for ext_name in self.extension_configs:
            module_name = "sqlspec.extensions.litestar" if ext_name == "litestar" else f"sqlspec.extensions.{ext_name}"

            try:
                module_path = module_to_os_path(module_name)
                migrations_dir = module_path / "migrations"

                if migrations_dir.exists():
                    extension_migrations[ext_name] = migrations_dir
                    logger.debug("Found migrations for extension %s at %s", ext_name, migrations_dir)
                else:
                    logger.warning("No migrations directory found for extension %s", ext_name)
            except TypeError:
                logger.warning("Extension %s not found", ext_name)

        return extension_migrations

    def _get_init_readme_content(self) -> str:
        """Get README content for migration directory initialization.

        Returns:
            README markdown content.
        """
        return """# SQLSpec Migrations

This directory contains database migration files.

## File Format

Migration files use SQLFileLoader's named query syntax with versioned names:

```sql
-- name: migrate-0001-up
CREATE TABLE example (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- name: migrate-0001-down
DROP TABLE example;
```

## Naming Conventions

### File Names

Format: `{version}_{description}.sql`

- Version: Zero-padded 4-digit number (0001, 0002, etc.)
- Description: Brief description using underscores
- Example: `0001_create_users_table.sql`

### Query Names

- Upgrade: `migrate-{version}-up`
- Downgrade: `migrate-{version}-down`

This naming ensures proper sorting and avoids conflicts when loading multiple files.
"""

    def init_directory(self, directory: str, package: bool = True) -> None:
        """Initialize migration directory structure.

        Args:
            directory: Directory to initialize migrations in.
            package: Whether to create __init__.py file.
        """
        from rich.console import Console

        console = Console()

        migrations_dir = Path(directory)
        migrations_dir.mkdir(parents=True, exist_ok=True)

        if package:
            (migrations_dir / "__init__.py").touch()

        readme = migrations_dir / "README.md"
        readme.write_text(self._get_init_readme_content())

        console.print(f"[green]Initialized migrations in {directory}[/]")

    @abstractmethod
    def init(self, directory: str, package: bool = True) -> Any:
        """Initialize migration directory structure."""
        ...

    @abstractmethod
    def current(self, verbose: bool = False) -> Any:
        """Show current migration version."""
        ...

    @abstractmethod
    def upgrade(self, revision: str = "head") -> Any:
        """Upgrade to a target revision."""
        ...

    @abstractmethod
    def downgrade(self, revision: str = "-1") -> Any:
        """Downgrade to a target revision."""
        ...

    @abstractmethod
    def stamp(self, revision: str) -> Any:
        """Mark database as being at a specific revision without running migrations."""
        ...

    @abstractmethod
    def revision(self, message: str, file_type: str = "sql") -> Any:
        """Create a new migration file."""
        ...
