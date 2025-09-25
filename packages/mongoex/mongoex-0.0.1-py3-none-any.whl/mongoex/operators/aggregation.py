"""
MongoDB Aggregation Operators for MongoEX.

This module provides type-safe MongoDB aggregation operators for pipeline construction.
Aggregation operators are used in $group stages to perform operations like summing,
averaging, collecting values, and other data summarization tasks.

All operators are implemented as type-safe dataclasses that encapsulate both the
operation type and the source field, enabling clean and validated aggregation
pipeline construction with the PipelineBuilder.

Key Features:
- Type-safe operator definitions using dataclasses
- Automatic MongoDB field prefixing (adding '$' to field names)
- Seamless integration with PipelineBuilder.group() method
- Support for all common MongoDB aggregation operations
- Enhanced error messages for invalid field references

Examples
--------
>>> from mongoex import PipelineBuilder
>>> from mongoex.operators.aggregation import Sum, Avg, Push

>>> builder = PipelineBuilder(Order)
>>> pipeline = builder.group(
...     by="customer_id",
...     total_amount=Sum("amount"),  # {"$sum": "$amount"}
...     avg_rating=Avg("rating"),  # {"$avg": "$rating"}
...     products=Push("product_name"),  # {"$push": "$product_name"}
... )
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class AggregationOperator:
    """
    Abstract base class for all MongoDB aggregation operators.

    AggregationOperator provides the foundation for type-safe aggregation operations
    in MongoDB pipelines. Each operator encapsulates both the MongoDB operator
    string and the source field reference, ensuring consistent handling across
    all aggregation types.

    This class serves as the contract that all concrete operators must follow,
    enabling the PipelineBuilder to process aggregation operations uniformly
    with proper validation and MongoDB syntax generation.

    Parameters
    ----------
    source_field : str
        The field name from the input documents to apply the aggregation to.
        Will be automatically prefixed with '$' when generating MongoDB queries.

    Class Attributes
    ----------------
    operator : str
        The MongoDB aggregation operator string (e.g., '$sum', '$avg').
        Must be overridden by concrete subclasses.

    Examples
    --------
    AggregationOperator is not used directly, but through its subclasses:

    >>> from mongoex.operators import Sum, Avg
    >>> total_sales = Sum("price")  # Aggregates the "price" field
    >>> avg_rating = Avg("rating")  # Averages the "rating" field

    >>> # Use in pipeline group operations
    >>> builder.group(
    ...     by="category",
    ...     total_revenue=total_sales,  # {"$sum": "$price"}
    ...     avg_rating=avg_rating,  # {"$avg": "$rating"}
    ... )

    Notes
    -----
    - All operators automatically handle '$' prefixing for field names
    - Field validation is performed by the PipelineBuilder during group operations
    - Operators are immutable dataclass instances for thread safety
    """

    source_field: str | int
    operator: ClassVar[str] = ""  # Should be overridden by subclasses


@dataclass
class Sum(AggregationOperator):
    """
    MongoDB $sum aggregation operator for numeric field summation.

    Calculates the total sum of numeric values for a specified field across
    all documents in each group. Null values are treated as 0, and non-numeric
    values cause an error in MongoDB.

    This operator is commonly used for calculating totals, revenues, counts,
    and other cumulative numeric operations in aggregation pipelines.

    Examples
    --------
    Basic usage in group operations:

    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import Sum

    >>> builder = PipelineBuilder(model=Sale)
    >>> pipeline = builder.group(
    ...     by="category",
    ...     total_revenue=Sum("price"),  # Sum all prices
    ...     total_items=Sum("quantity"),  # Sum all quantities
    ...     order_count=Sum(1),  # Count documents (sum of 1s)
    ... )

    >>> # Generated MongoDB:
    >>> # {"$group": {
    >>> #     "_id": "$category",
    >>> #     "total_revenue": {"$sum": "$price"},
    >>> #     "total_items": {"$sum": "$quantity"},
    >>> #     "order_count": {"$sum": 1}
    >>> # }}

    Advanced usage with expressions:

    >>> # Sum calculated values
    >>> pipeline = builder.group(
    ...     by="store_id", total_value=Sum({"$multiply": ["$price", "$quantity"]})
    ... )

    Notes
    -----
    - Automatically handles field name prefixing with '$'
    - Supports both field names and numeric literals
    - Can be used with complex MongoDB expressions
    - Null and missing values are treated as 0
    """

    operator: ClassVar[str] = "$sum"


@dataclass
class Avg(AggregationOperator):
    """
    MongoDB $avg aggregation operator for numeric field averaging.

    Calculates the arithmetic mean (average) of numeric values for a specified
    field across all documents in each group. Non-numeric values are ignored,
    and if all values are non-numeric or null, returns null.

    This operator is essential for statistical analysis, calculating average
    prices, ratings, scores, and other mean value computations.

    Examples
    --------
    Basic averaging operations:

    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import Avg

    >>> builder = PipelineBuilder(model=Product)
    >>> pipeline = builder.group(
    ...     by="category",
    ...     avg_price=Avg("price"),  # Average price per category
    ...     avg_rating=Avg("customer_rating"),  # Average rating per category
    ...     avg_stock=Avg("stock_level"),  # Average stock level
    ... )

    >>> # Generated MongoDB:
    >>> # {"$group": {
    >>> #     "_id": "$category",
    >>> #     "avg_price": {"$avg": "$price"},
    >>> #     "avg_rating": {"$avg": "$customer_rating"},
    >>> #     "avg_stock": {"$avg": "$stock_level"}
    >>> # }}

    Averaging calculated expressions:

    >>> # Average of calculated profit margin
    >>> pipeline = builder.group(
    ...     by="supplier",
    ...     avg_margin=Avg({"$subtract": ["$selling_price", "$cost_price"]}),
    ... )

    Real-world usage pattern:

    >>> # Sales analysis by region
    >>> sales_analysis = builder.group(
    ...     by="region",
    ...     avg_sale_amount=Avg("amount"),
    ...     avg_discount=Avg("discount_percent"),
    ...     avg_items_per_order=Avg("item_count"),
    ... )

    Notes
    -----
    - Non-numeric values are ignored in the calculation
    - Returns null if all values are non-numeric or missing
    - Supports complex MongoDB expressions as input
    - Automatically handles field name prefixing with '$'
    """

    operator: ClassVar[str] = "$avg"


@dataclass
class First(AggregationOperator):
    """
    MongoDB $first aggregation operator for retrieving first values.

    Returns the first value from a specified field in each group of documents.
    The "first" value depends on the order of documents as they appear in the
    pipeline, making this operator order-sensitive and often used with $sort.

    This operator is useful for getting representative values, earliest timestamps,
    or any "sample" value from grouped data.

    Examples
    --------
    Getting first values in groups:

    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import First

    >>> builder = PipelineBuilder(model=Order)
    >>> pipeline = builder.group(
    ...     by="customer_id",
    ...     first_order_date=First("created_at"),  # First order date
    ...     first_order_amount=First("total_amount"),  # Amount of first order
    ...     sample_product=First("product_name"),  # Sample product name
    ... )

    >>> # Generated MongoDB:
    >>> # {"$group": {
    >>> #     "_id": "$customer_id",
    >>> #     "first_order_date": {"$first": "$created_at"},
    >>> #     "first_order_amount": {"$first": "$total_amount"},
    >>> #     "sample_product": {"$first": "$product_name"}
    >>> # }}

    Order-sensitive usage (recommended pattern):

    >>> # Sort first, then group to get meaningful "first" values
    >>> pipeline = builder.sort_by(created_at=1).group(
    ...     by="customer_id",
    ...     earliest_order=First("created_at"),  # Truly earliest
    ...     first_purchase_amount=First("amount"),  # Amount of earliest order
    ... )

    Complex field expressions:

    >>> # First value of a calculated field
    >>> pipeline = builder.group(
    ...     by="category", first_profit=First({"$subtract": ["$revenue", "$cost"]})
    ... )

    Notes
    -----
    - Result depends on document order in the pipeline
    - Use with $sort for predictable "first" values
    - Returns the actual field value, not a summary statistic
    - Useful for getting representative samples from groups
    """

    operator: ClassVar[str] = "$first"


@dataclass
class Last(AggregationOperator):
    """
    MongoDB $last aggregation operator for retrieving last values.

    Returns the last value from a specified field in each group of documents.
    Like $first, the "last" value depends on the order of documents as they
    appear in the pipeline, making this operator order-sensitive and often
    used in combination with $sort stages.

    This operator is commonly used for getting the most recent values, latest
    timestamps, or final states in time-series and chronological data analysis.

    Examples
    --------
    Getting last values in groups:

    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import Last

    >>> builder = PipelineBuilder(model=Transaction)
    >>> pipeline = builder.group(
    ...     by="account_id",
    ...     last_transaction_date=Last("timestamp"),  # Most recent transaction
    ...     final_balance=Last("balance"),  # Latest balance
    ...     last_transaction_type=Last("type"),  # Type of last transaction
    ... )

    >>> # Generated MongoDB:
    >>> # {"$group": {
    >>> #     "_id": "$account_id",
    >>> #     "last_transaction_date": {"$last": "$timestamp"},
    >>> #     "final_balance": {"$last": "$balance"},
    >>> #     "last_transaction_type": {"$last": "$type"}
    >>> # }}

    Order-sensitive usage (recommended pattern):

    >>> # Sort by timestamp, then get truly "last" values
    >>> pipeline = builder.sort_by(timestamp=1).group(
    ...     by="user_id",
    ...     most_recent_activity=Last("timestamp"),  # Latest timestamp
    ...     current_status=Last("status"),  # Current status
    ...     last_login_ip=Last("ip_address"),  # Most recent IP
    ... )

    Time-series analysis example:

    >>> # Daily closing values
    >>> daily_summary = builder.group(
    ...     by={"$dateToString": {"format": "%Y-%m-%d", "date": "$timestamp"}},
    ...     closing_price=Last("price"),  # Last price of the day
    ...     closing_volume=Last("volume"),  # Last volume of the day
    ...     end_of_day_status=Last("status"),  # Final status
    ... )

    Notes
    -----
    - Result depends on document order in the pipeline
    - Use with $sort for predictable "last" values
    - Ideal for time-series data and chronological analysis
    - Returns the actual field value, not a computed statistic
    - Commonly used for "current state" or "most recent" queries
    """

    operator: ClassVar[str] = "$last"


@dataclass
class Push(AggregationOperator):
    """
    MongoDB $push aggregation operator for array accumulation.

    Creates an array containing all values from a specified field across all
    documents in each group. This operator collects values into arrays,
    preserving duplicates and maintaining the order of documents as processed.

    Push is essential for collecting related data, creating lists of associated
    items, and building arrays for further processing or analysis.

    Examples
    --------
    Basic array creation:

    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import Push

    >>> builder = PipelineBuilder(model=Order)
    >>> pipeline = builder.group(
    ...     by="customer_id",
    ...     all_products=Push("product_name"),  # Array of all products ordered
    ...     order_amounts=Push("total_amount"),  # Array of all order amounts
    ...     order_dates=Push("created_at"),  # Array of all order dates
    ... )

    >>> # Generated MongoDB:
    >>> # {"$group": {
    >>> #     "_id": "$customer_id",
    >>> #     "all_products": {"$push": "$product_name"},
    >>> #     "order_amounts": {"$push": "$total_amount"},
    >>> #     "order_dates": {"$push": "$created_at"}
    >>> # }}

    Creating arrays of objects:

    >>> # Push entire subdocuments
    >>> pipeline = builder.group(
    ...     by="category",
    ...     product_details=Push({
    ...         "name": "$name",
    ...         "price": "$price",
    ...         "rating": "$rating",
    ...     }),
    ... )

    Real-world usage patterns:

    >>> # Customer purchase history
    >>> customer_history = builder.group(
    ...     by="customer_email",
    ...     purchase_history=Push("product_id"),
    ...     spending_pattern=Push("amount"),
    ...     purchase_dates=Push("date"),
    ... )

    >>> # Tag aggregation for content
    >>> content_tags = builder.group(
    ...     by="author_id",
    ...     all_tags=Push("tags"),  # Collect all tag arrays
    ...     article_titles=Push("title"),  # Collect all article titles
    ... )

    With sorting for ordered results:

    >>> # Get chronologically ordered purchase history
    >>> ordered_history = builder.sort_by(created_at=1).group(
    ...     by="user_id",
    ...     chronological_purchases=Push("product_id"),  # Time-ordered array
    ... )

    Notes
    -----
    - Preserves duplicates in the resulting array
    - Order depends on document processing order (use $sort for control)
    - Can push primitive values, objects, or complex expressions
    - Resulting arrays can be quite large - consider memory implications
    - Useful for creating denormalized views of related data
    """

    operator: ClassVar[str] = "$push"
