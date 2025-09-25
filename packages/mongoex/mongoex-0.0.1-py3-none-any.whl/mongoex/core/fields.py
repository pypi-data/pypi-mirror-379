"""
Type-safe field-based query API for MongoDB operations.

This module provides the complete field-based query system that enables
intuitive, type-safe MongoDB query construction. It includes:

Core Classes:
- BaseQueryField: Abstract base class providing MongoDB comparison operators
- Field: Flexible field class supporting both simple and type-safe usage patterns
- FieldProxy: Dynamic proxy for type-safe field access via PipelineBuilder

Key Features:
- Operator overloading for natural query syntax (field > value)
- Type-safe field access through PipelineBuilder.fields
- Nested field access support (builder.fields.user.address.city)
- Enhanced validation with detailed error messages
- Full MongoDB operator support ($eq, $ne, $gt, $gte, $lt, $lte, $in, $nin)

The module supports two complementary approaches:
1. Direct Field creation: Field("price") > 100
2. Builder-integrated access: builder.fields.price > 100 (recommended)
"""

from __future__ import annotations

from dataclasses import is_dataclass
import inspect
import re
from typing import TYPE_CHECKING
from typing import Any

from mongoex.core.expressions import ComparisonExpression
from mongoex.validation.field_validator import ExpressionAnalyzer
from mongoex.validation.field_validator import QueryValidationError


if TYPE_CHECKING:
    from mongoex.operators.field import ExpressionOperator


class ExpressionField:
    """
    Wrapper for expression operators that can be used in MongoDB operations.

    This class allows expression operators to be used seamlessly in pipeline
    operations like project(), match(), etc. It also supports arithmetic
    operations to create more complex expressions.
    """

    def __init__(self, expression: ExpressionOperator) -> None:
        self.expression = expression

    def to_mongodb(self) -> dict[str, Any]:
        """Convert the expression to MongoDB format."""
        return self.expression.to_mongodb()

    def __repr__(self) -> str:
        """Return a string representation of the ExpressionField."""
        return f"ExpressionField({self.expression.to_mongodb()})"

    # Arithmetic operators for chaining expressions
    def __add__(self, other: Any) -> ExpressionField:
        """Add operator: expression + other."""
        from mongoex.operators.field import Add  # noqa: PLC0415

        return ExpressionField(Add(self, other))

    def __radd__(self, other: Any) -> ExpressionField:
        """Reverse add operator: other + expression."""
        from mongoex.operators.field import Add  # noqa: PLC0415

        return ExpressionField(Add(other, self))

    def __sub__(self, other: Any) -> ExpressionField:
        """Subtract operator: expression - other."""
        from mongoex.operators.field import Subtract  # noqa: PLC0415

        return ExpressionField(Subtract(self, other))

    def __rsub__(self, other: Any) -> ExpressionField:
        """Reverse subtract operator: other - expression."""
        from mongoex.operators.field import Subtract  # noqa: PLC0415

        return ExpressionField(Subtract(other, self))

    def __mul__(self, other: Any) -> ExpressionField:
        """Multiply operator: expression * other."""
        from mongoex.operators.field import Multiply  # noqa: PLC0415

        return ExpressionField(Multiply(self, other))

    def __rmul__(self, other: Any) -> ExpressionField:
        """Reverse multiply operator: other * expression."""
        from mongoex.operators.field import Multiply  # noqa: PLC0415

        return ExpressionField(Multiply(other, self))

    def __truediv__(self, other: Any) -> ExpressionField:
        """Divide operator: expression / other."""
        from mongoex.operators.field import Divide  # noqa: PLC0415

        return ExpressionField(Divide(self, other))

    def __rtruediv__(self, other: Any) -> ExpressionField:
        """Reverse divide operator: other / expression."""
        from mongoex.operators.field import Divide  # noqa: PLC0415

        return ExpressionField(Divide(other, self))


class BaseQueryField:
    """
    Abstract base class providing MongoDB comparison operators for query fields.

    BaseQueryField serves as the foundation for all field-based query operations
    in MongoEX. It implements Python's special methods to provide natural syntax
    for MongoDB comparisons using standard Python operators.

    This class defines the operator interface that all field classes must support,
    enabling consistent query syntax across different field implementations.

    Attributes
    ----------
    name : str
        The MongoDB field name. Must be provided by concrete subclasses.

    Methods
    -------
    All comparison methods return ComparisonExpression objects that can be
    combined with logical operators (&, |) and converted to MongoDB queries.

    Examples
    --------
    The BaseQueryField is not used directly but through its subclasses:

    >>> from mongoex import PipelineBuilder, Field
    >>> from dataclasses import dataclass
    >>>
    >>> @dataclass
    ... class Product:
    ...     name: str
    ...     price: float

    >>> builder = PipelineBuilder(Product)
    >>> price_field = builder.fields.price  # Field inherits from BaseQueryField

    >>> # All comparison operators are available
    >>> price_field == 100  # Equal to
    >>> price_field != 50  # Not equal to
    >>> price_field > 100  # Greater than
    >>> price_field >= 100  # Greater than or equal
    >>> price_field < 200  # Less than
    >>> price_field <= 200  # Less than or equal
    >>> price_field.in_([100, 150, 200])  # In list
    >>> price_field.nin([0, 999])  # Not in list

    >>> # Combine with logical operators
    >>> query = (builder.fields.price > 100) & (builder.fields.price < 200)
    """

    name: str  # Must be provided by subclasses

    def __eq__(self, value: Any) -> ComparisonExpression:  # type: ignore[override]
        """Equal comparison: field == value."""
        return ComparisonExpression(self.name, "$eq", value)

    def __ne__(self, value: Any) -> ComparisonExpression:  # type: ignore[override]
        """Not equal comparison: field != value."""
        return ComparisonExpression(self.name, "$ne", value)

    def __gt__(self, value: Any) -> ComparisonExpression:
        """Greater than comparison: field > value."""
        return ComparisonExpression(self.name, "$gt", value)

    def __ge__(self, value: Any) -> ComparisonExpression:
        """Greater than or equal comparison: field >= value."""
        return ComparisonExpression(self.name, "$gte", value)

    def __lt__(self, value: Any) -> ComparisonExpression:
        """Less than comparison: field < value."""
        return ComparisonExpression(self.name, "$lt", value)

    def __le__(self, value: Any) -> ComparisonExpression:
        """Less than or equal comparison: field <= value."""
        return ComparisonExpression(self.name, "$lte", value)

    def in_(self, values: list[Any]) -> ComparisonExpression:
        """
        In comparison: field in [values].

        Note: Uses in_() method because 'in' is a Python keyword.

        Parameters
        ----------
        values : list[Any]
            List of values to check membership.

        Returns
        -------
        ComparisonExpression
            MongoDB $in comparison expression.

        Examples
        --------
        >>> field.in_(["active", "pending"])
        """
        return ComparisonExpression(self.name, "$in", values)

    def nin(self, values: list[Any]) -> ComparisonExpression:
        """
        Not in comparison: field not in [values].

        Parameters
        ----------
        values : list[Any]
            List of values to check non-membership.

        Returns
        -------
        ComparisonExpression
            MongoDB $nin comparison expression.

        Examples
        --------
        >>> field.nin(["inactive", "deleted"])
        """
        return ComparisonExpression(self.name, "$nin", values)

    def isin(self, values: list[Any]) -> ComparisonExpression:
        """
        Alias for in_() method for pandas-style syntax.

        Parameters
        ----------
        values : list[Any]
            List of values to check membership.

        Returns
        -------
        ComparisonExpression
            MongoDB $in comparison expression.

        Examples
        --------
        >>> field.isin(["active", "pending"])
        """
        return self.in_(values)

    def __hash__(self) -> int:
        """Make field hashable based on its name."""
        return hash(self.name)

    # Arithmetic operators for expression building
    def __add__(self, other: Any) -> ExpressionField:
        """Add operator: field + other."""
        from mongoex.operators.field import Add

        return ExpressionField(Add(self, other))

    def __radd__(self, other: Any) -> ExpressionField:
        """Reverse add operator: other + field."""
        from mongoex.operators.field import Add

        return ExpressionField(Add(other, self))

    def __sub__(self, other: Any) -> ExpressionField:
        """Subtract operator: field - other."""
        from mongoex.operators.field import Subtract

        return ExpressionField(Subtract(self, other))

    def __rsub__(self, other: Any) -> ExpressionField:
        """Reverse subtract operator: other - field."""
        from mongoex.operators.field import Subtract

        return ExpressionField(Subtract(other, self))

    def __mul__(self, other: Any) -> ExpressionField:
        """Multiply operator: field * other."""
        from mongoex.operators.field import Multiply

        return ExpressionField(Multiply(self, other))

    def __rmul__(self, other: Any) -> ExpressionField:
        """Reverse multiply operator: other * field."""
        from mongoex.operators.field import Multiply

        return ExpressionField(Multiply(other, self))

    def __truediv__(self, other: Any) -> ExpressionField:
        """Divide operator: field / other."""
        from mongoex.operators.field import Divide

        return ExpressionField(Divide(self, other))

    def __rtruediv__(self, other: Any) -> ExpressionField:
        """Reverse divide operator: other / field."""
        from mongoex.operators.field import Divide

        return ExpressionField(Divide(other, self))

    # String methods that create expression operators
    def contains(self, value: str) -> ComparisonExpression:
        """
        Run 'string contains' operation using regex.

        Creates a MongoDB regex query to check if the field contains the
        specified substring.

        Parameters
        ----------
        value : str
            The substring to search for.

        Returns
        -------
        ComparisonExpression
            MongoDB regex comparison expression.

        Examples
        --------
        >>> field.contains("python")  # Field contains "python"
        >>> field.contains("MongoDB")  # Case-sensitive search
        """
        escaped_value = re.escape(value)
        return ComparisonExpression(self.name, "$regex", escaped_value)

    def regex(self, pattern: str, flags: str = "") -> ComparisonExpression:
        r"""
        Regex pattern matching operation.

        Creates a MongoDB regex query with the specified pattern and optional flags.

        Parameters
        ----------
        pattern : str
            The regex pattern to match.
        flags : str, optional
            Regex flags (e.g., "i" for case-insensitive). Defaults to "".

        Returns
        -------
        ComparisonExpression
            MongoDB regex comparison expression.

        Examples
        --------
        >>> field.regex("^[A-Z]", "i")  # Starts with letter, case-insensitive
        >>> field.regex("\\d+")  # Contains digits
        """
        if flags:
            return ComparisonExpression(
                self.name, "$regex", {"$regex": pattern, "$options": flags}
            )
        else:
            return ComparisonExpression(self.name, "$regex", pattern)

    # Boolean field operations
    def to_mongodb(self) -> dict[str, Any]:
        """
        Convert field to MongoDB query for direct boolean usage.
        
        Enables using boolean fields directly in match operations without
        explicit comparison. When used directly, the field is treated as
        a "truthy" check (equivalent to field == True).
        
        Returns
        -------
        dict[str, Any]
            MongoDB query dictionary for the field being truthy.
            
        Examples
        --------
        >>> builder = PipelineBuilder(Product)
        >>> active_query = builder.match(builder.fields.active)  # Direct usage
        >>> # Equivalent to: builder.match(builder.fields.active == True)
        """
        return {self.name: True}
    
    def __invert__(self) -> ComparisonExpression:
        """
        Negation operator for boolean fields: ~field.
        
        Enables Pythonic negation syntax for boolean field queries.
        The ~ operator creates a "False" comparison for the field.
        
        Returns
        -------
        ComparisonExpression
            Comparison expression for field == False.
            
        Examples
        --------
        >>> builder = PipelineBuilder(Product)
        >>> inactive_query = builder.match(~builder.fields.active)
        >>> # Equivalent to: builder.match(builder.fields.active == False)
        
        >>> # Can be combined with other expressions
        >>> complex_query = builder.match(
        ...     (~builder.fields.active) & (builder.fields.price > 100)
        ... )
        """
        return ComparisonExpression(self.name, "$eq", False)
    
    def __bool__(self) -> bool:
        """
        Prevent accidental boolean conversion of field objects.
        
        Fields should not be used in direct boolean contexts (if statements, etc.)
        as they represent query structures, not boolean values. This method
        provides a clear error message when such usage is attempted.
        
        Raises
        ------
        TypeError
            Always raised to prevent misuse of field objects in boolean contexts.
            
        Examples
        --------
        >>> field = Field("active")
        >>> if field:  # This will raise TypeError
        ...     pass
        
        >>> # Correct usage:
        >>> if field == True:  # Explicit comparison
        ...     pass
        """
        error_msg = (
            f"Field '{self.name}' cannot be used directly in boolean contexts. "
            "Use explicit comparisons like 'field == True' or 'field == False', "
            "or use 'field.to_mongodb()' for direct boolean queries."
        )
        raise TypeError(error_msg)


class Field[T](BaseQueryField):
    """
    MongoDB field representation with operator overloading and type safety.

    Field is the core class for building MongoDB queries in MongoEX. It supports
    both simple field creation for quick queries and advanced type-safe usage
    with model validation. Fields can be combined with comparison operators and
    logical operations to create complex MongoDB query expressions.

    The class provides two main usage patterns:
    1. Simple field creation for direct usage
    2. Type-safe proxy functionality with model validation

    Parameters
    ----------
    name : str
        The MongoDB document field name. Supports dot notation for nested fields.
    field_type : type[T] | None, optional
        Type hint for the field value. When provided, enables better IDE support
        and runtime type checking. Defaults to None (object type).

    Attributes
    ----------
    name : str
        The MongoDB field name.
    field_type : type
        The Python type of the field value.

    Examples
    --------
    Basic field creation and usage:

    >>> from mongoex import Field
    >>> price = Field("price")
    >>> category = Field("category")

    >>> # Simple comparisons
    >>> price_query = price > 100
    >>> category_query = category == "electronics"
    >>> combined = price_query & category_query

    >>> price_field = Field("price", field_type=float)
    >>> name_field = Field("name", field_type=str)
    >>> # Better IDE support and type checking

    Nested field access:

    >>> user = Field("user")
    >>> address_query = user.address.city == "New York"
    >>> # Creates Field("user.address.city")
    """

    def __init__(
        self,
        name: str,
        field_type: type[T] | None = None,
        valid_fields: set[str] | None = None,
    ) -> None:
        self.name = name
        self.field_type = field_type or object
        self.valid_fields = valid_fields

        if valid_fields and name not in valid_fields:
            analyzer = ExpressionAnalyzer(set(valid_fields))
            suggestions = analyzer.find_similar_fields(name)

            raise QueryValidationError(
                name,
                expression_context=f"Field initialization: Field('{name}')",
                available_fields=sorted(list(valid_fields)),
                suggestions=suggestions,
                error_location="Field declaration",
            )

    def __hash__(self) -> int:
        """Make field hashable based on its name."""
        return hash(self.name)

    def __repr__(self) -> str:
        """Return a string representation of the Field."""
        if self.field_type is not object:
            return f"Field(name='{self.name}', type={self.field_type.__name__})"
        return f"Field('{self.name}')"

    def __eq__(self, value: Any) -> ComparisonExpression:
        """Override equality to make field comparisons work."""
        return super().__eq__(value)

    def __getattr__(self, attr: str) -> Field[Any]:
        """
        Enable nested field access using dot notation.

        When accessing an attribute that doesn't exist on the Field object,
        this method creates a new Field instance representing the nested path.
        This enables intuitive access to nested MongoDB document fields.

        Parameters
        ----------
        attr : str
            The attribute name to access. Combined with the current field name
            using dot notation to create the nested path.

        Returns
        -------
        Field[Any]
            A new Field instance representing the nested field path.
            The field_type is set to object since nested structure types
            are not tracked.

        Examples
        --------
        Nested field access:

        >>> user_field = Field("user")
        >>> address_city = user_field.address.city
        >>> # Creates Field("user.address.city")
        >>> print(address_city.name)  # "user.address.city"

        >>> # Use in queries
        >>> query = user_field.profile.settings.notifications == True
        >>> mongo_query = query.to_mongodb()
        >>> # Result: {"user.profile.settings.notifications": True}

        Chaining multiple levels:

        >>> document = Field("document")
        >>> deep_field = document.metadata.author.info.email
        >>> # Creates Field("document.metadata.author.info.email")

        Notes
        -----
        - Each access creates a new Field instance
        - Type information is not preserved for nested fields
        - The resulting field can be used in all MongoDB operations
        """
        return Field(f"{self.name}.{attr}", field_type=object)


class ProxyCreationError(Exception):
    """Raised when a model lacks type annotations for proxy creation."""

    def __init__(self, model_name: str) -> None:
        super().__init__(
            f"Model '{model_name}' must have type annotations "
            "(e.g., dataclass or Pydantic model)."
        )


def create_proxy(model: type[Any], prefix: str = "") -> Any:
    """
    Generate a type-safe field proxy from a dataclass or Pydantic model.

    Creates a dynamic proxy object with typed field attributes that enable
    type-safe MongoDB query construction. This function is primarily used
    internally by PipelineBuilder to provide the builder.fields API.

    For most use cases, prefer using PipelineBuilder.fields instead of
    calling this function directly.

    Parameters
    ----------
    model : type[Any]
        A dataclass, Pydantic model, or any class with `__annotations__`.
        Must have type annotations defining field names and types.
    prefix : str, optional
        Internal parameter for nested proxy creation. Prepended to field names
        to create proper dot notation paths. Defaults to "".

    Returns
    -------
    object
        A proxy object with attributes corresponding to model fields.
        Each attribute is either a Field instance (for primitive types)
        or a nested proxy (for dataclass types).

    Raises
    ------
    ProxyCreationError
        If the model class doesn't have `__annotations__` attribute,
        which is required for extracting field information.

    Examples
    --------
    Recommended usage via PipelineBuilder:

    >>> from dataclasses import dataclass
    >>> from mongoex import PipelineBuilder

    >>> @dataclass
    ... class Sale:
    ...     item: str
    ...     price: float
    ...     quantity: int
    ...     category: str

    >>> # Recommended: Use PipelineBuilder.fields
    >>> builder = PipelineBuilder(Sale)
    >>> query = (builder.fields.price > 100) & (
    ...     builder.fields.category == "electronics"
    ... )

    Direct usage (advanced):

    >>> from mongoex.fields import create_proxy
    >>> # Create the proxy directly
    >>> SaleFields = create_proxy(Sale)
    >>> query = (SaleFields.price > 100) & (SaleFields.category == "electronics")

    Nested model support:

    >>> @dataclass
    ... class Address:
    ...     street: str
    ...     city: str
    ...     country: str

    >>> @dataclass
    ... class User:
    ...     name: str
    ...     email: str
    ...     address: Address

    >>> builder = PipelineBuilder(User)
    >>> # Nested access automatically creates proper dot notation
    >>> city_query = builder.fields.address.city == "New York"
    >>> # Generates Field("address.city") for MongoDB dot notation

    Integration patterns:

    >>> # The builder provides its own field proxy
    >>> pipeline = builder.match(builder.fields.price > 100)
    >>>
    >>> # Both approaches work together
    >>> SaleFields = create_proxy(Sale)
    >>> pipeline = builder.match(SaleFields.price > 100)

    Notes
    -----
    - The proxy object is created once and can be reused
    - Nested dataclass fields automatically get their own proxies
    - Field types are preserved for better IDE support
    - Each field access returns a Field instance ready for query operations
    - PipelineBuilder.fields is the recommended API for most use cases
    """
    # Check if model has annotations
    if not hasattr(model, "__annotations__"):
        raise ProxyCreationError(model.__name__)

    # Collect annotations from inheritance chain (MRO - Method Resolution Order)
    all_annotations: dict[str, Any] = {}
    for base in reversed(model.__mro__):
        if hasattr(base, "__annotations__"):
            all_annotations.update(base.__annotations__)

    # Create base proxy class with proper __name__ for better debugging
    proxy_class_name = f"{model.__name__}Fields"

    class ProxyClass:
        """Dynamically generated field proxy class for model fields."""

        def __repr__(self) -> str:
            return proxy_class_name

    # Set proper class name
    ProxyClass.__name__ = proxy_class_name
    ProxyClass.__qualname__ = proxy_class_name

    # Build type annotations dictionary for the proxy class
    proxy_annotations = {}

    # Add typed field proxies or nested proxies
    for field_name, field_type in all_annotations.items():
        full_name = f"{prefix}{field_name}"
        # Check if field_type is a class and is a dataclass
        if inspect.isclass(field_type) and is_dataclass(field_type):
            nested_proxy = create_proxy(field_type, prefix=full_name + ".")
            setattr(ProxyClass, field_name, nested_proxy)
            # For nested dataclasses, use the nested proxy type
            proxy_annotations[field_name] = type(nested_proxy)
        else:
            # Use the unified Field class with type information
            field_instance = Field(full_name, field_type=field_type)
            setattr(ProxyClass, field_name, field_instance)
            # Critical: Use the actual field type for better IDE support
            proxy_annotations[field_name] = field_type

    # Apply annotations to the proxy class for IDE type inference
    ProxyClass.__annotations__ = proxy_annotations

    return ProxyClass()
