"""Model utilities for dataclass and Pydantic support."""

from mongoex.models.introspection import InvalidAggregationModelError
from mongoex.models.introspection import extract_annotated_operators
from mongoex.models.introspection import extract_model_fields
from mongoex.models.introspection import is_pydantic_model
from mongoex.models.introspection import validate_aggregation_model


__all__ = [
    "InvalidAggregationModelError",
    "extract_annotated_operators",
    "extract_model_fields",
    "is_pydantic_model",
    "validate_aggregation_model",
]
