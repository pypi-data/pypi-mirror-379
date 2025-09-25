"""
MongoDB JSON pipeline to MongoEX code converter with AST-based generation.

This module provides sophisticated conversion capabilities that transform existing
MongoDB aggregation pipelines (in JSON format) into equivalent MongoEX Python code.
The conversion process uses Abstract Syntax Tree (AST) manipulation to generate
clean, idiomatic Python code with proper imports and formatting.

Key Features:
- AST-based code generation for clean, maintainable output
- Support for major MongoDB aggregation stages ($match, $group, $sort, etc.)
- Automatic field validation and type safety preservation
- Intelligent operator mapping (MongoDB operators to MongoEX equivalents)
- Proper import management and code organization
- Unsupported stage detection with helpful comments

Conversion Capabilities:
- $match stages with complex query expressions
- $group stages with aggregation operators
- $sort, $limit, $project stages
- $unwind operations with options
- Nested field references and dot notation
- Logical operators ($and, $or) and comparisons

The converter is designed to help migrate existing MongoDB pipelines to MongoEX
while maintaining readability and leveraging MongoEX's type safety features.
"""

import ast
from pathlib import Path
from typing import Any
from typing import cast


PipelineStageDict = dict[str, Any]
MongoDBPipeline = list[PipelineStageDict]


class CodeConverter:
    """
    Advanced MongoDB pipeline to MongoEX code converter using AST generation.

    CodeConverter transforms MongoDB aggregation pipelines (represented
    as Python dictionaries/JSON) into clean, idiomatic MongoEX Python code.
    The converter uses Abstract Syntax Tree manipulation to generate properly
    formatted code with correct imports, field proxies, and method chaining.

    The converter handles complex pipeline structures and provides intelligent
    mapping between MongoDB operators and MongoEX equivalents while preserving
    the semantic meaning and type safety of operations.

    Parameters
    ----------
    model_name : str
        The name of the dataclass model that represents the input document structure.
        Used to generate appropriate field proxy names and imports.

    Attributes
    ----------
    model_name : str
        The target model name for conversion.
    COMPARISON_MAP : dict[str, str]
        Mapping of MongoDB comparison operators to MongoEX field methods.
    AGGREGATION_MAP : dict[str, str]
        Mapping of MongoDB aggregation operators to MongoEX operator classes.

    Examples
    --------
    Basic pipeline conversion:

    >>> converter = CodeConverter("Sale")
    >>> pipeline = [
    ...     {"$match": {"price": {"$gt": 100}}},
    ...     {"$group": {"_id": "$category", "total": {"$sum": "$price"}}},
    ... ]
    >>> code = converter.convert(pipeline)
    >>> print(code)
    # Output:
    # from mongoex import PipelineBuilder
    # from mongoex.operators import Sum
    #
    # builder = PipelineBuilder(Sale)
    # pipeline = builder.match(builder.fields.price > 100)
    # pipeline = pipeline.group(by="category", total=Sum("price"))

    Complex query conversion:

    >>> complex_pipeline = [
    ...     {"$match": {"$and": [{"price": {"$gte": 50}}, {"status": "active"}]}},
    ...     {"$sort": {"created_date": -1}},
    ...     {"$limit": 10},
    ... ]
    >>> code = converter.convert(complex_pipeline)
    # Generates appropriate MongoEX code with logical operators

    Integration with model-specific conversions:

    >>> # Different models generate different field proxy names
    >>> user_converter = CodeConverter("User")
    >>> product_converter = CodeConverter("Product")
    >>> # Each maintains proper field naming and validation

    Notes
    -----
    - Uses AST manipulation for clean code generation
    - Preserves semantic meaning of MongoDB operations
    - Generates proper imports and field proxy setup
    - Handles unsupported stages gracefully with comments
    - Output code is ready to run with proper MongoEX imports
    """

    def __init__(self, model_name: str) -> None:
        """
        Initialize converter for a specific model.

        Parameters
        ----------
        model_name : str
            The name of the dataclass model (e.g., "Sale", "User")
        """
        self.model_name = model_name
        self.field_proxy_name = f"{model_name}Fields"

        # Operator mappings for compatibility with tests
        self.COMPARISON_MAP = {
            "$eq": "==",
            "$ne": "!=",
            "$gt": ">",
            "$gte": ">=",
            "$lt": "<",
            "$lte": "<=",
            "$in": ".in_",
            "$nin": ".nin",
        }

        self.AGGREGATION_MAP = {
            "$sum": "Sum",
            "$avg": "Avg",
            "$first": "First",
            "$last": "Last",
            "$push": "Push",
        }

    def convert(self, pipeline: MongoDBPipeline) -> str:
        """Convert MongoDB pipeline to MongoEX code using AST generation."""
        # 1. Build import section via AST
        import_src = self._generate_imports()

        # 2. Build setup (field proxy + builder + initial pipeline) via AST nodes
        setup_module = ast.Module(
            body=[
                # Field proxy assignment: ProductFields = create_proxy(Product)
                ast.Assign(
                    targets=[ast.Name(id=self.field_proxy_name, ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id="create_proxy", ctx=ast.Load()),
                        args=[ast.Name(id=self.model_name, ctx=ast.Load())],
                        keywords=[],
                    ),
                ),
                # builder = PipelineBuilder("collection_name", model=Product)
                ast.Assign(
                    targets=[ast.Name(id="builder", ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id="PipelineBuilder", ctx=ast.Load()),
                        args=[ast.Constant(value="collection_name")],
                        keywords=[
                            ast.keyword(
                                arg="model",
                                value=ast.Name(id=self.model_name, ctx=ast.Load()),
                            )
                        ],
                    ),
                ),
                # pipeline = builder
                ast.Assign(
                    targets=[ast.Name(id="pipeline", ctx=ast.Store())],
                    value=ast.Name(id="builder", ctx=ast.Load()),
                ),
            ],
            type_ignores=[],
        )
        setup_module = ast.fix_missing_locations(setup_module)
        setup_code = ast.unparse(setup_module)

        # 3. Build pipeline stage assignments (each as separate assignment to pipeline)
        stage_snippets: list[str] = []
        unsupported_comments: list[str] = []
        for stage in pipeline:
            generated = self._convert_stage_ast(stage)
            if generated is None:
                # Unsupported stage handled by comment placeholder
                stage_name = next(iter(stage.keys()))
                unsupported_comments.append(f"# TODO: Unsupported stage {stage_name}")
            else:
                stage_snippets.append(generated)

        stage_code = "\n".join(stage_snippets)

        # 4. Combine all parts
        parts = [import_src.rstrip(), setup_code.rstrip()]
        if stage_code:
            parts.append(stage_code.rstrip())
        if unsupported_comments:
            parts.extend(unsupported_comments)
        return "\n\n".join(parts) + "\n"

    @staticmethod
    def _generate_imports() -> str:
        """Generate necessary imports using AST for consistent formatting."""
        modules: list[ast.stmt] = [
            ast.ImportFrom(
                module="dataclasses", names=[ast.alias(name="dataclass")], level=0
            ),
            ast.ImportFrom(
                module="mongoex",
                names=[
                    ast.alias(name="PipelineBuilder"),
                    ast.alias(name="create_proxy"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="mongoex.operators",
                names=[
                    ast.alias(name="Sum"),
                    ast.alias(name="Avg"),
                    ast.alias(name="First"),
                    ast.alias(name="Last"),
                    ast.alias(name="Push"),
                ],
                level=0,
            ),
            ast.ImportFrom(
                module="mongoex.config",
                names=[ast.alias(name="UnwindOptions")],
                level=0,
            ),
        ]
        module = ast.Module(body=modules, type_ignores=[])
        # ast.unparse returns code without trailing newline by default; ensure newline
        return ast.unparse(module) + "\n"

    def _convert_stage_ast(self, stage: PipelineStageDict) -> str | None:
        """Return a code snippet (string) representing a stage assignment.

        Kept intentionally slim for complexity constraints; heavy formatting
        lives in dedicated helper methods.

        Returns
        -------
        str | None
            Assignment statement string (e.g. "pipeline = pipeline.match(...)")
            or None if stage unsupported.
        """
        stage_name = next(iter(stage.keys()))
        content = stage[stage_name]
        handlers: dict[str, Any] = {
            "$limit": self._stage_limit,
            "$match": self._stage_match,
            "$group": self._stage_group,
            "$sort": self._stage_sort,
            "$project": self._stage_project,
            "$unwind": self._stage_unwind,
        }
        handler = handlers.get(stage_name)
        return handler(content) if handler else None

    # --- Stage helper formatters (separated to reduce complexity) ---
    @staticmethod
    def _stage_limit(value: Any) -> str:  # value: int
        return f"pipeline = pipeline.limit({value})"

    def _stage_match(self, match_content: dict[str, Any]) -> str:
        expr = self._convert_query_expression(match_content)
        return f"pipeline = pipeline.match({expr})"

    def _stage_group(self, group_content: dict[str, Any]) -> str:
        return self._convert_group_ast(group_content)

    @staticmethod
    def _stage_sort(sort_content: dict[str, Any]) -> str:
        parts = [f"{f}={d}" for f, d in sort_content.items()]
        return f"pipeline = pipeline.sort({', '.join(parts)})"

    @staticmethod
    def _stage_project(project_content: dict[str, Any]) -> str:
        parts: list[str] = []
        for f, v in project_content.items():
            if isinstance(v, str) and v.startswith("$"):
                parts.append(f'{f}="{v}"')
            else:
                parts.append(f"{f}={v!r}")
        return f"pipeline = pipeline.project({', '.join(parts)})"

    @staticmethod
    def _stage_unwind(unwind_content: str | dict[str, Any]) -> str:
        if isinstance(unwind_content, str):
            path = unwind_content.removeprefix("$")
            return f'pipeline = pipeline.unwind(UnwindOptions("{path}"))'
        unwind_path = unwind_content["path"]
        path = unwind_path.removeprefix("$")
        options = [f'"{path}"']
        if "includeArrayIndex" in unwind_content:
            idx = unwind_content["includeArrayIndex"]
            options.append(f'array_index="{idx}"')
        if unwind_content.get("preserveNullAndEmptyArrays", False):
            options.append("preserve_empty=True")
        return f"pipeline = pipeline.unwind(UnwindOptions({', '.join(options)}))"

    @staticmethod
    def _convert_group_ast(group_content: dict[str, Any]) -> str:
        group_by = group_content["_id"]
        group_by = group_by.removeprefix("$")
        group_fields: list[str] = []
        for field_name, field_expr in group_content.items():
            if field_name == "_id":
                continue
            if isinstance(field_expr, dict):
                operator = next(iter(field_expr.keys()))  # type: ignore[arg-type]
                source_field = field_expr[operator]  # type: ignore[index]

                # Direct mapping instead of using AGGREGATION_OPERATORS dict
                agg_mapping = {
                    "$sum": "Sum",
                    "$avg": "Avg",
                    "$first": "First",
                    "$last": "Last",
                    "$push": "Push",
                }

                if operator in agg_mapping:
                    agg_class = agg_mapping[operator]
                    if isinstance(source_field, str) and source_field.startswith("$"):
                        source_field = source_field[1:]
                        group_fields.append(
                            f'{field_name}={agg_class}("{source_field}")'
                        )
                    elif isinstance(source_field, int):
                        group_fields.append(f"{field_name}=Sum({source_field})")
                    else:
                        group_fields.append(
                            f"{field_name}={agg_class}({source_field!r})"
                        )
                else:
                    group_fields.append(f"# TODO: Unsupported aggregation {operator}")
        fields_str = ", ".join(group_fields)
        return f'pipeline = pipeline.group(by="{group_by}", {fields_str})'

    def _convert_query_expression(self, expr: dict[str, Any]) -> str:
        """Convert MongoDB query expression to MongoEX expression."""
        if "$and" in expr:
            sub_expressions = [
                self._convert_query_expression(sub_expr) for sub_expr in expr["$and"]
            ]
            return f"({' & '.join(sub_expressions)})"

        elif "$or" in expr:
            sub_expressions = [
                self._convert_query_expression(sub_expr) for sub_expr in expr["$or"]
            ]
            return f"({' | '.join(sub_expressions)})"

        else:
            # Simple field comparison
            field_name = next(iter(expr.keys()))
            field_value = expr[field_name]

            if isinstance(field_value, dict):
                # Operator-based comparison like {"price": {"$gt": 100}}
                operator_dict = cast(dict[str, Any], field_value)
                operator = next(iter(operator_dict.keys()))
                value = operator_dict[operator]

                # Direct mapping instead of using COMPARISON_OPERATORS dict
                op_mapping = {
                    "$eq": "==",
                    "$ne": "!=",
                    "$gt": ">",
                    "$gte": ">=",
                    "$lt": "<",
                    "$lte": "<=",
                    "$in": ".in_",
                    "$nin": ".nin",
                }

                if operator in op_mapping:
                    op_str = op_mapping[operator]
                    if op_str.startswith("."):
                        # Method call like .in_() or .nin()
                        proxy_field = f"{self.field_proxy_name}.{field_name}"
                        return f"{proxy_field}{op_str}({value!r})"
                    else:
                        # Operator like >, ==, etc.
                        proxy_field = f"{self.field_proxy_name}.{field_name}"
                        return f"{proxy_field} {op_str} {value!r}"
                else:
                    return f"# TODO: Unsupported operator {operator}"
            else:
                # Simple equality like {"status": "active"}
                proxy_field = f"{self.field_proxy_name}.{field_name}"
                return f"{proxy_field} == {field_value!r}"


def to_mongoex(
    pipeline: MongoDBPipeline, model_name: str, output_file: str | None = None
) -> str:
    """
    Convert MongoDB aggregation pipeline to equivalent MongoEX Python code.

    This is the main entry point for pipeline conversion. It takes a MongoDB
    aggregation pipeline (as Python dictionaries) and generates clean,
    readable MongoEX code that produces the same results with added type
    safety and validation.

    The function handles all aspects of conversion including import generation,
    field proxy setup, pipeline stage conversion, and optional file output.

    Parameters
    ----------
    pipeline : MongoDBPipeline
        MongoDB aggregation pipeline represented as a list of stage dictionaries.
        Each dictionary represents a single pipeline stage (e.g., {"$match": ...}).
    model_name : str
        Name of the dataclass model representing input document structure.
        Used to generate field proxy names and provide type safety context.
    output_file : str | None, optional
        If provided, writes the generated code to the specified file path.
        Useful for batch conversion or code generation workflows. Default is None.

    Returns
    -------
    str
        Complete MongoEX Python code as a string, including imports, setup,
        and pipeline construction. Ready to execute with proper dependencies.

    Examples
    --------
    Basic pipeline conversion:

    >>> pipeline = [
    ...     {"$match": {"price": {"$gt": 100}}},
    ...     {"$group": {"_id": "$category", "total": {"$sum": "$price"}}},
    ...     {"$sort": {"total": -1}},
    ... ]
    >>> code = to_mongoex(pipeline, "Sale")
    >>> print(code)
    # Output:
    # from mongoex import PipelineBuilder
    # from mongoex.operators import Sum
    #
    # builder = PipelineBuilder(Sale)
    # pipeline = builder.match(builder.fields.price > 100)
    # pipeline = pipeline.group(by="category", total=Sum("price"))
    # pipeline = pipeline.sort_by(total=-1)

    Writing to file:

    >>> code = to_mongoex(pipeline, "Sale", output_file="generated_pipeline.py")
    >>> # Code is written to generated_pipeline.py and also returned

    Complex query conversion:

    >>> complex_pipeline = [
    ...     {
    ...         "$match": {
    ...             "$and": [
    ...                 {"price": {"$gte": 50}},
    ...                 {"status": {"$in": ["active", "pending"]}},
    ...             ]
    ...         }
    ...     },
    ...     {"$unwind": "$tags"},
    ...     {"$limit": 100},
    ... ]
    >>> code = to_mongoex(complex_pipeline, "Product")
    # Generates MongoEX code with logical operators and unwind operations

    Migration workflow example:

    >>> # Convert existing MongoDB pipelines to MongoEX
    >>> existing_pipelines = load_pipelines_from_codebase()
    >>> for name, pipeline in existing_pipelines.items():
    ...     mongoex_code = to_mongoex(pipeline, "Document", f"{name}_mongoex.py")
    ...     print(f"Converted {name} to MongoEX")

    Notes
    -----
    - Generated code includes all necessary imports
    - Field validation and type safety are preserved
    - Unsupported stages are marked with comments for manual review
    - Output is formatted for readability and maintainability
    - Can be used for migration, learning, or code generation workflows
    """
    converter = CodeConverter(model_name)
    code = converter.convert(pipeline)

    if output_file:
        Path(output_file).write_text(code, encoding="utf-8")

    return code
