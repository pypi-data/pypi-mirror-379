import inspect
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    TypedDict,
    TypeVar,
    Union,
    get_args,
    get_origin,
)

F = TypeVar("F", bound=Callable[..., Any])


def tool() -> Callable[[F], F]:
    """
    Decorator to register a function as a tool.
    """

    def decorator(func: F) -> F:
        func._is_tool = True
        return func

    return decorator


class ToolSchema(TypedDict):
    name: str
    description: str
    inputSchema: Dict[str, Any]


def get_schema(func: Callable) -> ToolSchema:
    """
    Extract schema information from a tool function.
    """
    if not hasattr(func, "_is_tool"):
        raise ValueError(f"Function {func.__name__} is not a tool")

    doc = inspect.getdoc(func) or ""
    description_lines = []

    for line in doc.split("\n"):
        line = line.strip()
        if line.lower().startswith(
            ("args:", "returns:", "return:", "examples:", "example:")
        ):
            break
        description_lines.append(line)

    description = "\n".join(description_lines).strip()

    sig = inspect.signature(func)
    params = sig.parameters

    if not params:
        raise ValueError(
            f"Tool function {func.__name__} must have at least one parameter"
        )

    properties = {}
    required = []

    type_map = {
        str: {"type": "string"},
        int: {"type": "integer"},
        float: {"type": "number"},
        bool: {"type": "boolean"},
    }

    for param_name, param in params.items():
        param_type = param.annotation

        if param.default == inspect.Parameter.empty:
            required.append(param_name)

        origin = get_origin(param_type)
        args = get_args(param_type)

        is_optional = False

        if origin is list or origin is List:
            item_type = args[0] if args else Any
            item_schema = type_map.get(item_type, {"type": "string"})
            param_schema = {"type": "array", "items": item_schema}
        elif origin is Union:
            if type(None) in args:
                is_optional = True
                for arg in args:
                    if arg is not type(None):
                        non_none_type = arg
                        break
                else:
                    non_none_type = str
                if get_origin(non_none_type) is Literal:
                    literal_args = get_args(non_none_type)
                    param_schema = {"type": "string", "enum": list(literal_args)}
                else:
                    param_schema = type_map.get(non_none_type, {"type": "string"})
            else:
                param_schema = {"type": "string"}
        elif origin is Literal:
            literal_args = args
            param_schema = {"type": "string", "enum": list(literal_args)}
        else:
            param_schema = type_map.get(param_type, {"type": "string"})

        param_description_lines = []
        in_args_section = False
        capturing_description = False

        for line in doc.split("\n"):
            line = line.strip()
            if line.lower().startswith("args:"):
                in_args_section = True
                continue
            if (
                in_args_section
                and not capturing_description
                and line.startswith(f"{param_name}:")
            ):
                capturing_description = True
                first_line = line[len(param_name) + 1 :].strip()
                if first_line:
                    param_description_lines.append(first_line)
                continue
            if capturing_description:
                if (
                    not line
                    or line.lower().startswith(
                        ("returns:", "return:", "examples:", "example:")
                    )
                    or (
                        line
                        and not line.startswith((" ", "\t", "-"))
                        and not line.startswith(f"{param_name}:")
                    )
                ):
                    capturing_description = False
                    break
                if line:
                    param_description_lines.append(line.strip())

        param_description = (
            "\n".join(param_description_lines)
            if param_description_lines
            else f"{param_name} parameter"
        )
        param_schema["description"] = param_description
        properties[param_name] = param_schema

        if param.default != inspect.Parameter.empty or is_optional:
            if param_name in required:
                required.remove(param_name)

    schema = {
        "name": func.__name__,
        "description": description,
        "inputSchema": {
            "type": "object",
            "properties": properties,
            "required": required,
        },
    }

    return schema
