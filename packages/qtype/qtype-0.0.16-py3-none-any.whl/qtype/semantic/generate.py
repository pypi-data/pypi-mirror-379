import argparse
import inspect
import subprocess
from pathlib import Path
from textwrap import dedent
from typing import Any, Literal, Union, get_args, get_origin

import networkx as nx

import qtype.dsl.model as dsl
from qtype.dsl.validator import _is_dsl_type

FIELDS_TO_IGNORE = {"Application.references"}
TYPES_TO_IGNORE = {
    "CustomType",
    "DecoderFormat",
    "Document",
    "Flow",
    "ListType",
    "PrimitiveTypeEnum",
    "StrictBaseModel",
    "StructuralTypeEnum",
    "TypeDefinition",
    "ToolParameter",
    "Variable",
}

FROZEN_TYPES = {
    "AuthorizationProvider",
    "DocumentIndex",
    "EmbeddingModel",
    "Index",
    "Memory",
    "Model",
    "Tool",
    "VectorIndex",
}


def sort_classes_by_inheritance(
    classes: list[tuple[str, type]],
) -> list[tuple[str, type]]:
    """Sort classes based on their inheritance hierarchy."""
    graph: nx.DiGraph = nx.DiGraph()
    class_dict = dict(classes)

    # Build dependency graph
    for class_name, cls in classes:
        graph.add_node(class_name)
        for base in cls.__bases__:
            if (
                hasattr(base, "__module__")
                and base.__module__ == dsl.__name__
                and base.__name__ not in TYPES_TO_IGNORE
                and not base.__name__.startswith("_")
            ):
                graph.add_edge(base.__name__, class_name)

    sorted_names = list(nx.topological_sort(graph))

    # sorted_names = sorted(graph.nodes, key=lambda node: depths[node])
    return [(name, class_dict[name]) for name in sorted_names]


def generate_semantic_model(args: argparse.Namespace) -> None:
    """Generate semantic model classes from DSL model classes.

    This function inspects the DSL model classes and generates corresponding
    semantic model classes where string ID references are replaced with actual
    object references.
    """
    output_path = Path(args.output)

    # Get all classes from the DSL model module
    dsl_classes = []
    for name, cls in inspect.getmembers(dsl, inspect.isclass):
        if (
            cls.__module__ == dsl.__name__
            and not name.startswith("_")
            and name not in TYPES_TO_IGNORE
            and not name.endswith("List")
        ):
            dsl_classes.append((name, cls))

    # Sort classes based on inheritance hierarchy
    sorted_classes = sort_classes_by_inheritance(dsl_classes)

    # Generate semantic classes in sorted order
    generated = [
        generate_semantic_class(class_name, cls)
        for class_name, cls in sorted_classes
    ]

    # Write to output file
    with open(output_path, "w") as f:
        # Write header
        f.write(
            dedent('''
            """
            Semantic Intermediate Representation models.

            This module contains the semantic models that represent a resolved QType
            specification where all ID references have been replaced with actual object
            references.

            Generated automatically with command:
            qtype generate semantic-model

            Types are ignored since they should reflect dsl directly, which is type checked.
            """

        ''').lstrip()
        )

        # Write imports
        f.write(
            dedent("""
            from __future__ import annotations

            from typing import Any, Literal

            from pydantic import BaseModel, Field, model_validator

            # Import enums and type aliases from DSL
            from qtype.dsl.model import (  # noqa: F401
                CustomType,
                DecoderFormat,
                ListType,
                PrimitiveTypeEnum,
                StepCardinality,
                StructuralTypeEnum,
                ToolParameter
            )
            from qtype.dsl.model import Variable as DSLVariable  # noqa: F401
            from qtype.dsl.model import VariableType  # noqa: F401
            from qtype.semantic.base_types import ImmutableModel

        """).lstrip()
        )

        # Write the new variable class
        f.write(
            dedent('''
            class Variable(DSLVariable, BaseModel):
                """Semantic version of DSL Variable with ID references resolved."""
                value: Any | None = Field(None, description="The value of the variable")
                def is_set(self) -> bool:
                    return self.value is not None

        ''').lstrip()
        )

        # Write classes
        f.write("\n\n".join(generated))

        # Write the Flow class which _could_ be generated but we want a validator to update it's carndiality
        f.write("\n\n")
        f.write(
            dedent('''
            class Flow(Step):
                """Defines a flow of steps that can be executed in sequence or parallel.
                If input or output variables are not specified, they are inferred from
                the first and last step, respectively.
                """

                description: str | None = Field(
                    None, description="Optional description of the flow."
                )
                cardinality: StepCardinality = Field(
                    StepCardinality.auto,
                    description="The cardinality of the flow, inferred from its steps when set to 'auto'.",
                )
                mode: Literal["Complete", "Chat"] = Field("Complete")
                steps: list[Step] = Field(..., description="List of steps or step IDs.")

                @model_validator(mode="after")
                def infer_cardinality(self) -> "Flow":
                    if self.cardinality == StepCardinality.auto:
                        self.cardinality = StepCardinality.one
                        for step in self.steps:
                            if step.cardinality == StepCardinality.many:
                                self.cardinality = StepCardinality.many
                                break
                    return self

        ''').lstrip()
        )

    # Format the file with Ruff
    format_with_ruff(str(output_path))


def format_with_ruff(file_path: str) -> None:
    """Format the given file using Ruff and isort to match pre-commit configuration."""
    # Apply the same formatting as pre-commit but only to the specific file
    # Use --force-exclude to match pre-commit behavior exactly
    subprocess.run(["ruff", "check", "--fix", file_path], check=True)
    subprocess.run(
        ["ruff", "format", "--force-exclude", file_path], check=True
    )
    subprocess.run(["isort", file_path], check=True)


DSL_ONLY_UNION_TYPES = {
    get_args(dsl.ToolType): "Tool",
    get_args(dsl.StepType): "Step",
    get_args(dsl.IndexType): "Index",
    get_args(dsl.ModelType): "Model",
}


def _transform_union_type(args: tuple) -> str:
    """Transform Union types, handling string ID references."""

    args_without_str_none = tuple(
        arg for arg in args if arg is not str and arg is not type(None)
    )
    has_none = any(arg is type(None) for arg in args)
    has_str = any(arg is str for arg in args)

    # First see if this is a DSL-only union type
    # If so, just return the corresponding semantic type
    if args_without_str_none in DSL_ONLY_UNION_TYPES:
        if has_none:
            # If we have a DSL type and None, we return the DSL type with None
            return DSL_ONLY_UNION_TYPES[args_without_str_none] + " | None"
        else:
            # Note we don't handle the case where we have a DSL type and str,
            # because that would indicate a reference to an ID, which we handle separately.
            return DSL_ONLY_UNION_TYPES[args_without_str_none]

    # Handle the case where we have a list | None, which in the dsl is needed, but here we will just have an empty list.
    if len(args) == 2:
        list_elems = [
            arg for arg in args if get_origin(arg) in set([list, dict])
        ]
        if len(list_elems) > 0 and has_none:
            # If we have a list and None, we return the list type
            # This is to handle cases like List[SomeType] | None
            # which in the DSL is needed, but here we will just have an empty list.
            return dsl_to_semantic_type_name(list_elems[0])

    # If the union contains a DSL type and a str, we need to drop the str
    if any(_is_dsl_type(arg) for arg in args) and has_str:
        # There is a DSL type and a str, which indicates something that can reference an ID.
        # drop the str
        args = tuple(arg for arg in args if arg is not str)

    return " | ".join(dsl_to_semantic_type_name(a) for a in args)


def dsl_to_semantic_type_name(field_type: Any) -> str:
    """Transform a DSL field type to a semantic field type."""

    # Handle ForwardRef objects
    if hasattr(field_type, "__forward_arg__"):
        # Extract the string from ForwardRef and process it
        forward_ref_str = field_type.__forward_arg__
        actual_type = eval(forward_ref_str, dict(vars(dsl)))
        return dsl_to_semantic_type_name(actual_type)

    # Handle Union types (including | syntax)
    origin = get_origin(field_type)
    args = get_args(field_type)

    if origin is Union or (
        hasattr(field_type, "__class__")
        and field_type.__class__.__name__ == "UnionType"
    ):
        return _transform_union_type(args)

    # Handle Literal types
    if origin is Literal:
        # Format literal values
        literal_values = []
        for arg in args:
            if isinstance(arg, str):
                literal_values.append(f'"{arg}"')
            else:
                literal_values.append(str(arg))
        return f"Literal[{', '.join(literal_values)}]"

    # Handle list types
    if origin is list:
        if args:
            inner_type = dsl_to_semantic_type_name(args[0])
            return f"list[{inner_type}]"
        return "list"

    # Handle dict types
    if origin is dict:
        if len(args) == 2:
            key_type = dsl_to_semantic_type_name(args[0])
            value_type = dsl_to_semantic_type_name(args[1])
            return f"dict[{key_type}, {value_type}]"
        return "dict"

    # Handle basic types
    if hasattr(field_type, "__name__"):
        type_name = field_type.__name__
        if _is_dsl_type(field_type) and type_name not in TYPES_TO_IGNORE:
            return str(type_name)
        if type_name == "NoneType":
            return "None"
        return str(type_name)

    return str(field_type)


def generate_semantic_class(class_name: str, cls: type) -> str:
    """Generate a semantic class from a DSL class."""
    semantic_name = f"{class_name}"

    # Get class docstring
    docstring = cls.__doc__ or f"Semantic version of {class_name}."

    # Determine inheritance
    if class_name in FROZEN_TYPES:
        # If this is a frozen type, we use ImmutableModel instead of BaseModel
        inheritance = "ImmutableModel"
    else:
        inheritance = "BaseModel"
    if inspect.isabstract(cls):
        inheritance += ", ABC"

    # Check if this class inherits from another DSL class
    for base in cls.__bases__:
        if (
            hasattr(base, "__module__")
            and base.__module__ == dsl.__name__
            and base.__name__ not in TYPES_TO_IGNORE
            and not base.__name__.startswith("_")
        ):
            # This class inherits from another DSL class
            semantic_base = f"{base.__name__}"
            if inspect.isabstract(cls):
                inheritance = f"ABC, {semantic_base}"
            else:
                inheritance = semantic_base
            if semantic_name == "Tool":
                # Tools should inherit from Step and be immutable
                inheritance = f"{semantic_base}, ImmutableModel"
            break

    # Get field information from the class - only fields defined on this class, not inherited
    fields = []
    if hasattr(cls, "__annotations__") and hasattr(cls, "model_fields"):
        # Only process fields that are actually defined on this class
        for field_name in cls.__annotations__:
            if (
                field_name in cls.model_fields
                and f"{class_name}.{field_name}" not in FIELDS_TO_IGNORE
            ):
                field_info = cls.model_fields[field_name]
                field_type = field_info.annotation
                field_default = field_info.default
                field_description = getattr(field_info, "description", None)

                # Transform the field type
                semantic_type = dsl_to_semantic_type_name(field_type)

                # Check if we should change the default of `None` to `[]` if the type is a list
                if field_default is None and semantic_type.startswith("list["):
                    field_default = []

                # Check if we should change the default of `None` to `{}` if the type is a dict
                if field_default is None and semantic_type.startswith("dict["):
                    field_default = {}

                # Create field definition
                field_def = create_field_definition(
                    field_name, semantic_type, field_default, field_description
                )
                fields.append(field_def)

    # Build class definition
    lines = [f"class {semantic_name}({inheritance}):"]
    lines.append(f'    """{docstring}"""')
    lines.append("")

    # Add fields
    if fields:
        lines.extend(fields)
    else:
        lines.append("    pass")

    return "\n".join(lines)


def create_field_definition(
    field_name: str,
    field_type: str,
    field_default: Any,
    field_description: str | None,
) -> str:
    """Create a field definition string."""
    # Handle aliases
    alias_part = ""
    if field_name == "else_":
        alias_part = ', alias="else"'

    # Handle default values
    # Check for PydanticUndefined (required field)
    from enum import Enum

    from pydantic_core import PydanticUndefined

    if field_default is PydanticUndefined or field_default is ...:
        default_part = "..."
    elif field_default is None:
        default_part = "None"
    elif isinstance(field_default, Enum):
        # Handle enum values (like DecoderFormat.json) - check this before str since some enums inherit from str
        enum_class_name = field_default.__class__.__name__
        enum_value_name = field_default.name
        default_part = f"{enum_class_name}.{enum_value_name}"
    elif isinstance(field_default, str):
        default_part = f'"{field_default}"'
    elif hasattr(
        field_default, "__name__"
    ):  # Callable or other objects with names
        # Handle other defaults with names
        if hasattr(field_default, "__module__") and hasattr(
            field_default, "__qualname__"
        ):
            default_part = f"{field_default.__qualname__}"
        else:
            default_part = str(field_default)
    else:
        default_part = str(field_default)

    # Create Field definition
    field_parts = [default_part]
    if field_description:
        # Escape quotes and handle multiline descriptions
        escaped_desc = field_description.replace('"', '\\"').replace(
            "\n", "\\n"
        )
        field_parts.append(f'description="{escaped_desc}"')
    if alias_part:
        field_parts.append(alias_part.lstrip(", "))

    field_def = f"Field({', '.join(field_parts)})"

    return f"    {field_name}: {field_type} = {field_def}"
