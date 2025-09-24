# -*- coding: utf-8 -*-
# mcp_wrapper.py
from typing import Any, Callable, Generic, Optional, Type, TypeVar

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from pydantic_core import PydanticUndefined

T = TypeVar("T", bound=BaseModel)
U = TypeVar("U", bound=BaseModel)


class MCPWrapper(Generic[T, U]):
    """A wrapper class for integrating zh with MCP (Model Context
         Protocol) servers.

    This class provides functionality to wrap component classes and expose
    them as MCP tools with proper type annotations and parameter handling.

    Attributes:
        mcp (FastMCP): The MCP server instance.
        component_class (Type): The component class to wrap.
    """

    def __init__(self, mcp: FastMCP, component_class: Type):
        """Initialize the MCP wrapper.

        Args:
            mcp (FastMCP): The FastMCP server instance to register tools with.
            component_class (Type): The component class to wrap as an MCP tool.
        """
        self.mcp = mcp
        self.component_class = component_class

    def wrap(
        self,
        name: str,
        description: str,
        method_name: str = "arun",
    ) -> Callable[..., Any]:
        """Wrap a component as an MCP tool.

        This method creates a component instance and wraps it as an MCP tool
        with proper parameter handling and type annotations derived from the
        component's input model.

        Args:
            name (str): The name for the component instance.
            description (str): The description for the component instance.
            method_name (str, optional): The method name to call on the
                 component.  Defaults to "arun".

        Returns:
            Callable[..., Any]: The wrapped tool function that can be called
               by MCP.
        """
        component = self.component_class(name=name, description=description)

        def create_decorated_async_function(
            params: list[str],
            func_name: str = "wrapped_tool",
            decorator: Optional[Callable] = None,
        ) -> Callable[..., Any]:
            """Create a dynamically generated async function with proper
            type annotations.

            This internal function generates Python code for an async
            function that matches the component's input schema,
            then executes it to create the actual function.

            Args:
                params (list[str]): List of parameter names from the
                    component's input model.
                func_name (str, optional): Name for the generated function.
                    Defaults to "wrapped_tool".
                decorator (Optional[Callable], optional): Decorator to apply
                    to the generated function. Defaults to None.

            Returns:
                Callable[..., Any]: The dynamically created async function.
            """
            # Generate parameter list with type annotations
            params_types_with_default = []
            params_types_without_default = []

            for param in params:
                # Get field information from Pydantic model
                field_info = component.input_type.model_fields[param]
                # Extract type annotation
                param_type = field_info.annotation
                # Convert type to string representation
                if hasattr(param_type, "__name__"):
                    type_str = param_type.__name__
                    if type_str == "Optional":
                        type_str = ""
                else:
                    type_str = str(param_type)

                # Check for default value
                if not field_info.is_required():
                    # All non-required fields get None as default
                    default_repr = (
                        repr(field_info.default)
                        if field_info.default is not PydanticUndefined
                        else "None"
                    )
                    if type_str == "":
                        param_line = f"{param} = {default_repr}"
                    else:
                        param_line = f"{param}: {type_str} = {default_repr}"
                    params_types_with_default.append(param_line)
                else:
                    if type_str == "":
                        param_line = f"{param}"
                    else:
                        param_line = f"{param}: {type_str}"
                    params_types_without_default.append(param_line)

            args_str_with_default = ", ".join(params_types_with_default)
            args_str_without_default = ", ".join(params_types_without_default)

            args_str = args_str_without_default
            if len(args_str_with_default) > 0:
                args_str += f", {args_str_with_default}"
            # dynamic generate functions
            code = f"""
async def {func_name}({args_str}):
    # Build kwargs dict dynamically,
    # only including non-None values for optional params
    kwargs_dict = {{}}
    locals_dict = locals()
    field_infos = component.input_type.model_fields

    for param_name in {params}:
        param_value = locals_dict[param_name]
        field_info = field_infos[param_name]

        # Include required fields always, optional fields only if not None
        if field_info.is_required():
            kwargs_dict[param_name] = param_value
        elif param_value is not None:
            kwargs_dict[param_name] = param_value
        # Skip optional fields with None values - let Pydantic use defaults

    input_model = component.input_type(**kwargs_dict)
    method = getattr(component, method_name)
    result = await method(input_model)
    import json
    return json.dumps(result.model_dump(), ensure_ascii=False)
"""

            # make namespace for component
            namespace = {
                "component": component,
                "method_name": method_name,
                "Context": __import__(
                    "mcp.server.fastmcp",
                    fromlist=["Context"],
                ).Context,
                "PydanticUndefined": PydanticUndefined,
            }

            # generate code generations
            exec(code, namespace)

            raw_function = namespace[func_name]

            # apply decorator
            if decorator:
                return decorator(raw_function)
            return raw_function

        # define the mcp tool decorator
        tool_decorator = self.mcp.tool(
            name=component.name,
            description=component.description,
        )

        # wrap the tool with mcp decorator with respect of the component
        # input type

        wrapped_tool = create_decorated_async_function(
            params=list(component.input_type.model_fields.keys()),
            decorator=tool_decorator,
        )

        self.mcp._tool_manager._tools[component.name].parameters.update(
            component.function_schema.parameters.model_dump(),
        )
        return wrapped_tool
