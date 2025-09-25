# MongoEX
### Type-Safe MongoDB Queries in Python

Welcome to MongoEX! This project is a modern Python library for building MongoDB queries with full type safety, IDE autocompletion, and compile-time validation. My goal is to make your database interactions as safe and developer-friendly as possible.

## Core Features

- **Fluent Query Builder**: Chain methods to build complex aggregation pipelines.
- **Type-Safe Fields**: Catch errors at compile-time with type-safe field proxies.
- **Model-Based Aggregation**: Define aggregation transformations using strongly-typed dataclass models with versioning support.
- **IDE Autocompletion**: Get intelligent suggestions for fields and operators in your IDE.
- **AST-Based Code Generation**: Convert existing MongoDB JSON pipelines into clean, readable MongoEX code.
- **Enhanced Error Reporting**: Get clear, contextual error messages with suggestions for typos.

## Quick Example

```python
from dataclasses import dataclass
from mongoex import PipelineBuilder
from mongoex.operators import Sum

@dataclass
class Sale:
    item: str
    price: float
    quantity: int

# Build a pipeline with type-safe field access
builder = PipelineBuilder(model=Sale)
pipeline = (
    builder.match(builder.fields.price > 50)
    .group(by="item", total_revenue=Sum("price"))
)

# The builder can be used directly with PyMongo
# result = db.sales.aggregate(pipeline)

# The generated pipeline:
# [
#     {'$match': {'price': {'$gt': 50}}},
#     {'$group': {'_id': '$item', 'total_revenue': {'$sum': '$price'}}}
# ]
```

## Examples

- `examples/01_basic_pipeline.py`: A basic example of building a pipeline.
- `examples/02_advanced_grouping.py`: Demonstrating advanced grouping operations and output validation.
- `examples/03_json_to_mongoex.py`: How to convert a JSON pipeline to MongoEX code.
- `examples/04_logical_operations.py`: Demonstrating `AND` and `OR` operations.
- `examples/05_error_handling.py`: Demonstrating the enhanced error reporting.
- `examples/06_complex_analytics_pipeline.py`: A complex, multi-stage analytics pipeline example.

## Model-Based Aggregation

MongoEX introduces a powerful **Model-Based Aggregation** system that allows you to define aggregation pipelines using strongly-typed dataclass models. This approach provides enhanced type safety, better maintainability, and clear versioning of data transformations.

### Key Benefits

- **Type-Safe Transformations**: Define aggregation operations using `Annotated[type, Operator]` syntax
- **Versioned Models**: Track and version your data transformations using dataclass models
- **Compile-Time Validation**: Catch aggregation errors before runtime with full IDE support
- **Reusable Components**: Share aggregation models across different pipelines and applications
- **Self-Documenting Code**: Models serve as living documentation of your data transformations

### Basic Example

```python
from typing import Annotated
from dataclasses import dataclass
from mongoex import PipelineBuilder
from mongoex.operators import Sum, Avg, First

@dataclass
class CategoryAnalysis:
    """Revenue analysis model for product categories."""
    _id: str  # The grouped field (category name)
    total_revenue: Annotated[float, Sum("price")]
    avg_price: Annotated[float, Avg("price")]
    transaction_count: Annotated[int, Sum(1)]
    first_sale: Annotated[str, First("item")]

# Usage with model-based grouping
builder = PipelineBuilder(model=Sale)
pipeline = (
    builder.match(builder.fields.price > 10)
    .group(by="category", model=CategoryAnalysis)  # ← Type-safe model
    .sort_by(total_revenue=-1)
)

# Generates identical pipeline to traditional approach, but with full type safety
```

### Advanced Features

**Model Versioning for Data Transformations:**
```python
@dataclass 
class CustomerAnalysisV1:
    """Version 1: Basic customer metrics."""
    _id: str
    total_spent: Annotated[float, Sum("amount")]
    order_count: Annotated[int, Sum(1)]

@dataclass
class CustomerAnalysisV2:
    """Version 2: Enhanced with lifetime value calculation."""
    _id: str
    total_spent: Annotated[float, Sum("amount")]
    order_count: Annotated[int, Sum(1)]
    avg_order_value: Annotated[float, Avg("amount")]
    first_order_date: Annotated[str, First("order_date")]
```

**Pipeline Stage Composition:**
```python
# Build complex analytics with multiple model-based stages
analytics_pipeline = (
    builder.match(builder.fields.status == "completed")
    .group(by="customer_id", model=CustomerLifetimeValue)
    .match(builder.fields.total_spent > 1000)  # High-value customers
    .sort_by(lifetime_value=-1)
)
```

### Available Operators

- `Sum("field")` - Sum values from a field
- `Sum(1)` - Count documents (literal count)
- `Avg("field")` - Average values from a field
- `First("field")` - First value in group
- `Last("field")` - Last value in group

### Documentations

You can find some syntax examples / tutorials at [tutorials folder](./tutorials/)

- [01 - fundamentals](./tutorials/01_fundamentals/)
- [02 - operators](./tutorials/02_operators/)
- [03 - aggregation](./tutorials/03_aggregation/)
- [04 - advanced](./tutorials/04_advanced/)
- [05 - live samples](./tutorials/05_live/)


## Development Status

MongoEX is currently in an early development stage. I am actively working on expanding the API, improving performance, and adding support for more MongoDB operators.

## Contributing

I welcome contributions! To get started, please check out the development workflow in our `makefile`.

- `make format lint`: Format and lint your code.
- `make type-check`: Run the type checker.
- `make test`: Run the full test suite.
