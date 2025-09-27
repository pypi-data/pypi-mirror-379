"""INSERT statement builder.

Provides a fluent interface for building SQL INSERT queries with
parameter binding and validation.
"""

from typing import TYPE_CHECKING, Any, Final, Optional

from sqlglot import exp
from typing_extensions import Self

from sqlspec.builder._base import QueryBuilder
from sqlspec.builder._parsing_utils import extract_sql_object_expression
from sqlspec.builder.mixins import InsertFromSelectMixin, InsertIntoClauseMixin, InsertValuesMixin, ReturningClauseMixin
from sqlspec.core.result import SQLResult
from sqlspec.exceptions import SQLBuilderError
from sqlspec.utils.type_guards import has_expression_and_sql

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence


__all__ = ("Insert",)

ERR_MSG_TABLE_NOT_SET: Final[str] = "The target table must be set using .into() before adding values."
ERR_MSG_VALUES_COLUMNS_MISMATCH: Final[str] = (
    "Number of values ({values_len}) does not match the number of specified columns ({columns_len})."
)
ERR_MSG_INTERNAL_EXPRESSION_TYPE: Final[str] = "Internal error: expression is not an Insert instance as expected."
ERR_MSG_EXPRESSION_NOT_INITIALIZED: Final[str] = "Internal error: base expression not initialized."


class Insert(QueryBuilder, ReturningClauseMixin, InsertValuesMixin, InsertFromSelectMixin, InsertIntoClauseMixin):
    """Builder for INSERT statements.

    Constructs SQL INSERT queries with parameter binding and validation.
    """

    __slots__ = ("_columns", "_table", "_values_added_count")

    def __init__(self, table: Optional[str] = None, **kwargs: Any) -> None:
        """Initialize INSERT with optional table.

        Args:
            table: Target table name
            **kwargs: Additional QueryBuilder arguments
        """
        super().__init__(**kwargs)

        self._table: Optional[str] = None
        self._columns: list[str] = []
        self._values_added_count: int = 0

        self._initialize_expression()

        if table:
            self.into(table)

    def _create_base_expression(self) -> exp.Insert:
        """Create a base INSERT expression.

        This method is called by the base QueryBuilder during initialization.

        Returns:
            A new sqlglot Insert expression.
        """
        return exp.Insert()

    @property
    def _expected_result_type(self) -> "type[SQLResult]":
        """Specifies the expected result type for an INSERT query.

        Returns:
            The type of result expected for INSERT operations.
        """
        return SQLResult

    def _get_insert_expression(self) -> exp.Insert:
        """Safely gets and casts the internal expression to exp.Insert.

        Returns:
            The internal expression as exp.Insert.

        Raises:
            SQLBuilderError: If the expression is not initialized or is not an Insert.
        """
        if self._expression is None:
            raise SQLBuilderError(ERR_MSG_EXPRESSION_NOT_INITIALIZED)
        if not isinstance(self._expression, exp.Insert):
            raise SQLBuilderError(ERR_MSG_INTERNAL_EXPRESSION_TYPE)
        return self._expression

    def get_insert_expression(self) -> exp.Insert:
        """Get the insert expression (public API)."""
        return self._get_insert_expression()

    def values(self, *values: Any, **kwargs: Any) -> "Self":
        """Adds a row of values to the INSERT statement.

        This method can be called multiple times to insert multiple rows,
        resulting in a multi-row INSERT statement like `VALUES (...), (...)`.

        Supports:
        - values(val1, val2, val3)
        - values(col1=val1, col2=val2)
        - values(mapping)

        Args:
            *values: The values for the row to be inserted. The number of values
                     must match the number of columns set by `columns()`, if `columns()` was called
                     and specified any non-empty list of columns.
            **kwargs: Column-value pairs for named values.

        Returns:
            The current builder instance for method chaining.

        Raises:
            SQLBuilderError: If `into()` has not been called to set the table,
                             or if `columns()` was called with a non-empty list of columns
                             and the number of values does not match the number of specified columns.
        """
        if not self._table:
            raise SQLBuilderError(ERR_MSG_TABLE_NOT_SET)

        if kwargs:
            if values:
                msg = "Cannot mix positional values with keyword values."
                raise SQLBuilderError(msg)
            return self.values_from_dict(kwargs)

        if len(values) == 1:
            values_0 = values[0]
            if isinstance(values_0, dict):
                return self.values_from_dict(values_0)

        insert_expr = self.get_insert_expression()

        if self._columns and len(values) != len(self._columns):
            msg = ERR_MSG_VALUES_COLUMNS_MISMATCH.format(values_len=len(values), columns_len=len(self._columns))
            raise SQLBuilderError(msg)

        value_placeholders: list[exp.Expression] = []
        for i, value in enumerate(values):
            if isinstance(value, exp.Expression):
                value_placeholders.append(value)
            elif has_expression_and_sql(value):
                value_expr = extract_sql_object_expression(value, builder=self)
                value_placeholders.append(value_expr)
            else:
                if self._columns and i < len(self._columns):
                    column_str = str(self._columns[i])
                    column_name = column_str.rsplit(".", maxsplit=1)[-1] if "." in column_str else column_str
                    param_name = self.generate_unique_parameter_name(column_name)
                else:
                    param_name = self.generate_unique_parameter_name(f"value_{i + 1}")
                _, param_name = self.add_parameter(value, name=param_name)
                value_placeholders.append(exp.Placeholder(this=param_name))

        tuple_expr = exp.Tuple(expressions=value_placeholders)
        if self._values_added_count == 0:
            insert_expr.set("expression", exp.Values(expressions=[tuple_expr]))
        else:
            current_values = insert_expr.args.get("expression")
            if isinstance(current_values, exp.Values):
                current_values.expressions.append(tuple_expr)
            else:
                insert_expr.set("expression", exp.Values(expressions=[tuple_expr]))

        self._values_added_count += 1
        return self

    def values_from_dict(self, data: "Mapping[str, Any]") -> "Self":
        """Adds a row of values from a dictionary.

        This is a convenience method that automatically sets columns based on
        the dictionary keys and values based on the dictionary values.

        Args:
            data: A mapping of column names to values.

        Returns:
            The current builder instance for method chaining.

        Raises:
            SQLBuilderError: If `into()` has not been called to set the table.
        """
        if not self._table:
            raise SQLBuilderError(ERR_MSG_TABLE_NOT_SET)

        data_keys = list(data.keys())
        if not self._columns:
            self.columns(*data_keys)
        elif set(self._columns) != set(data_keys):
            msg = f"Dictionary keys {set(data_keys)} do not match existing columns {set(self._columns)}."
            raise SQLBuilderError(msg)

        return self.values(*[data[col] for col in self._columns])

    def values_from_dicts(self, data: "Sequence[Mapping[str, Any]]") -> "Self":
        """Adds multiple rows of values from a sequence of dictionaries.

        This is a convenience method for bulk inserts from structured data.

        Args:
            data: A sequence of mappings, each representing a row of data.

        Returns:
            The current builder instance for method chaining.

        Raises:
            SQLBuilderError: If `into()` has not been called to set the table,
                           or if dictionaries have inconsistent keys.
        """
        if not data:
            return self

        first_dict = data[0]
        if not self._columns:
            self.columns(*first_dict.keys())

        expected_keys = set(self._columns)
        for i, row_dict in enumerate(data):
            if set(row_dict.keys()) != expected_keys:
                msg = (
                    f"Dictionary at index {i} has keys {set(row_dict.keys())} "
                    f"which do not match expected keys {expected_keys}."
                )
                raise SQLBuilderError(msg)

        for row_dict in data:
            self.values(*[row_dict[col] for col in self._columns])

        return self

    def on_conflict(self, *columns: str) -> "ConflictBuilder":
        """Adds an ON CONFLICT clause with specified columns.

        Args:
            *columns: Column names that define the conflict. If no columns provided,
                     creates an ON CONFLICT without specific columns (catches all conflicts).

        Returns:
            A ConflictBuilder instance for chaining conflict resolution methods.

        Example:
            ```python
            sql.insert("users").values(id=1, name="John").on_conflict(
                "id"
            ).do_nothing()

            sql.insert("users").values(...).on_conflict(
                "email", "username"
            ).do_update(updated_at=sql.raw("NOW()"))

            sql.insert("users").values(...).on_conflict().do_nothing()
            ```
        """
        return ConflictBuilder(self, columns)

    def on_conflict_do_nothing(self, *columns: str) -> "Insert":
        """Adds an ON CONFLICT DO NOTHING clause (convenience method).

        Args:
            *columns: Column names that define the conflict. If no columns provided,
                     creates an ON CONFLICT without specific columns.

        Returns:
            The current builder instance for method chaining.

        Note:
            This is a convenience method. For more control, use on_conflict().do_nothing().
        """
        return self.on_conflict(*columns).do_nothing()

    def on_duplicate_key_update(self, **kwargs: Any) -> "Insert":
        """Adds MySQL-style ON DUPLICATE KEY UPDATE clause.

        Args:
            **kwargs: Column-value pairs to update on duplicate key.

        Returns:
            The current builder instance for method chaining.

        Note:
            This method creates MySQL-specific ON DUPLICATE KEY UPDATE syntax.
            For PostgreSQL, use on_conflict() instead.
        """
        if not kwargs:
            return self

        insert_expr = self._get_insert_expression()

        set_expressions = []
        for col, val in kwargs.items():
            if has_expression_and_sql(val):
                value_expr = extract_sql_object_expression(val, builder=self)
            elif isinstance(val, exp.Expression):
                value_expr = val
            else:
                param_name = self.generate_unique_parameter_name(col)
                _, param_name = self.add_parameter(val, name=param_name)
                value_expr = exp.Placeholder(this=param_name)

            set_expressions.append(exp.EQ(this=exp.column(col), expression=value_expr))

        on_conflict = exp.OnConflict(duplicate=True, action=exp.var("UPDATE"), expressions=set_expressions or None)

        insert_expr.set("conflict", on_conflict)

        return self


class ConflictBuilder:
    """Builder for ON CONFLICT clauses in INSERT statements.

    Constructs conflict resolution clauses using PostgreSQL-style syntax,
    which SQLGlot can transpile to other dialects.
    """

    __slots__ = ("_columns", "_insert_builder")

    def __init__(self, insert_builder: "Insert", columns: tuple[str, ...]) -> None:
        """Initialize ConflictBuilder.

        Args:
            insert_builder: The parent Insert builder
            columns: Column names that define the conflict
        """
        self._insert_builder = insert_builder
        self._columns = columns

    def do_nothing(self) -> "Insert":
        """Add DO NOTHING conflict resolution.

        Returns:
            The parent Insert builder for method chaining.

        Example:
            ```python
            sql.insert("users").values(id=1, name="John").on_conflict(
                "id"
            ).do_nothing()
            ```
        """
        insert_expr = self._insert_builder.get_insert_expression()

        conflict_keys = [exp.to_identifier(col) for col in self._columns] if self._columns else None
        on_conflict = exp.OnConflict(conflict_keys=conflict_keys, action=exp.var("DO NOTHING"))

        insert_expr.set("conflict", on_conflict)
        return self._insert_builder

    def do_update(self, **kwargs: Any) -> "Insert":
        """Add DO UPDATE conflict resolution with SET clauses.

        Args:
            **kwargs: Column-value pairs to update on conflict.

        Returns:
            The parent Insert builder for method chaining.

        Example:
            ```python
            sql.insert("users").values(id=1, name="John").on_conflict(
                "id"
            ).do_update(
                name="Updated Name", updated_at=sql.raw("NOW()")
            )
            ```
        """
        insert_expr = self._insert_builder.get_insert_expression()

        set_expressions = []
        for col, val in kwargs.items():
            if has_expression_and_sql(val):
                value_expr = extract_sql_object_expression(val, builder=self._insert_builder)
            elif isinstance(val, exp.Expression):
                value_expr = val
            else:
                param_name = self._insert_builder.generate_unique_parameter_name(col)
                _, param_name = self._insert_builder.add_parameter(val, name=param_name)
                value_expr = exp.Placeholder(this=param_name)

            set_expressions.append(exp.EQ(this=exp.column(col), expression=value_expr))

        conflict_keys = [exp.to_identifier(col) for col in self._columns] if self._columns else None
        on_conflict = exp.OnConflict(
            conflict_keys=conflict_keys, action=exp.var("DO UPDATE"), expressions=set_expressions or None
        )

        insert_expr.set("conflict", on_conflict)
        return self._insert_builder
