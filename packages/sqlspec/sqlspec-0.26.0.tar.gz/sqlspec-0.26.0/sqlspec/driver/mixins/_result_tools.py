# ruff: noqa: C901
"""Result handling and schema conversion mixins for database drivers."""

import datetime
import logging
from collections.abc import Sequence
from enum import Enum
from functools import partial
from pathlib import Path, PurePath
from typing import Any, Callable, Final, Optional, overload
from uuid import UUID

from mypy_extensions import trait

from sqlspec.exceptions import SQLSpecError
from sqlspec.typing import (
    CATTRS_INSTALLED,
    NUMPY_INSTALLED,
    ModelDTOT,
    ModelT,
    attrs_asdict,
    cattrs_structure,
    cattrs_unstructure,
    convert,
    get_type_adapter,
)
from sqlspec.utils.data_transformation import transform_dict_keys
from sqlspec.utils.text import camelize, kebabize, pascalize
from sqlspec.utils.type_guards import (
    get_msgspec_rename_config,
    is_attrs_schema,
    is_dataclass,
    is_dict,
    is_msgspec_struct,
    is_pydantic_model,
)

__all__ = ("_DEFAULT_TYPE_DECODERS", "_default_msgspec_deserializer")


logger = logging.getLogger(__name__)


_DATETIME_TYPES: Final[set[type]] = {datetime.datetime, datetime.date, datetime.time}


def _is_list_type_target(target_type: Any) -> bool:
    """Check if target type is a list type (e.g., list[float])."""
    try:
        return hasattr(target_type, "__origin__") and target_type.__origin__ is list
    except (AttributeError, TypeError):
        return False


def _convert_numpy_to_list(target_type: Any, value: Any) -> Any:
    """Convert numpy array to list if target is a list type."""
    if not NUMPY_INSTALLED:
        return value

    import numpy as np

    if isinstance(value, np.ndarray) and _is_list_type_target(target_type):
        return value.tolist()

    return value


_DEFAULT_TYPE_DECODERS: Final[list[tuple[Callable[[Any], bool], Callable[[Any, Any], Any]]]] = [
    (lambda x: x is UUID, lambda t, v: t(v.hex)),
    (lambda x: x is datetime.datetime, lambda t, v: t(v.isoformat())),
    (lambda x: x is datetime.date, lambda t, v: t(v.isoformat())),
    (lambda x: x is datetime.time, lambda t, v: t(v.isoformat())),
    (lambda x: x is Enum, lambda t, v: t(v.value)),
    (_is_list_type_target, _convert_numpy_to_list),
]


def _default_msgspec_deserializer(
    target_type: Any, value: Any, type_decoders: "Optional[Sequence[tuple[Any, Any]]]" = None
) -> Any:
    """Convert msgspec types with type decoder support.

    Args:
        target_type: Type to convert to
        value: Value to convert
        type_decoders: Optional sequence of (predicate, decoder) pairs

    Returns:
        Converted value or original value if conversion not applicable
    """
    # Handle numpy arrays first for list types
    if NUMPY_INSTALLED:
        import numpy as np

        if isinstance(value, np.ndarray) and _is_list_type_target(target_type):
            return value.tolist()

    if type_decoders:
        for predicate, decoder in type_decoders:
            if predicate(target_type):
                return decoder(target_type, value)

    if target_type is UUID and isinstance(value, UUID):
        return value.hex

    if target_type in _DATETIME_TYPES and hasattr(value, "isoformat"):
        return value.isoformat()  # pyright: ignore

    if isinstance(target_type, type) and issubclass(target_type, Enum) and isinstance(value, Enum):
        return value.value

    # Check if value is already the correct type (but avoid parameterized generics)
    try:
        if isinstance(target_type, type) and isinstance(value, target_type):
            return value
    except TypeError:
        # Handle parameterized generics like list[int] which can't be used with isinstance
        pass

    if isinstance(target_type, type):
        try:
            if issubclass(target_type, (Path, PurePath)) or issubclass(target_type, UUID):
                return target_type(str(value))
        except (TypeError, ValueError):
            pass

    return value


@trait
class ToSchemaMixin:
    """Mixin providing data transformation methods for various schema types."""

    __slots__ = ()

    @overload
    @staticmethod
    def to_schema(data: "list[dict[str, Any]]") -> "list[dict[str, Any]]": ...
    @overload
    @staticmethod
    def to_schema(data: "list[dict[str, Any]]", *, schema_type: "type[ModelDTOT]") -> "list[ModelDTOT]": ...
    @overload
    @staticmethod
    def to_schema(data: "list[dict[str, Any]]", *, schema_type: None = None) -> "list[dict[str, Any]]": ...
    @overload
    @staticmethod
    def to_schema(data: "dict[str, Any]") -> "dict[str, Any]": ...
    @overload
    @staticmethod
    def to_schema(data: "dict[str, Any]", *, schema_type: "type[ModelDTOT]") -> "ModelDTOT": ...
    @overload
    @staticmethod
    def to_schema(data: "dict[str, Any]", *, schema_type: None = None) -> "dict[str, Any]": ...
    @overload
    @staticmethod
    def to_schema(data: "list[ModelT]") -> "list[ModelT]": ...
    @overload
    @staticmethod
    def to_schema(data: "list[ModelT]", *, schema_type: "type[ModelDTOT]") -> "list[ModelDTOT]": ...
    @overload
    @staticmethod
    def to_schema(data: "list[ModelT]", *, schema_type: None = None) -> "list[ModelT]": ...
    @overload
    @staticmethod
    def to_schema(data: "ModelT") -> "ModelT": ...
    @overload
    @staticmethod
    def to_schema(data: Any, *, schema_type: None = None) -> Any: ...

    @staticmethod
    def to_schema(data: Any, *, schema_type: "Optional[type[ModelDTOT]]" = None) -> Any:
        """Convert data to a specified schema type.

        Args:
            data: Input data to convert
            schema_type: Target schema type for conversion

        Returns:
            Converted data in the specified schema type

        Raises:
            SQLSpecError: If schema_type is not a supported type
        """
        if schema_type is None:
            return data
        if is_dataclass(schema_type):
            if isinstance(data, list):
                result: list[Any] = []
                for item in data:
                    if is_dict(item):
                        result.append(schema_type(**dict(item)))  # type: ignore[operator]
                    else:
                        result.append(item)
                return result
            if is_dict(data):
                return schema_type(**dict(data))  # type: ignore[operator]
            if isinstance(data, dict):
                return schema_type(**data)  # type: ignore[operator]
            return data
        if is_msgspec_struct(schema_type):
            rename_config = get_msgspec_rename_config(schema_type)  # type: ignore[arg-type]
            deserializer = partial(_default_msgspec_deserializer, type_decoders=_DEFAULT_TYPE_DECODERS)

            # Transform field names if rename configuration exists
            transformed_data = data
            if (rename_config and is_dict(data)) or (isinstance(data, Sequence) and data and is_dict(data[0])):
                try:
                    converter = None
                    if rename_config == "camel":
                        converter = camelize
                    elif rename_config == "kebab":
                        converter = kebabize
                    elif rename_config == "pascal":
                        converter = pascalize

                    if converter is not None:
                        if isinstance(data, Sequence):
                            transformed_data = [
                                transform_dict_keys(item, converter) if is_dict(item) else item for item in data
                            ]
                        else:
                            transformed_data = transform_dict_keys(data, converter) if is_dict(data) else data
                except Exception as e:
                    logger.debug("Field name transformation failed for msgspec schema: %s", e)
                    transformed_data = data

            # Pre-process numpy arrays to lists before msgspec conversion
            if NUMPY_INSTALLED:
                try:
                    import numpy as np

                    def _convert_numpy_arrays_in_data(obj: Any) -> Any:
                        """Recursively convert numpy arrays to lists in data structures."""
                        if isinstance(obj, np.ndarray):
                            return obj.tolist()
                        if isinstance(obj, dict):
                            return {k: _convert_numpy_arrays_in_data(v) for k, v in obj.items()}
                        if isinstance(obj, (list, tuple)):
                            return type(obj)(_convert_numpy_arrays_in_data(item) for item in obj)
                        return obj

                    transformed_data = _convert_numpy_arrays_in_data(transformed_data)
                except ImportError:
                    pass

            if not isinstance(transformed_data, Sequence):
                return convert(obj=transformed_data, type=schema_type, from_attributes=True, dec_hook=deserializer)
            return convert(obj=transformed_data, type=list[schema_type], from_attributes=True, dec_hook=deserializer)  # type: ignore[valid-type]
        if is_pydantic_model(schema_type):
            if not isinstance(data, Sequence):
                adapter = get_type_adapter(schema_type)
                return adapter.validate_python(data, from_attributes=True)
            list_adapter = get_type_adapter(list[schema_type])  # type: ignore[valid-type]
            return list_adapter.validate_python(data, from_attributes=True)
        if is_attrs_schema(schema_type):
            if CATTRS_INSTALLED:
                if isinstance(data, Sequence):
                    return cattrs_structure(data, list[schema_type])  # type: ignore[valid-type]
                if hasattr(data, "__attrs_attrs__"):
                    unstructured_data = cattrs_unstructure(data)
                    return cattrs_structure(unstructured_data, schema_type)
                return cattrs_structure(data, schema_type)
            if isinstance(data, list):
                attrs_result: list[Any] = []
                for item in data:
                    if hasattr(item, "keys"):
                        attrs_result.append(schema_type(**dict(item)))
                    else:
                        attrs_result.append(schema_type(**attrs_asdict(item)))
                return attrs_result
            if hasattr(data, "keys"):
                return schema_type(**dict(data))
            if isinstance(data, dict):
                return schema_type(**data)
            return data
        msg = "`schema_type` should be a valid Dataclass, Pydantic model, Msgspec struct, or Attrs class"
        raise SQLSpecError(msg)
