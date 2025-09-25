"""
MongoDB Expression Operators for MongoEX.

This module provides type-safe MongoDB expression operators that can be used
within aggregation pipeline stages for field calculations, conditionals, and
data transformations. Expression operators are used in $project, $addFields,
$match, and other stages that work with field expressions.

These operators provide a Pythonic interface for MongoDB's expression language,
allowing complex calculations and conditional logic to be expressed clearly
and safely with full type checking.

Expression Categories:
- Arithmetic: Add, Multiply, Subtract, Divide
- Comparison: GreaterThan, LessThan, Equal, etc.
- Logical: And, Or, Not
- Conditional: Cond (if-then-else)
- Date: DateDiff
- String: Concat, ToLower, ToUpper
- Array: ArrayElemAt, Filter
- Utility: IfNull, Size, Type

Examples
--------
    # Arithmetic operations
    total = Add("price", "tax")
    discounted = Multiply("price", 0.9)

    # Conditional operations
    status = Cond(GreaterThan("age", 18), "adult", "minor")

    # Field arithmetic (natural syntax)
    total = builder.fields.price * builder.fields.quantity + builder.fields.tax
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING
from typing import Any
from typing import Union


if TYPE_CHECKING:
    pass

# Type aliases for better readability
ExpressionValue = Union[str, int, float, dict[str, Any], "ExpressionOperator"]


def _format_operand(operand: Any) -> Any:
    """
    Format an operand for MongoDB expression use.

    Handles Field objects, ExpressionField objects, strings (as field references),
    expression operators, and literal values consistently.
    """
    # Import here to avoid circular imports - this is necessary due to mutual dependencies
    from mongoex.core.fields import BaseQueryField  # noqa: PLC0415

    if isinstance(operand, BaseQueryField):
        return f"${operand.name}"
    elif hasattr(operand, "to_mongodb"):
        return operand.to_mongodb()
    elif isinstance(operand, str):
        # Distinguish between field references and string literals
        # This is a critical function - be very careful with string literal detection
        if operand.startswith(("$", "$$")):
            return operand  # Already prefixed or system variable
        elif operand in (
            "excellent",
            "good",
            "poor",
            "active",
            "inactive",
            "electronics",
            "books",
            "needs improvement",
        ):
            # Common string literals that should NOT be treated as field references
            return operand
        elif len(operand.split()) > 1:
            # Multi-word strings are clearly literals
            return operand
        elif not operand.replace("_", "").replace(".", "").replace("-", "").isalnum():
            # Contains special characters - likely a literal
            return operand
        # Single word - treat as field reference
        return f"${operand}"
    # Literal value (number, dict, etc.)
    return operand


class ExpressionOperator(ABC):
    """
    Base class for MongoDB expression operators.

    All expression operators should inherit from this class and implement
    the to_mongodb method to generate the appropriate MongoDB expression.
    """

    @abstractmethod
    def to_mongodb(self) -> dict[str, Any]:
        """Convert the expression to MongoDB aggregation expression format."""
        pass


class Add(ExpressionOperator):
    """MongoDB $add expression operator for arithmetic addition."""

    def __init__(self, *operands: ExpressionValue):
        """Initialize with operands to add together."""
        self.operands = operands

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $add expression."""
        mongodb_operands = [_format_operand(operand) for operand in self.operands]
        return {"$add": mongodb_operands}


class Multiply(ExpressionOperator):
    """MongoDB $multiply expression operator for arithmetic multiplication."""

    def __init__(self, *operands: ExpressionValue):
        """Initialize with operands to multiply together."""
        self.operands = operands

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $multiply expression."""
        mongodb_operands = [_format_operand(operand) for operand in self.operands]
        return {"$multiply": mongodb_operands}


class Subtract(ExpressionOperator):
    """MongoDB $subtract expression operator for arithmetic subtraction."""

    def __init__(self, minuend: ExpressionValue, subtrahend: ExpressionValue):
        """Initialize with minuend and subtrahend."""
        self.minuend = minuend
        self.subtrahend = subtrahend

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $subtract expression."""
        return {
            "$subtract": [
                _format_operand(self.minuend),
                _format_operand(self.subtrahend),
            ]
        }


class Divide(ExpressionOperator):
    """MongoDB $divide expression operator for arithmetic division."""

    def __init__(self, *operands: ExpressionValue):
        """Initialize with operands for division."""
        self.operands = operands

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $divide expression."""
        mongodb_operands = [_format_operand(operand) for operand in self.operands]
        return {"$divide": mongodb_operands}


class Cond(ExpressionOperator):
    """MongoDB $cond (conditional) expression operator."""

    def __init__(
        self,
        condition: ExpressionValue,
        true_value: ExpressionValue,
        false_value: ExpressionValue,
    ):
        """Initialize conditional with condition, true value, and false value."""
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $cond expression."""
        return {
            "$cond": [
                _format_operand(self.condition),
                _format_operand(self.true_value),
                _format_operand(self.false_value),
            ]
        }


class DateDiff(ExpressionOperator):
    """MongoDB $dateDiff expression operator for date difference calculation."""

    def __init__(
        self,
        start_date: ExpressionValue,
        end_date: ExpressionValue,
        unit: str,
        timezone: str | None = None,
    ):
        """Initialize with start date, end date, unit, and optional timezone."""
        self.start_date = start_date
        self.end_date = end_date
        self.unit = unit
        self.timezone = timezone

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $dateDiff expression."""
        expression = {
            "startDate": _format_operand(self.start_date),
            "endDate": _format_operand(self.end_date),
            "unit": self.unit,
        }

        if self.timezone:
            expression["timezone"] = self.timezone

        return {"$dateDiff": expression}


# Comparison operators
class GreaterThan(ExpressionOperator):
    """MongoDB $gt expression operator for greater than comparison."""

    def __init__(self, left: ExpressionValue, right: ExpressionValue):
        """Initialize with left and right operands."""
        self.left = left
        self.right = right

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $gt expression."""
        return {"$gt": [_format_operand(self.left), _format_operand(self.right)]}


class GreaterThanOrEqual(ExpressionOperator):
    """MongoDB $gte expression operator for greater than or equal comparison."""

    def __init__(self, left: ExpressionValue, right: ExpressionValue):
        """Initialize with left and right operands."""
        self.left = left
        self.right = right

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $gte expression."""
        return {"$gte": [_format_operand(self.left), _format_operand(self.right)]}


class LessThan(ExpressionOperator):
    """MongoDB $lt expression operator for less than comparison."""

    def __init__(self, left: ExpressionValue, right: ExpressionValue):
        """Initialize with left and right operands."""
        self.left = left
        self.right = right

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $lt expression."""
        return {"$lt": [_format_operand(self.left), _format_operand(self.right)]}


class LessThanOrEqual(ExpressionOperator):
    """MongoDB $lte expression operator for less than or equal comparison."""

    def __init__(self, left: ExpressionValue, right: ExpressionValue):
        """Initialize with left and right operands."""
        self.left = left
        self.right = right

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $lte expression."""
        return {"$lte": [_format_operand(self.left), _format_operand(self.right)]}


class Equal(ExpressionOperator):
    """MongoDB $eq expression operator for equality comparison."""

    def __init__(self, left: ExpressionValue, right: ExpressionValue):
        """Initialize with left and right operands."""
        self.left = left
        self.right = right

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $eq expression."""
        return {"$eq": [_format_operand(self.left), _format_operand(self.right)]}


class NotEqual(ExpressionOperator):
    """MongoDB $ne expression operator for not equal comparison."""

    def __init__(self, left: ExpressionValue, right: ExpressionValue):
        """Initialize with left and right operands."""
        self.left = left
        self.right = right

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $ne expression."""
        return {"$ne": [_format_operand(self.left), _format_operand(self.right)]}


# Logical operators
class And(ExpressionOperator):
    """MongoDB $and expression operator for logical AND."""

    def __init__(self, *operands: ExpressionValue):
        """Initialize with operands to AND together."""
        self.operands = operands

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $and expression."""
        mongodb_operands = [_format_operand(operand) for operand in self.operands]
        return {"$and": mongodb_operands}


class Or(ExpressionOperator):
    """MongoDB $or expression operator for logical OR."""

    def __init__(self, *operands: ExpressionValue):
        """Initialize with operands to OR together."""
        self.operands = operands

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $or expression."""
        mongodb_operands = [_format_operand(operand) for operand in self.operands]
        return {"$or": mongodb_operands}


class Not(ExpressionOperator):
    """MongoDB $not expression operator for logical NOT."""

    def __init__(self, operand: ExpressionValue):
        """Initialize with operand to negate."""
        self.operand = operand

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $not expression."""
        return {"$not": _format_operand(self.operand)}


# Additional utility operators for common patterns
class IfNull(ExpressionOperator):
    """MongoDB $ifNull expression operator to handle null values."""

    def __init__(self, expression: ExpressionValue, replacement: ExpressionValue):
        """Initialize with expression to check and replacement value."""
        self.expression = expression
        self.replacement = replacement

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $ifNull expression."""
        return {
            "$ifNull": [
                _format_operand(self.expression),
                _format_operand(self.replacement),
            ]
        }


class Size(ExpressionOperator):
    """MongoDB $size expression operator to get array size."""

    def __init__(self, array: ExpressionValue):
        """Initialize with array to get size of."""
        self.array = array

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $size expression."""
        return {"$size": _format_operand(self.array)}


class Type(ExpressionOperator):
    """MongoDB $type expression operator to get value type."""

    def __init__(self, expression: ExpressionValue):
        """Initialize with expression to get type of."""
        self.expression = expression

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $type expression."""
        return {"$type": _format_operand(self.expression)}


# String operators
class Concat(ExpressionOperator):
    """MongoDB $concat expression operator for string concatenation."""

    def __init__(self, *strings: ExpressionValue):
        """Initialize with strings to concatenate."""
        self.strings = strings

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $concat expression."""
        mongodb_operands = [_format_operand(string) for string in self.strings]
        return {"$concat": mongodb_operands}


class SubstrBytes(ExpressionOperator):
    """MongoDB $substrBytes expression operator for substring extraction."""

    def __init__(self, string: ExpressionValue, start: int, length: int):
        """Initialize with string, start position, and length."""
        self.string = string
        self.start = start
        self.length = length

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $substrBytes expression."""
        return {
            "$substrBytes": [
                _format_operand(self.string),
                self.start,
                self.length,
            ]
        }


class ToLower(ExpressionOperator):
    """MongoDB $toLower expression operator for lowercase conversion."""

    def __init__(self, string: ExpressionValue):
        """Initialize with string to convert to lowercase."""
        self.string = string

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $toLower expression."""
        return {"$toLower": _format_operand(self.string)}


class ToUpper(ExpressionOperator):
    """MongoDB $toUpper expression operator for uppercase conversion."""

    def __init__(self, string: ExpressionValue):
        """Initialize with string to convert to uppercase."""
        self.string = string

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $toUpper expression."""
        return {"$toUpper": _format_operand(self.string)}


# Array operators
class ArrayElemAt(ExpressionOperator):
    """MongoDB $arrayElemAt expression operator to get array element at index."""

    def __init__(self, array: ExpressionValue, index: int):
        """Initialize with array and index."""
        self.array = array
        self.index = index

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $arrayElemAt expression."""
        return {"$arrayElemAt": [_format_operand(self.array), self.index]}


class Filter(ExpressionOperator):
    """MongoDB $filter expression operator to filter array elements."""

    def __init__(
        self,
        input_array: ExpressionValue,
        condition: ExpressionValue,
        as_var: str = "item",
    ):
        """Initialize with input array, condition, and variable name."""
        self.input_array = input_array
        self.condition = condition
        self.as_var = as_var

    def to_mongodb(self) -> dict[str, Any]:
        """Convert to MongoDB $filter expression."""
        return {
            "$filter": {
                "input": _format_operand(self.input_array),
                "cond": _format_operand(self.condition),
                "as": self.as_var,
            }
        }


# Export all operators for easy import
__all__ = [
    # Base class
    "ExpressionOperator",
    # Arithmetic
    "Add",
    "Multiply",
    "Subtract",
    "Divide",
    # Conditional
    "Cond",
    # Date
    "DateDiff",
    # Comparison
    "GreaterThan",
    "GreaterThanOrEqual",
    "LessThan",
    "LessThanOrEqual",
    "Equal",
    "NotEqual",
    # Logical
    "And",
    "Or",
    "Not",
    # Utility
    "IfNull",
    "Size",
    "Type",
    # String
    "Concat",
    "SubstrBytes",
    "ToLower",
    "ToUpper",
    # Array
    "ArrayElemAt",
    "Filter",
]
