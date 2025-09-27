# pyright: reportPrivateUsage=false
"""INSERT operation mixins.

Provides mixins for INSERT statement functionality including
INTO clauses, VALUES clauses, and INSERT FROM SELECT operations.
"""

from collections.abc import Sequence
from typing import Any, Optional, TypeVar, Union

from mypy_extensions import trait
from sqlglot import exp
from typing_extensions import Self

from sqlspec.exceptions import SQLBuilderError
from sqlspec.protocols import SQLBuilderProtocol

BuilderT = TypeVar("BuilderT", bound=SQLBuilderProtocol)

__all__ = ("InsertFromSelectMixin", "InsertIntoClauseMixin", "InsertValuesMixin")


@trait
class InsertIntoClauseMixin:
    """Mixin providing INTO clause for INSERT builders."""

    __slots__ = ()

    # Type annotations for PyRight - these will be provided by the base class
    def get_expression(self) -> Optional[exp.Expression]: ...
    def set_expression(self, expression: exp.Expression) -> None: ...

    def into(self, table: str) -> Self:
        """Set the target table for the INSERT statement.

        Args:
            table: The name of the table to insert data into.

        Raises:
            SQLBuilderError: If the current expression is not an INSERT statement.

        Returns:
            The current builder instance for method chaining.
        """
        current_expr = self.get_expression()
        if current_expr is None:
            self.set_expression(exp.Insert())
            current_expr = self.get_expression()

        if not isinstance(current_expr, exp.Insert):
            msg = "Cannot set target table on a non-INSERT expression."
            raise SQLBuilderError(msg)

        setattr(self, "_table", table)
        current_expr.set("this", exp.to_table(table))
        return self


@trait
class InsertValuesMixin:
    """Mixin providing VALUES and columns methods for INSERT builders."""

    __slots__ = ()

    # Type annotations for PyRight - these will be provided by the base class
    def get_expression(self) -> Optional[exp.Expression]: ...
    def set_expression(self, expression: exp.Expression) -> None: ...

    _columns: Any  # Provided by QueryBuilder

    def add_parameter(self, value: Any, name: Optional[str] = None) -> tuple[Any, str]:
        """Add parameter - provided by QueryBuilder."""
        msg = "Method must be provided by QueryBuilder subclass"
        raise NotImplementedError(msg)

    def _generate_unique_parameter_name(self, base_name: str) -> str:
        """Generate unique parameter name - provided by QueryBuilder."""
        msg = "Method must be provided by QueryBuilder subclass"
        raise NotImplementedError(msg)

    def columns(self, *columns: Union[str, exp.Expression]) -> Self:
        """Set the columns for the INSERT statement and synchronize the _columns attribute on the builder."""
        current_expr = self.get_expression()
        if current_expr is None:
            self.set_expression(exp.Insert())
            current_expr = self.get_expression()

        if not isinstance(current_expr, exp.Insert):
            msg = "Cannot set columns on a non-INSERT expression."
            raise SQLBuilderError(msg)

        # Get the current table from the expression
        current_this = current_expr.args.get("this")
        if current_this is None:
            msg = "Table must be set using .into() before setting columns."
            raise SQLBuilderError(msg)

        if columns:
            # Create identifiers for columns
            column_identifiers = [exp.to_identifier(col) if isinstance(col, str) else col for col in columns]

            # Get table name from current this
            table_name = current_this.this

            # Create Schema object with table and columns
            schema = exp.Schema(this=table_name, expressions=column_identifiers)
            current_expr.set("this", schema)
        # No columns specified - ensure we have just a Table object
        elif isinstance(current_this, exp.Schema):
            table_name = current_this.this
            current_expr.set("this", exp.Table(this=table_name))

        try:
            cols = self._columns
            if not columns:
                cols.clear()
            else:
                cols[:] = [col if isinstance(col, str) else str(col) for col in columns]
        except AttributeError:
            pass
        return self

    def values(self, *values: Any, **kwargs: Any) -> Self:
        """Add a row of values to the INSERT statement.

        Supports:
        - values(val1, val2, val3)
        - values(col1=val1, col2=val2)
        - values(mapping)

        Args:
            *values: Either positional values or a single mapping.
            **kwargs: Column-value pairs.

        Returns:
            The current builder instance for method chaining.
        """
        current_expr = self.get_expression()
        if current_expr is None:
            self.set_expression(exp.Insert())
            current_expr = self.get_expression()

        if not isinstance(current_expr, exp.Insert):
            msg = "Cannot add values to a non-INSERT expression."
            raise SQLBuilderError(msg)

        if kwargs:
            if values:
                msg = "Cannot mix positional values with keyword values."
                raise SQLBuilderError(msg)
            try:
                cols = self._columns
                if not cols:
                    self.columns(*kwargs.keys())
            except AttributeError:
                pass
            row_exprs = []
            for col, val in kwargs.items():
                if isinstance(val, exp.Expression):
                    row_exprs.append(val)
                else:
                    column_name = col if isinstance(col, str) else str(col)
                    if "." in column_name:
                        column_name = column_name.split(".")[-1]
                    param_name = self._generate_unique_parameter_name(column_name)
                    _, param_name = self.add_parameter(val, name=param_name)
                    row_exprs.append(exp.Placeholder(this=param_name))
        elif len(values) == 1 and hasattr(values[0], "items"):
            mapping = values[0]
            try:
                cols = self._columns
                if not cols:
                    self.columns(*mapping.keys())
            except AttributeError:
                pass
            row_exprs = []
            for col, val in mapping.items():
                if isinstance(val, exp.Expression):
                    row_exprs.append(val)
                else:
                    column_name = col if isinstance(col, str) else str(col)
                    if "." in column_name:
                        column_name = column_name.split(".")[-1]
                    param_name = self._generate_unique_parameter_name(column_name)
                    _, param_name = self.add_parameter(val, name=param_name)
                    row_exprs.append(exp.Placeholder(this=param_name))
        else:
            try:
                cols = self._columns
                if cols and len(values) != len(cols):
                    msg = f"Number of values ({len(values)}) does not match the number of specified columns ({len(cols)})."
                    raise SQLBuilderError(msg)
            except AttributeError:
                pass
            row_exprs = []
            for i, v in enumerate(values):
                if isinstance(v, exp.Expression):
                    row_exprs.append(v)
                else:
                    try:
                        cols = self._columns
                        if cols and i < len(cols):
                            column_name = str(cols[i]).split(".")[-1] if "." in str(cols[i]) else str(cols[i])
                            param_name = self._generate_unique_parameter_name(column_name)
                        else:
                            param_name = self._generate_unique_parameter_name(f"value_{i + 1}")
                    except AttributeError:
                        param_name = self._generate_unique_parameter_name(f"value_{i + 1}")
                    _, param_name = self.add_parameter(v, name=param_name)
                    row_exprs.append(exp.Placeholder(this=param_name))

        values_expr = exp.Values(expressions=[row_exprs])
        current_expr.set("expression", values_expr)
        return self

    def add_values(self, values: Sequence[Any]) -> Self:
        """Add a row of values to the INSERT statement (alternative signature).

        Args:
            values: Sequence of values for the row.

        Returns:
            The current builder instance for method chaining.
        """
        return self.values(*values)


@trait
class InsertFromSelectMixin:
    """Mixin providing INSERT ... SELECT support for INSERT builders."""

    __slots__ = ()

    # Type annotations for PyRight - these will be provided by the base class
    def get_expression(self) -> Optional[exp.Expression]: ...
    def set_expression(self, expression: exp.Expression) -> None: ...

    _table: Any  # Provided by QueryBuilder

    def add_parameter(self, value: Any, name: Optional[str] = None) -> tuple[Any, str]:
        """Add parameter - provided by QueryBuilder."""
        msg = "Method must be provided by QueryBuilder subclass"
        raise NotImplementedError(msg)

    def from_select(self, select_builder: Any) -> Self:
        """Sets the INSERT source to a SELECT statement.

        Args:
            select_builder: A SelectBuilder instance representing the SELECT query.

        Returns:
            The current builder instance for method chaining.

        Raises:
            SQLBuilderError: If the table is not set or the select_builder is invalid.
        """
        try:
            if not self._table:
                msg = "The target table must be set using .into() before adding values."
                raise SQLBuilderError(msg)
        except AttributeError:
            msg = "The target table must be set using .into() before adding values."
            raise SQLBuilderError(msg)
        current_expr = self.get_expression()
        if current_expr is None:
            self.set_expression(exp.Insert())
            current_expr = self.get_expression()

        if not isinstance(current_expr, exp.Insert):
            msg = "Cannot set INSERT source on a non-INSERT expression."
            raise SQLBuilderError(msg)
        subquery_parameters = select_builder._parameters
        if subquery_parameters:
            for p_name, p_value in subquery_parameters.items():
                self.add_parameter(p_value, name=p_name)
        select_expr = select_builder._expression
        if select_expr and isinstance(select_expr, exp.Select):
            current_expr.set("expression", select_expr.copy())
        else:
            msg = "SelectBuilder must have a valid SELECT expression."
            raise SQLBuilderError(msg)
        return self
