"""
MongoDB Operators Package for MongoEX.

This package provides comprehensive MongoDB operator support divided into two main categories:

Aggregation Operators:
    Operators used in aggregation pipelines for grouping, summarizing, and transforming data.
    Examples: Sum, Avg, First, Last, Push
    Used in: $group stages, accumulator operations

Expression Operators:
    Operators used within expressions for field calculations, conditionals, and transformations.
    Examples: Add, Multiply, Cond, DateDiff, GreaterThan
    Used in: $project, $addFields, $match expressions, conditional logic

This organization provides clear separation of concerns and makes it easier to find
and use the appropriate operators for different MongoDB operations.
"""

# Import aggregation operators
from .aggregation import AggregationOperator
from .aggregation import Avg
from .aggregation import First
from .aggregation import Last
from .aggregation import Push
from .aggregation import Sum

# Import expression operators
from .field import Add
from .field import And
from .field import ArrayElemAt
from .field import Concat
from .field import Cond
from .field import DateDiff
from .field import Divide
from .field import Equal
from .field import ExpressionOperator
from .field import Filter
from .field import GreaterThan
from .field import GreaterThanOrEqual
from .field import IfNull
from .field import LessThan
from .field import LessThanOrEqual
from .field import Multiply
from .field import Not
from .field import NotEqual
from .field import Or
from .field import Size
from .field import SubstrBytes
from .field import Subtract
from .field import ToLower
from .field import ToUpper
from .field import Type


__all__ = [
    # Base classes
    "AggregationOperator",
    "ExpressionOperator",
    # Aggregation operators
    "Avg",
    "First",
    "Last",
    "Push",
    "Sum",
    # Expression operators - Arithmetic
    "Add",
    "Multiply",
    "Subtract",
    "Divide",
    # Expression operators - Comparison
    "GreaterThan",
    "GreaterThanOrEqual",
    "LessThan",
    "LessThanOrEqual",
    "Equal",
    "NotEqual",
    # Expression operators - Logical
    "And",
    "Or",
    "Not",
    # Expression operators - Conditional
    "Cond",
    # Expression operators - Date
    "DateDiff",
    # Expression operators - Utility
    "IfNull",
    "Size",
    "Type",
    # Expression operators - String
    "Concat",
    "SubstrBytes",
    "ToLower",
    "ToUpper",
    # Expression operators - Array
    "ArrayElemAt",
    "Filter",
]
