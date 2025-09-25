"""Core expression and field system for MongoEX."""

from mongoex.core.expressions import AndExpression
from mongoex.core.expressions import ComparisonExpression
from mongoex.core.expressions import OrExpression
from mongoex.core.expressions import QueryExpression
from mongoex.core.fields import Field
from mongoex.core.fields import create_proxy


__all__ = [
    # Expressions
    "AndExpression",
    "ComparisonExpression",
    "OrExpression",
    "QueryExpression",
    # Fields
    "Field",
    "create_proxy",
]
