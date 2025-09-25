"""Validation and error reporting utilities for MongoEX.

This module provides comprehensive validation infrastructure for MongoEX's
type-safe MongoDB query construction. It includes rich error reporting,
expression analysis, and field validation capabilities that enhance the
developer experience with detailed diagnostics and helpful suggestions.

Key Components:
- QueryValidationError: Rich exception with contextual metadata and suggestions
- ExpressionAnalyzer: Lightweight analyzer for query expression validation
- EnhancedFieldValidator: Model-aware field validation with error enhancement
- Field similarity detection and suggestion generation
- Decorator-based error enhancement for existing validation code

Features:
- Contextual error messages with location information
- Smart field name suggestions using similarity algorithms
- Expression-aware validation with detailed diagnostics
- Integration with Field and PipelineBuilder validation
- Decorator support for upgrading basic validation errors
"""

from __future__ import annotations

import ast
from collections.abc import Callable
from dataclasses import dataclass
from dataclasses import field
from functools import wraps
from typing import Any
from typing import overload


__all__ = [
    "ExpressionAnalyzer",
    "FieldValidator",
    "QueryValidationError",
    "ValidationContext",
    "create_field_validator",
    "enhance_validation_errors",
]


@dataclass(slots=True)
class ValidationContext:
    """Container for optional validation context metadata.

    Parameters
    ----------
    field_name : str | None, optional
        Offending field name, if applicable.
    expression_context : str | None, optional
        High-level textual description of the expression being validated.
    available_fields : list[str]
        All valid field names for the current model.
    suggestions : list[str]
        Suggested alternative field names.
    error_location : str | None, optional
        Human friendly indicator of where the error occurred.
    """

    field_name: str | None = None
    expression_context: str | None = None

    # NOTE: using lambdas to help Pylance infer types correctly.
    #       Just default_factory=list doesn't work and cast would be ugly.
    available_fields: list[str] = field(default_factory=lambda: [])
    suggestions: list[str] = field(default_factory=lambda: [])
    error_location: str | None = None


class QueryValidationError(Exception):
    """
    Rich validation exception with contextual metadata and helpful suggestions.

    QueryValidationError provides enhanced error reporting for MongoEX validation
    failures. Unlike basic exceptions, it includes contextual information, field
    suggestions, and detailed diagnostics to help developers quickly identify
    and fix validation issues.

    The exception is designed for both programmatic inspection (tests can check
    specific attributes) and human-readable error messages with helpful context
    and suggestions for resolution.

    Parameters
    ----------
    field_name : str | None, optional
        Name of the field that caused the validation failure.
        Used for error messages and programmatic inspection.
    expression_context : str | None, optional
        High-level description of the operation or expression context where
        the error occurred (e.g., "Field initialization", "Pipeline match stage").
    available_fields : list[str] | None, optional
        Complete list of valid field names for the model being validated.
        Used to provide context and generate suggestions.
    suggestions : list[str] | None, optional
        List of suggested alternative field names based on similarity to
        the invalid field name. Helps users quickly identify typos.
    error_location : str | None, optional
        Specific location or expression fragment where the error occurred.
        Provides pinpoint accuracy for error identification.

    Attributes
    ----------
    field_name : str | None
        The invalid field name that caused the error.
    expression_context : str | None
        Context description of where the error occurred.
    available_fields : list[str]
        All valid field names for reference.
    suggestions : list[str]
        Suggested corrections for the invalid field name.
    error_location : str | None
        Specific error location information.

    Examples
    --------
    Validation error in pipeline operations:

    >>> from mongoex import PipelineBuilder
    >>> from mongoex.operators import Sum
    >>> from dataclasses import dataclass
    >>>
    >>> @dataclass
    >>> class Product:
    ...     name: str
    ...     price: float
    >>>
    >>> builder = PipelineBuilder(Product)
    >>> try:
    ...     # This will raise QueryValidationError for invalid field in group operation
    ...     pipeline = builder.group(by="priice", total=Sum("price"))  # typo: "priice"
    ... except QueryValidationError as e:
    ...     print(e.field_name)  # "priice"
    ...     print(e.suggestions)  # ["price"] (similar fields)
    ...     print(e.available_fields)  # ["name", "price"]

    Error with full context:

    >>> error = QueryValidationError.field_not_valid(
    ...     "priice",  # typo in "price"
    ...     expression_context="Pipeline match stage",
    ...     available_fields=["name", "price", "category"],
    ...     suggestions=["price"],
    ...     error_location="builder.fields.priice > 100",
    ... )
    >>> print(error)
    # Field priice is not valid.
    # Location: builder.fields.priice > 100
    # Context: Pipeline match stage
    # Available fields: category, name, price
    # Did you mean: price?

    Programmatic inspection:

    >>> try:
    ...     # Some validation operation
    ...     pass
    ... except QueryValidationError as e:
    ...     if e.field_name == "expected_typo":
    ...         # Handle specific field error
    ...         suggested = e.suggestions[0] if e.suggestions else None

    Notes
    -----
    - Error messages are formatted for human readability
    - All attributes are optional to support various validation scenarios
    - Suggestions are automatically generated using similarity algorithms
    - Integration with Field and PipelineBuilder validation systems
    """

    def __init__(
        self,
        field_name: str | None = None,
        *,
        expression_context: str | None = None,
        available_fields: list[str] | None = None,
        suggestions: list[str] | None = None,
        error_location: str | None = None,
    ) -> None:
        self.field_name = field_name
        self.expression_context = expression_context
        self.available_fields = available_fields or []
        self.suggestions = suggestions or []
        self.error_location = error_location
        super().__init__(self._format(f"Field {field_name} is not valid."))

    def _format(self, base: str) -> str:
        parts = [base]
        if self.error_location:
            parts.append(f"\n📍 Error location: {self.error_location}")
        if self.expression_context:
            parts.extend(["\n🔍 Expression context:", f"   {self.expression_context}"])
        if self.available_fields:
            parts.append(
                "\n✅ Available fields: " + ", ".join(sorted(self.available_fields))
            )
        if self.suggestions:
            parts.append("\n💡 Did you mean: " + ", ".join(self.suggestions) + "?")
        return "".join(parts)

    @classmethod
    def field_not_valid(
        cls,
        field_name: str,
        *,
        expression_context: str | None,
        available_fields: list[str],
        suggestions: list[str],
        error_location: str,
    ) -> QueryValidationError:
        """Create a ``QueryValidationError`` for an invalid field reference."""
        return cls(
            field_name,
            expression_context=expression_context,
            available_fields=available_fields,
            suggestions=suggestions,
            error_location=error_location,
        )


class ExpressionAnalyzer(ast.NodeVisitor):
    """Analyze query expression objects for validation and context extraction."""

    def __init__(self, valid_fields: set[str]) -> None:
        self.valid_fields = valid_fields
        self.expression_parts: list[str] = []
        self.current_context: str = ""
        # Collected error locations (used by tests)
        self.error_locations: list[str] = []

    def analyze_expression(self, expression: Any, context: str) -> dict[str, Any]:
        """Analyze an expression returning structured diagnostic info.

        Parameters
        ----------
        expression : Any
            The expression tree / object graph to inspect.
        context : str
            High-level context string for inclusion in error messages.

        Returns
        -------
        dict[str, Any]
            Dictionary containing validation status, parts, and potential error.
        """
        self.current_context = context
        self.expression_parts = []
        try:
            self._walk(expression)
        except QueryValidationError as err:  # pragma: no cover - exercised indirectly
            return {
                "valid": False,
                "error": err,
                "expression_parts": self.expression_parts,
                "context": context,
            }
        return {
            "valid": True,
            "expression_parts": self.expression_parts,
            "context": context,
        }

    def _walk(self, expr: Any, depth: int = 0) -> None:
        indent = "  " * depth
        if hasattr(expr, "field_name"):
            field_name = expr.field_name
            operator = getattr(expr, "operator", "?")
            value = getattr(expr, "value", "?")
            self._validate_field(field_name, f"{indent}{field_name} {operator} {value}")
            self.expression_parts.append(
                f"{indent}Field '{field_name}' {operator} {value}"
            )
        elif hasattr(expr, "expressions"):
            exprs = expr.expressions
            expr_type = "AND" if "And" in expr.__class__.__name__ else "OR"
            self.expression_parts.append(f"{indent}{expr_type} expression:")
            for idx, sub in enumerate(exprs):
                self.expression_parts.append(f"{indent}  [{idx + 1}]:")
                self._walk(sub, depth + 2)
        elif isinstance(expr, str):
            self._validate_field(expr, f"{indent}Field: {expr}")
            self.expression_parts.append(f"{indent}Field: {expr}")

    def _validate_field(self, field_name: str, location: str) -> None:
        # For nested fields like "user.address.city", check if the root field exists
        root_field = field_name.split(".", 1)[0]

        if root_field not in self.valid_fields:
            suggestions = self._suggest(root_field)
            self.error_locations.append(location)
            raise QueryValidationError.field_not_valid(
                root_field,
                expression_context=self.current_context,
                available_fields=sorted(self.valid_fields),
                suggestions=suggestions,
                error_location=location,
            )

    def _suggest(self, field_name: str, max_items: int = 3) -> list[str]:
        lower = field_name.lower()
        matches: list[str] = []
        for f in self.valid_fields:
            fl = f.lower()
            if lower in fl or fl.startswith(lower[:2]):
                matches.append(f)
            if len(matches) >= max_items:
                break
        return matches

    def find_similar_fields(self, field_name: str, max_items: int = 3) -> list[str]:
        """Return similar field names based on substring/prefix heuristics."""
        return self._suggest(field_name, max_items)


def create_field_validator(model: type[Any]) -> FieldValidator:
    """Create a field validator for an annotated (e.g., dataclass) model.

    Parameters
    ----------
    model : type[Any]
        A class that may define ``__annotations__`` mapping field names to
        types. Missing annotations are tolerated (an empty validator results).

    Returns
    -------
    EnhancedFieldValidator
        Configured validator bound to the provided model.
    """
    annotations = getattr(model, "__annotations__", {}) or {}
    valid = set(annotations.keys())
    return FieldValidator(valid, model.__name__)


class FieldValidator:
    """Validate field names and expression objects against a model."""

    def __init__(self, valid_fields: set[str], model_name: str) -> None:
        self.valid_fields = valid_fields
        self.model_name = model_name
        self._analyzer = ExpressionAnalyzer(valid_fields)

    @property
    def analyzer(self) -> ExpressionAnalyzer:
        """Return the internal expression analyzer (for tests)."""
        return self._analyzer

    def validate_field_name(self, field_name: str, context: str = "") -> None:
        """
        Validate a field name, raising ``QueryValidationError`` if invalid.

        Parameters
        ----------
        field_name : str
            Field name to validate.
        context : str, optional
            Extra contextual phrase; when omitted a default descriptive phrase
            is generated to satisfy test expectations.

        Raises
        ------
        QueryValidationError.field_not_valid
            If `field_name` is not present in the model's valid field set.
        """
        # For nested fields like "user.address.city", check if the root field exists
        root_field = field_name.split(".", 1)[0]

        if root_field not in self.valid_fields:
            suggestions = self._analyzer.find_similar_fields(root_field)
            default_ctx = f"Field validation for {self.model_name} model"
            raise QueryValidationError.field_not_valid(
                root_field,
                expression_context=context or default_ctx,
                available_fields=sorted(self.valid_fields),
                suggestions=suggestions,
                error_location=f"Field reference: '{field_name}'",
            )

    @overload
    def validate_field(self, field_name: str, context: str) -> None: ...

    @overload
    def validate_field(self, field_name: int, context: str) -> None: ...

    @overload
    def validate_field(self, field_name: float, context: str) -> None: ...

    def validate_field(self, field_name: str | int | float, context: str) -> None:
        """
        Validate a field with rich error reporting.

        Parameters
        ----------
        field_name : str | int | float
            Field name to validate. String fields support nested fields
            (e.g., "user.address.city"). Numeric literals (int/float) are
            automatically skipped (e.g., Sum(1) for counting).
        context : str
            Context description for error reporting.

        Raises
        ------
        QueryValidationError.field_not_valid
            If `field_name` root field is not present in the model's valid field set.
            Only raised for string field names - numeric literals are silently ignored.
        """
        # Skip validation for numeric literals (e.g., Sum(1) for counting)
        if isinstance(field_name, (int, float)):
            return

        # For nested fields like "user.address.city", check if the root field exists
        root_field = field_name.split(".", 1)[0]

        if root_field not in self.valid_fields:
            suggestions = self._analyzer.find_similar_fields(root_field)
            raise QueryValidationError.field_not_valid(
                root_field,
                expression_context=f"{context} for {self.model_name} model",
                available_fields=sorted(self.valid_fields),
                suggestions=suggestions,
                error_location=f"Field reference: '{field_name}'",
            )

    def validate_expression(self, expression: Any, context: str = "") -> None:
        """
        Validate an expression object graph.

        Parameters
        ----------
        expression : Any
            Expression / object tree to validate.
        context : str, optional
            Additional phrase appended to the default query context.
        """
        base = f"Query on {self.model_name} model"
        full_context = base if not context else f"{base} ({context})"
        analysis = self._analyzer.analyze_expression(expression, full_context)
        if not analysis["valid"]:
            raise analysis["error"]


def enhance_validation_errors[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Return decorator enriching basic validation related errors.

    Parameters
    ----------
    func : Callable[P, R]
        Function whose raised AttributeError / ValueError should be
        converted when they appear to reference field validity.

    Returns
    -------
    Callable[P, R]
        Wrapped function that raises QueryValidationError for validation
        related low-level errors.
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except (AttributeError, ValueError) as exc:
            msg_lower = str(exc).lower()
            if "field" in msg_lower or "valid" in msg_lower:
                raise QueryValidationError(
                    str(exc),
                    expression_context=f"Error in {func.__name__}",
                    suggestions=[
                        "Check field spelling",
                        "Verify model definition",
                    ],
                ) from None
            raise

    return wrapper
