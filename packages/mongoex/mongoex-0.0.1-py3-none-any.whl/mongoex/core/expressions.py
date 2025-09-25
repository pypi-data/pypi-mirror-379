"""
Query expression classes for type-safe MongoDB query construction.

This module provides the core expression classes that form the foundation of
MongoEX's type-safe query building system. These classes enable intuitive
construction of MongoDB queries using Python operators and method chaining.

The expression system supports:
- Comparison operations (>, <, ==, !=, etc.)
- Logical combinations (& for AND, | for OR)
- Automatic MongoDB query generation
- Type-safe query validation
"""

from __future__ import annotations

from typing import Any


class QueryExpression:
    """
    Base class for all MongoDB query expressions.

    QueryExpression serves as the foundation for building type-safe MongoDB queries
    in MongoEX. It provides the interface for converting Python expressions into
    MongoDB query dictionaries and supports logical combination of expressions.

    This class defines the contract that all query expressions must follow:
    - Convert to MongoDB query format via to_mongodb()
    - Support logical AND (&) and OR (|) operations
    - Enable method chaining for complex query construction

    All concrete expression classes (ComparisonExpression, AndExpression, etc.)
    inherit from this base class and implement the to_mongodb() method.

    Examples
    --------
    Query expressions are typically created through Field objects:

    >>> from mongoex import Field
    >>> price = Field("price")
    >>> category = Field("category")

    >>> # Create expressions using comparison operators
    >>> price_expr = price > 100
    >>> category_expr = category == "electronics"

    >>> # Combine expressions using logical operators
    >>> combined = price_expr & category_expr  # Returns AndExpression
    >>> alternative = price_expr | category_expr  # Returns OrExpression

    >>> # Convert to MongoDB format
    >>> mongo_query = combined.to_mongodb()
    >>> # Result: {"$and": [{"price": {"$gt": 100}}, {"category": "electronics"}]}
    """

    def to_mongodb(self) -> dict[str, Any]:
        """
        Convert the expression to a MongoDB query dictionary.

        This abstract method must be implemented by all subclasses to define
        how the expression translates to MongoDB's query language format.

        Returns
        -------
        dict[str, Any]
            MongoDB query dictionary ready for use in aggregation pipelines,
            find() operations, or other MongoDB queries.

        Raises
        ------
        NotImplementedError
            If called on the base class or if a subclass doesn't implement it.

        Examples
        --------
        >>> expr = Field("price") > 100
        >>> mongo_query = expr.to_mongodb()
        >>> # Returns: {"price": {"$gt": 100}}
        """
        raise NotImplementedError("Subclasses must implement to_mongodb()")

    def __and__(self, other: QueryExpression) -> AndExpression:
        """
        Combine expressions with logical AND using the & operator.

        Creates an AndExpression that represents the logical AND of this
        expression and another expression.

        Parameters
        ----------
        other : QueryExpression
            The expression to combine with this one using AND logic.

        Returns
        -------
        AndExpression
            A new expression representing (self AND other).

        Examples
        --------
        >>> price_expr = Field("price") > 100
        >>> status_expr = Field("status") == "active"
        >>> combined = price_expr & status_expr
        >>> mongo_query = combined.to_mongodb()
        >>> # Result: {"$and": [{"price": {"$gt": 100}}, {"status": "active"}]}
        """
        return AndExpression([self, other])

    def __or__(self, other: QueryExpression) -> OrExpression:
        """
        Combine expressions with logical OR using the | operator.

        Creates an OrExpression that represents the logical OR of this
        expression and another expression.

        Parameters
        ----------
        other : QueryExpression
            The expression to combine with this one using OR logic.

        Returns
        -------
        OrExpression
            A new expression representing (self OR other).

        Examples
        --------
        >>> high_price = Field("price") > 1000
        >>> on_sale = Field("discount") > 0.2
        >>> combined = high_price | on_sale
        >>> mongo_query = combined.to_mongodb()
        >>> # Result: {"$or": [{"price": {"$gt": 1000}}, {"discount": {"$gt": 0.2}}]}
        """
        return OrExpression([self, other])


class ComparisonExpression(QueryExpression):
    """
    MongoDB comparison operation between a field and a value.

    ComparisonExpression represents a single comparison operation such as
    equality, greater than, less than, etc. It forms the atomic unit of
    MongoDB queries and can be combined with other expressions using
    logical operators.

    This class handles the translation of Python comparison operators
    to MongoDB query operators and provides optimizations like using
    MongoDB's shorthand syntax for equality comparisons.

    Parameters
    ----------
    field_name : str
        The MongoDB field name to compare against.
    operator : str
        The MongoDB comparison operator (e.g., '$eq', '$gt', '$lt', '$in').
    value : Any
        The value to compare the field against.

    Examples
    --------
    Comparison expressions are typically created through Field operations:

    >>> from mongoex import Field
    >>> price = Field("price")

    >>> # Different comparison operations
    >>> equal_expr = price == 100  # ComparisonExpression("price", "$eq", 100)
    >>> greater_expr = price > 100  # ComparisonExpression("price", "$gt", 100)
    >>> # ComparisonExpression("price", "$in", [100, 200])
    >>> in_expr = price.in_([100, 200])

    >>> # Convert to MongoDB format
    >>> equal_expr.to_mongodb()  # Returns: {"price": 100}
    >>> greater_expr.to_mongodb()  # Returns: {"price": {"$gt": 100}}
    >>> in_expr.to_mongodb()  # Returns: {"price": {"$in": [100, 200]}}
    """

    def __init__(self, field_name: str, operator: str, value: Any) -> None:
        self.field_name = field_name
        self.operator = operator
        self.value = value

    def to_mongodb(self) -> dict[str, Any]:
        """
        Convert the comparison to MongoDB query format.

        Translates the comparison expression into a MongoDB query dictionary.
        Provides optimization for equality comparisons by using MongoDB's
        shorthand syntax when the operator is '$eq'.

        Returns
        -------
        dict[str, Any]
            MongoDB query dictionary. For equality comparisons, returns
            {field_name: value}. For other operators, returns
            {field_name: {operator: value}}.

        Examples
        --------
        >>> expr1 = ComparisonExpression("price", "$eq", 100)
        >>> expr1.to_mongodb()
        {"price": 100}

        >>> expr2 = ComparisonExpression("price", "$gt", 100)
        >>> expr2.to_mongodb()
        {"price": {"$gt": 100}}
        """
        if self.operator == "$eq":
            # MongoDB allows shorthand for equality
            return {self.field_name: self.value}
        return {self.field_name: {self.operator: self.value}}


class AndExpression(QueryExpression):
    """
    Logical AND operation combining multiple query expressions.

    AndExpression represents the logical conjunction of multiple query expressions
    using MongoDB's $and operator. It optimizes single-expression cases by
    returning the expression directly instead of wrapping it in $and.

    The class supports efficient chaining of multiple AND operations and
    automatically flattens nested AND expressions for better performance.

    Parameters
    ----------
    expressions : list[QueryExpression]
        List of query expressions to combine with AND logic.
        All expressions must be valid QueryExpression instances.

    Examples
    --------
    AndExpression is typically created using the & operator:

    >>> from mongoex import Field
    >>> price = Field("price")
    >>> category = Field("category")
    >>> status = Field("status")

    >>> # Create expressions
    >>> price_expr = price > 100
    >>> category_expr = category == "electronics"
    >>> status_expr = status == "active"

    >>> # Combine with AND
    >>> and_expr = price_expr & category_expr
    >>> # Result: AndExpression([price_expr, category_expr])

    >>> # Chain multiple ANDs
    >>> complex_expr = and_expr & status_expr
    >>> # Result: AndExpression([price_expr, category_expr, status_expr])

    >>> # Convert to MongoDB format
    >>> and_expr.to_mongodb()
    >>> # Returns: {"$and": [{"price": {"$gt": 100}}, {"category": "electronics"}]}
    """

    def __init__(self, expressions: list[QueryExpression]) -> None:
        self.expressions = expressions

    def to_mongodb(self) -> dict[str, Any]:
        """
        Convert to MongoDB $and query with single-expression optimization.

        Translates the AND expression to MongoDB format. When only one expression
        is present, returns that expression directly to avoid unnecessary $and
        wrapping, which improves query performance.

        Returns
        -------
        dict[str, Any]
            For single expressions: the expression's MongoDB representation.
            For multiple expressions: {"$and": [expr1, expr2, ...]}

        Examples
        --------
        >>> single_expr = AndExpression([Field("price") > 100])
        >>> single_expr.to_mongodb()
        {"price": {"$gt": 100}}  # No $and wrapper needed

        >>> multi_expr = AndExpression([
        ...     Field("price") > 100,
        ...     Field("status") == "active",
        ... ])
        >>> multi_expr.to_mongodb()
        {"$and": [{"price": {"$gt": 100}}, {"status": "active"}]}
        """
        mongo_expressions = [expr.to_mongodb() for expr in self.expressions]
        if len(mongo_expressions) == 1:
            return mongo_expressions[0]
        return {"$and": mongo_expressions}

    def __and__(self, other: QueryExpression) -> AndExpression:
        """
        Chain multiple AND expressions efficiently.

        Optimizes chaining by flattening nested AND expressions instead of
        creating deeply nested structures. This improves both performance
        and readability of the resulting MongoDB queries.

        Parameters
        ----------
        other : QueryExpression
            Another expression to add to this AND expression.

        Returns
        -------
        AndExpression
            A new AndExpression containing all expressions from this AND
            plus the new expression.

        Examples
        --------
        >>> expr1 = Field("price") > 100
        >>> expr2 = Field("category") == "electronics"
        >>> expr3 = Field("status") == "active"
        >>> # Chain efficiently - flattens automatically
        >>> and_expr = expr1 & expr2  # AndExpression([expr1, expr2])
        >>> final_expr = and_expr & expr3  # AndExpression([expr1, expr2, expr3])
        >>> # Instead of: AndExpression([AndExpression([expr1, expr2]), expr3])
        """
        return AndExpression([*self.expressions, other])


class OrExpression(QueryExpression):
    """
    Logical OR operation combining multiple query expressions.

    OrExpression represents the logical disjunction of multiple query expressions
    using MongoDB's $or operator. It enables flexible query construction where
    documents can match any of the specified conditions.

    The class supports efficient chaining of multiple OR operations and
    automatically handles the conversion to MongoDB's $or format.

    Parameters
    ----------
    expressions : list[QueryExpression]
        List of query expressions to combine with OR logic.
        All expressions must be valid QueryExpression instances.

    Examples
    --------
    OrExpression is typically created using the | operator:

    >>> from mongoex import Field
    >>> price = Field("price")
    >>> discount = Field("discount")
    >>> category = Field("category")

    >>> # Create expressions
    >>> expensive = price > 1000
    >>> discounted = discount > 0.5
    >>> electronics = category == "electronics"

    >>> # Combine with OR
    >>> or_expr = expensive | discounted
    >>> # Result: OrExpression([expensive, discounted])

    >>> # Chain multiple ORs
    >>> complex_or = or_expr | electronics
    >>> # Result: OrExpression([expensive, discounted, electronics])

    >>> # Convert to MongoDB format
    >>> or_expr.to_mongodb()
    >>> # Returns: {"$or": [{"price": {"$gt": 1000}}, {"discount": {"$gt": 0.5}}]}
    """

    def __init__(self, expressions: list[QueryExpression]) -> None:
        self.expressions = expressions

    def to_mongodb(self) -> dict[str, Any]:
        """
        Convert to MongoDB $or query format.

        Translates the OR expression to MongoDB's $or operator format.
        Unlike AndExpression, OR expressions always use the $or wrapper
        since MongoDB doesn't have a shorthand syntax for OR operations.

        Returns
        -------
        dict[str, Any]
            MongoDB query dictionary in the format:
            {"$or": [expr1_dict, expr2_dict, ...]}

        Examples
        --------
        >>> or_expr = OrExpression([Field("price") > 1000, Field("discount") > 0.5])
        >>> or_expr.to_mongodb()
        {"$or": [{"price": {"$gt": 1000}}, {"discount": {"$gt": 0.5}}]}
        """
        mongo_expressions = [expr.to_mongodb() for expr in self.expressions]
        return {"$or": mongo_expressions}

    def __or__(self, other: QueryExpression) -> OrExpression:
        """
        Chain multiple OR expressions efficiently.

        Optimizes chaining by flattening nested OR expressions instead of
        creating deeply nested structures. This improves both performance
        and readability of the resulting MongoDB queries.

        Parameters
        ----------
        other : QueryExpression
            Another expression to add to this OR expression.

        Returns
        -------
        OrExpression
            A new OrExpression containing all expressions from this OR
            plus the new expression.

        Examples
        --------
        >>> expensive = Field("price") > 1000
        >>> discounted = Field("discount") > 0.5
        >>> popular = Field("views") > 10000
        >>> # Chain efficiently - flattens automatically
        >>> or_expr = expensive | discounted  # OrExpression([expensive, discounted])
        >>> final_expr = (
        ...     or_expr | popular
        ... )  # OrExpression([expensive, discounted, popular])
        >>> # Instead of: OrExpression([OrExpression([expensive, discounted]), popular])
        """
        return OrExpression([*self.expressions, other])
