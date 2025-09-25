"""
MongoDB aggregation pipeline builder with type-safe query construction.

This module provides the core PipelineBuilder class that enables fluent,
type-safe construction of MongoDB aggregation pipelines. The builder supports
validation against dataclass models and provides comprehensive error checking.
"""

from dataclasses import fields
import json
from typing import Any

from mongoex.core.expressions import QueryExpression
from mongoex.core.fields import BaseQueryField
from mongoex.core.fields import create_proxy
from mongoex.models.introspection import extract_annotated_operators
from mongoex.models.introspection import validate_aggregation_model
from mongoex.operators import AggregationOperator
from mongoex.validation.field_validator import create_field_validator


class OutputFieldError(AttributeError):
    """Raised when a destination field is not present in the output model."""

    def __init__(self, field: str) -> None:
        super().__init__(f"Unknown output field: {field}")


class IntoTypeError(TypeError):
    """Raised when 'into' argument is not a dataclass type."""

    def __init__(self) -> None:
        super().__init__("'into' must be a dataclass")


class PipelineBuilder(list[dict[str, Any]]):  # noqa: FURB189
    """
    Type-safe MongoDB aggregation pipeline builder with fluent API.

    PipelineBuilder provides a fluent, method-chaining interface for constructing
    MongoDB aggregation pipelines. It validates field references against dataclass
    models and provides built-in type-safe field access via the `fields` attribute.

    The class inherits from list for PyMongo compatibility, allowing direct usage
    with PyMongo's aggregate() method without requiring a separate build() call.

    Parameters
    ----------
    model : type[Any]
        A dataclass or annotated model representing the input document structure.
        Must have `__annotations__` attribute defining field types.

    Attributes
    ----------
    model : type[Any]
        The input document model used for field validation.
    valid_fields : set[str]
        Set of valid field names extracted from the model annotations.
    fields : object
        Lazy-loaded field proxy object providing type-safe field access.
        Access model fields via builder.fields.field_name syntax.

    Raises
    ------
    TypeError
        If the model doesn't have type annotations.

    Examples
    --------
    Basic usage with dataclass models:

    >>> from dataclasses import dataclass
    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import Sum, Avg

    >>> @dataclass
    ... class Sale:
    ...     item: str
    ...     price: float
    ...     quantity: int

    >>> # Create builder with model validation
    >>> builder = PipelineBuilder(Sale)

    >>> # Type-safe field access via builder.fields (recommended)
    >>> pipeline = builder.match(builder.fields.price > 100).group(
    ...     by="item", total_quantity=Sum("quantity"), avg_price=Avg("price")
    ... )

    >>> # Direct usage with PyMongo (no build() call needed)
    >>> result = db.collection.aggregate(pipeline)

    >>> # Alternative: Using direct Field objects
    >>> from mongoex import Field
    >>> pipeline = builder.match(Field("price") > 100).group(
    ...     by="item", total_quantity=Sum("quantity")
    ... )

    Nested field access:

    >>> @dataclass
    ... class Address:
    ...     city: str
    ...     country: str

    >>> @dataclass
    ... class User:
    ...     name: str
    ...     address: Address

    >>> builder = PipelineBuilder(User)
    >>> # Automatic dot notation for nested fields
    >>> pipeline = builder.match(builder.fields.address.city == "New York")
    """

    def __init__(self, model: type[Any]) -> None:
        super().__init__()  # Initialize the list
        self.model = model
        self._fields_proxy = None  # Lazy-loaded field proxy

        # Extract valid field names from the model's type annotations
        # (including inheritance)
        if not hasattr(model, "__annotations__"):

            class _ModelAnnotationError(TypeError):
                def __init__(self):  # pragma: no cover - simple message container
                    super().__init__(
                        "Model must define type annotations (e.g., dataclass, "
                        "Pydantic)."
                    )

            raise _ModelAnnotationError from None

        # Collect annotations from inheritance chain (same logic as create_proxy)
        all_annotations: dict[str, Any] = {}
        for base in reversed(model.__mro__):
            if hasattr(base, "__annotations__"):
                all_annotations.update(base.__annotations__)

        self.valid_fields = set(all_annotations.keys())

        # Create field validator for rich error reporting
        self._validator = create_field_validator(model)

    def _update_model(self, new_model: type[Any]) -> None:
        """
        Update the current model and invalidate cached field proxy.

        This method is called when pipeline stages cause schema transitions
        (e.g., $unwind, $group with model, $project with model).

        Parameters
        ----------
        new_model : type[Any]
            The new model type that represents the transformed schema.
        """
        self.model = new_model
        self._fields_proxy = None  # Invalidate cache to force regeneration

        # Update valid fields from new model
        all_annotations: dict[str, Any] = {}
        for base in reversed(new_model.__mro__):
            if hasattr(base, "__annotations__"):
                all_annotations.update(base.__annotations__)

        self.valid_fields = set(all_annotations.keys())

        # Update field validator for new model
        self._validator = create_field_validator(new_model)

    @property
    def fields(self):
        """
        Lazy-loaded field proxy for type-safe query building.

        Returns a dynamically generated proxy object with typed field attributes
        corresponding to the model's fields. Each field attribute is a Field object
        that supports MongoDB query operators and maintains type information.

        The proxy is created once and cached for subsequent access, providing
        efficient field access while maintaining type safety at runtime.

        Returns
        -------
        object
            Field proxy object with attributes corresponding to model fields.
            Each attribute supports MongoDB comparison operators (>, <, ==, etc.)
            and logical combinations (&, |).

        Examples
        --------
        >>> @dataclass
        ... class Sale:
        ...     item: str
        ...     price: float
        ...     category: str

        >>> builder = PipelineBuilder(model=Sale)
        >>> # Access fields through the proxy
        >>> price_query = builder.fields.price > 100
        >>> item_query = builder.fields.item == "laptop"
        >>> combined = price_query & item_query

        >>> # Nested field access is also supported
        >>> nested_query = builder.fields.address.city == "New York"

        Note
        ----
        Due to dynamic proxy generation, IDEs may show generic 'Any' types
        for field attributes, but proper typing is maintained at runtime.
        This is a limitation of static analysis with dynamically generated code.
        """
        if self._fields_proxy is None:
            self._fields_proxy = create_proxy(self.model)
        return self._fields_proxy

    def match(self, expression: QueryExpression | BaseQueryField) -> "PipelineBuilder":
        """
        Add a $match stage to filter documents based on query expressions.

        Creates a MongoDB $match stage that filters documents according to the
        provided query expression. Supports both Field-based and FieldProxy-based
        expressions with full logical combination capabilities.

        Parameters
        ----------
        expression : QueryExpression
            A query expression built using Field objects or FieldProxy objects.
            Supports all MongoDB comparison operators and logical combinations
            using Python's & (and) and | (or) operators.

        Returns
        -------
        PipelineBuilder
            Self instance enabling method chaining for building complex pipelines.

        Examples
        --------
        Using direct Field objects:

        >>> from mongoex import Field
        >>> price = Field("price")
        >>> status = Field("status")
        >>> builder.match((price > 100) & (status == "active"))

        Using FieldProxy (recommended for type safety):

        >>> # Using the builder's field proxy (recommended)
        >>> builder.match(builder.fields.price > 100)
        >>> builder.match(
        ...     (builder.fields.price >= 50) & (builder.fields.item != "book")
        ... )

        >>> # Or using direct Field objects
        >>> from mongoex import Field
        >>> builder.match(Field("price").in_([100, 200, 300]))

        Complex logical expressions:

        >>> builder.match(
        ...     (builder.fields.price > 100)
        ...     | (
        ...         (builder.fields.category == "electronics")
        ...         & (builder.fields.discount > 0.1)
        ...     )
        ... )
        """
        # Convert the expression to MongoDB query format
        query = expression.to_mongodb()
        self.append({"$match": query})
        return self

    def group(
        self,
        by: str,
        model: type[Any] | None = None,
        into: type[Any] | None = None,
        **kwargs: AggregationOperator | dict[str, Any],
    ) -> "PipelineBuilder":
        """
        Add a $group stage to aggregate documents by specified field.

        Creates a MongoDB $group stage that groups documents by a field from the
        input model and applies aggregation operations. Supports two modes:
        1. Traditional: explicit kwargs with AggregationOperator instances
        2. Model-based: automatic extraction from Annotated dataclass fields

        Parameters
        ----------
        by : str
            Field name from the INPUT model to group documents by.
            Must be a valid field name present in the model's annotations.
        model : type[Any] | None, optional
            Annotated dataclass with fields using Annotated[type, AggregationOperator].
            When provided, extracts aggregation operations from field annotations.
            Mutually exclusive with kwargs - use either model OR kwargs, not both.
        into : type[Any] | None, optional
            Dataclass representing the expected OUTPUT structure after grouping.
            When provided, validates that all aggregation fields exist in this model.
            Deprecated when using model parameter
            (model serves as both source and target).
        **kwargs : Any
            Aggregation operations to perform. Keys become field names in the output,
            values should be AggregationOperator instances (Sum, Avg, etc.) or
            raw MongoDB aggregation expressions.
            Mutually exclusive with model parameter.

        Returns
        -------
        PipelineBuilder
            Self instance enabling method chaining.

        Raises
        ------
        OutputFieldError
            If any aggregation field name is not present in the 'into' model.
        IntoTypeError
            If 'into' is provided but is not a dataclass.
        ValueError
            If both model and kwargs are provided (mutually exclusive).

        Examples
        --------
        Traditional approach with explicit operators:

        >>> from mongoex.operators import Sum, Avg, First
        >>> builder.group(
        ...     by="category",
        ...     total_sales=Sum("price"),
        ...     avg_price=Avg("price"),
        ...     first_item=First("item"),
        ... )

        New model-based approach with Annotated fields:

        >>> from typing import Annotated
        >>> @dataclass
        ... class CategorySummary:
        ...     _id: str  # The grouped field (category value)
        ...     total_sales: Annotated[float, Sum("price")]
        ...     avg_price: Annotated[float, Avg("price")]
        ...     first_item: Annotated[str, First("item")]

        >>> builder.group(by="category", model=CategorySummary)
        ...     by="category",
        ...     total_sales=Sum("price"),
        ...     avg_price=Avg("price"),
        ...     first_item=First("item"),
        ... )

        With output model validation:

        >>> @dataclass
        ... class CategorySummary:
        ...     _id: str  # The grouped field value
        ...     total_sales: float
        ...     avg_price: float
        ...     item_count: int

        >>> builder.group(
        ...     by="category",
        ...     into=CategorySummary,
        ...     total_sales=Sum("price"),
        ...     avg_price=Avg("price"),
        ...     item_count=Sum("quantity"),
        ... )

        Using raw MongoDB expressions:

        >>> builder.group(
        ...     by="status", total={"$sum": "$amount"}, max_date={"$max": "$created_at"}
        ... )
        """
        # Validates the 'by' field against the input model
        self._validator.validate_field(by, "Group operation")

        # Handle model-based vs kwargs-based approach
        if model is not None and kwargs:
            msg = "Cannot use both 'model' and explicit kwargs. Choose one approach."
            raise ValueError(msg)

        # Extract operations from model if provided
        if model is not None:
            validate_aggregation_model(model)
            aggregation_ops = extract_annotated_operators(model)

            # Use model fields as both validation target and operation source
            output_fields = {f.name for f in fields(model)}
        else:
            # Traditional kwargs approach
            aggregation_ops = kwargs

            # Handle into parameter for output validation (legacy approach)
            output_fields: set[str] = set()
            if into:
                try:
                    # The `_id` field is special, it's the output of `by`.
                    # The output model should have a field for it.
                    output_fields = {f.name for f in fields(into)}
                except TypeError:
                    raise IntoTypeError() from None

        group_stage: dict[str, Any] = {"_id": f"${by}"}
        for field_name, agg_op in aggregation_ops.items():
            # Validate destination field against output model (model or into)
            if output_fields and field_name not in output_fields:
                raise OutputFieldError(field_name)

            if isinstance(agg_op, AggregationOperator):
                # Validates the operator's source field against the input model
                self._validator.validate_field(
                    agg_op.source_field, f"Aggregation operation '{field_name}'"
                )

                # Handle numeric literals vs field names in aggregation operations
                if isinstance(agg_op.source_field, (int, float)):
                    group_stage[field_name] = {agg_op.operator: agg_op.source_field}
                else:
                    group_stage[field_name] = {
                        agg_op.operator: f"${agg_op.source_field}"
                    }
            else:
                group_stage[field_name] = agg_op

        self.append({"$group": group_stage})

        # Handle model transition for model-based grouping
        if model is not None:
            self._update_model(model)

        return self

    def project(self, **kwargs: Any) -> "PipelineBuilder":
        """
        Add a $project stage to reshape output documents.

        Creates a MongoDB $project stage that controls which fields are included,
        excluded, or computed in the pipeline output. Supports field inclusion,
        exclusion, renaming, and computed expressions.

        Parameters
        ----------
        **kwargs : Any
            Field projection specifications:
            - field_name=1: Include field in output
            - field_name=0: Exclude field from output
            - _id=0: Commonly used to exclude the _id field
            - new_field="$existing_field": Rename or reference fields
            - computed_field={"$add": ["$field1", "$field2"]}: Computed expressions

        Returns
        -------
        PipelineBuilder
            Self instance enabling method chaining.

        Examples
        --------
        Simple field inclusion/exclusion:

        >>> builder.project(item=1, price=1, _id=0)  # Include only item and price
        >>> builder.project(sensitive_data=0)  # Exclude sensitive_data field

        Field renaming and computed values:

        >>> builder.project(
        ...     product_name="$item",
        ...     final_price="$price",
        ...     total_value={"$multiply": ["$price", "$quantity"]},
        ...     _id=0,
        ... )

        Complex computed expressions:

        >>> builder.project(
        ...     item=1,
        ...     price=1,
        ...     discounted_price={
        ...         "$multiply": ["$price", {"$subtract": [1, "$discount"]}]
        ...     },
        ...     category_upper={"$toUpper": "$category"},
        ... )
        """
        self.append({"$project": kwargs})
        return self

    def sort_by(self, **kwargs: Any) -> "PipelineBuilder":
        """
        Add a $sort stage to order documents in the pipeline.

        Creates a MongoDB $sort stage that orders documents based on one or more
        fields. Supports both ascending and descending sort orders.

        Parameters
        ----------
        **kwargs : Any
            Sort specifications where:
            - field_name=1: Sort ascending by field_name
            - field_name=-1: Sort descending by field_name
            Multiple fields can be specified to create compound sorting.

        Returns
        -------
        PipelineBuilder
            Self instance enabling method chaining.

        Examples
        --------
        Single field sorting:

        >>> builder.sort_by(price=1)  # Sort by price ascending
        >>> builder.sort_by(created_date=-1)  # Sort by date descending

        Multi-field compound sorting:

        >>> # Sort by category ascending, then price descending
        >>> builder.sort_by(category=1, price=-1)
        >>> builder.sort_by(priority=-1, name=1, created_date=-1)

        Common patterns:

        >>> # Most recent first
        >>> builder.sort_by(created_at=-1)
        >>> # Highest price first, then alphabetical by name
        >>> builder.sort_by(price=-1, name=1)
        """
        self.append({"$sort": kwargs})
        return self

    def limit(self, count: int) -> "PipelineBuilder":
        """
        Add a $limit stage to restrict the number of documents.

        Creates a MongoDB $limit stage that caps the number of documents
        passed to subsequent pipeline stages. Useful for pagination,
        performance optimization, or getting top-N results.

        Parameters
        ----------
        count : int
            Maximum number of documents to return. Must be a positive integer.

        Returns
        -------
        PipelineBuilder
            Self instance enabling method chaining.

        Examples
        --------
        Basic limiting:

        >>> builder.limit(10)  # Get only first 10 documents
        >>> builder.limit(100)  # Limit to 100 documents

        Common use cases:

        >>> # Get top 5 highest-priced items
        >>> builder.sort_by(price=-1).limit(5)

        >>> # Pagination: skip first 20, take next 10
        >>> # Note: Use MongoDB's $skip stage before $limit for pagination
        >>> builder.limit(10)  # This only limits, doesn't skip

        >>> # Performance optimization for large datasets
        >>> builder.match(builder.fields.status == "active").limit(1000)
        """
        self.append({"$limit": count})
        return self

    def unwind(
        self,
        path: str,
        *,
        array_index: str | None = None,
        preserve_empty: bool = False,
        model: type[Any] | None = None,
    ) -> "PipelineBuilder":
        """
        Add a $unwind stage to deconstruct array fields.

        The $unwind stage flattens array fields, creating a new document for each
        array element. This fundamentally changes the document schema, so an
        optional model parameter allows defining the new schema after unwinding.

        Parameters
        ----------
        path : str
            Field path to unwind. The field should contain an array that will be
            deconstructed. Automatically prefixed with '$' if not present.
        array_index : str | None, optional
            Name of a new field to hold the array index (0-based) of the
            unwound element. Useful for preserving the original position of
            elements. Default is None.
        preserve_empty : bool, optional
            If True, includes documents in the output even when the unwind path is null,
            missing, or an empty array. If False, such documents are excluded from
            the output. Default is False.
        model : type[Any] | None, optional
            Model representing the document structure after unwinding.
            When provided, automatically transitions the pipeline to use this new
            model for subsequent operations. Use this when unwinding changes the
            schema significantly (e.g., flattening nested objects).

        Returns
        -------
        PipelineBuilder
            Self instance for method chaining.

        Examples
        --------
        Basic array unwinding:

        >>> builder.unwind("tags")

        Unwinding with array index:

        >>> builder.unwind("items", array_index="item_index")

        Preserving null/empty arrays:

        >>> builder.unwind("optional_tags", preserve_empty=True)

        Schema transition with model (when unwinding changes structure):

        >>> @dataclass
        ... class UnwoundOrder:
        ...     customer_id: str
        ...     order_date: datetime
        ...     item: str  # Unwound from items array
        ...     item_price: float  # From unwound items
        ...     item_index: int  # Added by unwind with array_index

        >>> builder.unwind("items", array_index="item_index", model=UnwoundOrder)
        # Subsequent operations now use UnwoundOrder fields

        Complete example:

        >>> builder.unwind(
        ...     "products.variants",
        ...     array_index="variant_position",
        ...     preserve_empty=True,
        ...     model=UnwoundProduct,
        ... )
        """
        # Ensure path starts with '$'
        if not path.startswith("$"):
            path = f"${path}"

        # Build unwind stage based on complexity
        if array_index is None and not preserve_empty:
            # Simple unwind format
            unwind_stage = {"$unwind": path}
        else:
            # Complex unwind format with options
            unwind_options: dict[str, Any] = {"path": path}

            if array_index is not None:
                unwind_options["includeArrayIndex"] = array_index

            if preserve_empty:
                unwind_options["preserveNullAndEmptyArrays"] = True

            unwind_stage = {"$unwind": unwind_options}

        self.append(unwind_stage)

        # Handle model transition if new model provided
        if model is not None:
            self._update_model(model)

        return self
        return self

    def build(self) -> list[dict[str, Any]]:
        """
        Build and return the complete MongoDB aggregation pipeline.

        Converts the accumulated pipeline stages into a list format suitable
        for use with MongoDB's aggregate() method. Returns a new list instance
        to prevent accidental modification of the builder's internal state.

        Returns
        -------
        list[dict[str, Any]]
            Complete aggregation pipeline as a list of MongoDB stage dictionaries.
            Each dictionary represents a single pipeline stage (e.g., {"$match": ...}).

        Examples
        --------
        Building a pipeline and using it with MongoDB:

        >>> builder = PipelineBuilder(model=Sale)
        >>> pipeline = (
        ...     builder.match(builder.fields.price > 100)
        ...     .group(by="category", total=Sum("price"))
        ...     .sort_by(total=-1)
        ...     .build()
        ... )

        >>> # Use with PyMongo
        >>> results = collection.aggregate(pipeline)

        >>> # Pipeline structure:
        >>> # [
        >>> #     {"$match": {"price": {"$gt": 100}}},
        >>> #     {"$group": {"_id": "$category", "total": {"$sum": "$price"}}},
        >>> #     {"$sort": {"total": -1}}
        >>> # ]
        """
        return list(self)  # Convert to a new list instance

    def to_list(self) -> list[dict[str, Any]]:
        """
        Convert to list for explicit PyMongo compatibility.

        Alias for build() method that emphasizes the return of a list
        object compatible with PyMongo's aggregate() method.

        Returns
        -------
        list[dict[str, Any]]
            The aggregation pipeline as a list of stage dictionaries.
        """
        return self.build()

    def as_list(self) -> list[dict[str, Any]]:
        """
        Return a list-compatible object for PyMongo.

        Another alias for build() method providing semantic clarity
        when the pipeline needs to be used as a list object.

        Returns
        -------
        list[dict[str, Any]]
            The aggregation pipeline as a list of stage dictionaries.
        """
        return self.build()

    def __repr__(self) -> str:
        """
        Return a string representation of the PipelineBuilder.

        Provides a concise string representation showing the associated model
        and the current number of pipeline stages.

        Returns
        -------
        str
            String representation in the format
            "PipelineBuilder(model='ModelName', stages=N)"
        """
        return f"PipelineBuilder(model='{self.model.__name__}', stages={len(self)})"

    def print_pipeline(self, title: str = "MongoDB Aggregation Pipeline") -> None:
        """
        Print the pipeline in formatted JSON for inspection and debugging.

        Displays the current pipeline stages in a human-readable JSON format
        with proper indentation. Useful for debugging, documentation, and
        understanding the generated MongoDB aggregation pipeline.

        Parameters
        ----------
        title : str, optional
            Custom title for the pipeline display.
            Defaults to "MongoDB Aggregation Pipeline".

        Examples
        --------
        Basic usage:

        >>> builder.match(builder.fields.price > 100).group(by="category")
        >>> builder.print_pipeline()
        # Output:
        # === MongoDB Aggregation Pipeline ===
        # [
        #   {"$match": {"price": {"$gt": 100}}},
        #   {"$group": {"_id": "$category"}}
        # ]
        # =====================================

        With custom title:

        >>> builder.print_pipeline("Sales Analysis Pipeline")
        # Output:
        # === Sales Analysis Pipeline ===
        # [pipeline JSON here...]
        # ================================

        Notes
        -----
        If the pipeline is empty, prints a helpful message indicating
        that stages need to be added first.
        """
        if not self:
            print("Pipeline is empty. Add stages first!")
            return

        print(f"\n=== {title} ===")
        print(json.dumps(list(self), indent=2))
        print("=" * (len(title) + 8))
