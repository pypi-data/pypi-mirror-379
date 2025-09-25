"""
MongoEX - Type-Safe MongoDB Query Builder.

A modern Python library for building MongoDB aggregation pipelines with full
type safety, IDE autocompletion, and comprehensive validation.

MongoEX provides a fluent, type-safe API for constructing MongoDB aggregation
pipelines using Python dataclasses or Pydantic models. It eliminates the need
to write raw MongoDB queries while providing excellent IDE support and runtime
validation.

Key Features
------------
- **Type Safety**: Full type checking with dataclass/Pydantic model support
- **Fluent API**: Method chaining for readable pipeline construction
- **Field Validation**: Automatic validation of field names against models
- **Rich Error Messages**: Enhanced error reporting with suggestions
- **Query Expression Builder**: Intuitive comparison and logical operators
- **Pipeline Conversion**: Convert existing MongoDB JSON pipelines to MongoEX code

Query APIs
----------
MongoEX offers two complementary approaches for field referencing:

1. **Field-based API**: Direct field creation
   >>> Field("price") > 100

2. **Builder-integrated API**: Type-safe model-based fields via PipelineBuilder
   >>> builder.fields.price > 100

Examples
--------
Basic usage with dataclass models:

>>> from mongoex import PipelineBuilder, Field
>>> from mongoex.operators import Sum, Avg
>>> from dataclasses import dataclass

>>> @dataclass
... class Sale:
...     item: str
...     price: float
...     quantity: int

>>> # Method 1: Direct Field usage
>>> builder = PipelineBuilder(Sale)
>>> pipeline = builder.match(Field("price") > 100).group(
...     by="item", total_quantity=Sum("quantity"), avg_price=Avg("price")
... )

>>> # Method 2: Builder.fields usage (recommended for type safety)
>>> pipeline = builder.match(
...     (builder.fields.price > 100) & (builder.fields.item != "book")
... ).group(by="item", total_quantity=Sum("quantity"), avg_price=Avg("price"))

>>> # Use directly with PyMongo (no build() call needed)
>>> result = db.collection.aggregate(pipeline)

Advanced Features
-----------------
Enhanced validation with detailed error messages:

>>> try:
...     builder.match(builder.fields.invalid_field == "test")
... except QueryValidationError as e:
...     print(e)  # Provides suggestions and context

Pipeline conversion from existing MongoDB JSON:

>>> from mongoex.utils import to_mongoex
>>> json_pipeline = [{"$match": {"price": {"$gt": 100}}}]
>>> code = to_mongoex(json_pipeline, "Sale")
>>> print(code)  # Generates equivalent MongoEX code
"""

from mongoex.__version__ import __version__

# Core pipeline builder
from mongoex.builder import PipelineBuilder

# Core expression types (advanced usage)
from mongoex.core import AndExpression
from mongoex.core import ComparisonExpression
from mongoex.core import Field
from mongoex.core import OrExpression
from mongoex.core import QueryExpression
from mongoex.core import create_proxy

# Aggregation operators
from mongoex.operators.aggregation import AggregationOperator
from mongoex.operators.aggregation import Avg
from mongoex.operators.aggregation import First
from mongoex.operators.aggregation import Last
from mongoex.operators.aggregation import Push
from mongoex.operators.aggregation import Sum

# Expression operators for computed fields and projections
from mongoex.operators.field import Add
from mongoex.operators.field import Cond
from mongoex.operators.field import DateDiff
from mongoex.operators.field import Divide
from mongoex.operators.field import ExpressionOperator
from mongoex.operators.field import GreaterThan as Greater
from mongoex.operators.field import GreaterThanOrEqual as GreaterEqual
from mongoex.operators.field import LessThan as Less
from mongoex.operators.field import LessThanOrEqual as LessEqual
from mongoex.operators.field import Multiply
from mongoex.operators.field import NotEqual
from mongoex.operators.field import Subtract

# Enhanced validation and error handling
from mongoex.validation import QueryValidationError
from mongoex.validation import create_field_validator


# Cleaned up public API - removed duplicated __all__ and unused symbols
__all__ = [
    "Add",
    "AggregationOperator",
    "AndExpression",
    "Avg",
    "ComparisonExpression",
    "Cond",
    "DateDiff",
    "Divide",
    "ExpressionOperator",
    "Field",
    "First",
    "Greater",
    "GreaterEqual",
    "Last",
    "Less",
    "LessEqual",
    "Multiply",
    "NotEqual",
    "OrExpression",
    "PipelineBuilder",
    "Push",
    "QueryExpression",
    "QueryValidationError",
    "Subtract",
    "Sum",
    "__version__",
    "create_field_validator",
    "create_proxy",
]
