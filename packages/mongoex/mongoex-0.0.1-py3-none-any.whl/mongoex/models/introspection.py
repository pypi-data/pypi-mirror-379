"""
Model utilities for handling dataclasses and Pydantic models in MongoEX.

RIGID IMPLEMENTATION: This module enforces strict Annotated syntax for all
aggregation models. No fallbacks or defaults - if a model doesn't follow
the Annotated[type, AggregationOperator] pattern, it will fail.
"""

from dataclasses import fields as dataclass_fields
from dataclasses import is_dataclass
from typing import Any
from typing import get_args
from typing import get_origin

from mongoex.operators import AggregationOperator


class UnsupportedModelError(ValueError):
    """Raised when a model type is not supported by MongoEX."""

    def __init__(self, model: type) -> None:
        message = (
            f"Unsupported model type: {model}. "
            "Must be a dataclass, Pydantic model, or have __annotations__"
        )
        super().__init__(message)


class InvalidAggregationModelError(ValueError):
    """Raised when a model doesn't use proper Annotated syntax for aggregations."""

    def __init__(self, model: type, missing_fields: list[str]) -> None:
        fields_str = ", ".join(missing_fields)
        message = (
            f"Model {model.__name__} is invalid for aggregation operations.\n"
            f"Fields [{fields_str}] must use "
            "Annotated[type, AggregationOperator] syntax.\n"
            "Example: total_sales: Annotated[float, Sum('amount')]"
        )
        super().__init__(message)


def is_pydantic_model(cls: type) -> bool:
    """Check if a class is a Pydantic model."""
    try:
        return hasattr(cls, "model_fields") or hasattr(cls, "__pydantic_model__")
    except Exception:
        return False


def extract_model_fields(model: type[Any]) -> dict[str, Any]:
    """Extract field names and types from a dataclass or Pydantic model."""
    if is_dataclass(model):
        return {field.name: field.type for field in dataclass_fields(model)}
    elif is_pydantic_model(model):
        if hasattr(model, "model_fields"):  # Pydantic v2
            return {
                name: field.annotation for name, field in model.model_fields.items()
            }
        elif hasattr(model, "__fields__"):  # Pydantic v1
            return {name: field.type_ for name, field in model.__fields__.items()}
    elif hasattr(model, "__annotations__"):
        # Collect annotations from inheritance chain (MRO)
        all_annotations: dict[str, Any] = {}
        for base in reversed(model.__mro__):
            if hasattr(base, "__annotations__"):
                all_annotations.update(base.__annotations__)
        return all_annotations

    raise UnsupportedModelError(model)


def extract_annotated_operators(model: type[Any]) -> dict[str, AggregationOperator]:
    """
    Extract aggregation operations from Annotated field types.

    Only extracts operators from properly annotated fields.
    Fields without Annotated[type, AggregationOperator] are ignored.

    Returns
    -------
    dict[str, AggregationOperator]
        Dictionary mapping field names to their AggregationOperator instances.
    """
    fields_map = extract_model_fields(model)
    operators: dict[str, AggregationOperator] = {}

    for field_name, field_type in fields_map.items():
        if _is_annotated_field(field_type):
            operator = _extract_operator_from_annotated(field_type)
            if operator:
                operators[field_name] = operator

    return operators


def _is_annotated_field(field_type: type) -> bool:
    """Check if a field type is an Annotated type."""
    origin = get_origin(field_type)
    if origin is None:
        return False
    return hasattr(origin, "__name__") and "Annotated" in str(origin)


def _extract_operator_from_annotated(field_type: type) -> AggregationOperator | None:
    """Extract AggregationOperator from Annotated type metadata."""
    min_args = 2
    args = get_args(field_type)
    if len(args) >= min_args:
        # First arg is the actual type, rest are metadata
        metadata = args[1:]
        for meta in metadata:
            if isinstance(meta, AggregationOperator):
                return meta
    return None


def validate_aggregation_model(model: type[Any]) -> None:
    """
    RIGID validation: ALL fields must use Annotated[type, AggregationOperator].

    Exception: '_id' field is allowed without annotation as it's MongoDB standard.

    Raises
    ------
    InvalidAggregationModelError
        If any field doesn't use proper Annotated[type, AggregationOperator] syntax.
    """
    fields_map = extract_model_fields(model)
    annotated_fields = extract_annotated_operators(model)

    missing_fields = [
        field_name
        for field_name in fields_map.keys()
        if field_name not in annotated_fields and field_name != "_id"
    ]

    if missing_fields:
        raise InvalidAggregationModelError(model, missing_fields)
