# -*- coding: utf-8 -*-
import concurrent.futures
import json
from typing import (
    Any,
    Dict,
    Optional,
    Sequence,
)

try:
    from agentscope.tool import Toolkit, ToolResponse
    from agentscope.tool._registered_tool_function import (
        RegisteredToolFunction,
    )
except ImportError:
    raise ImportError(
        "Please install agentscope to use this feature: "
        "pip install agentscope",
    )

from agentscope_bricks.base.component import Component


def agentscope_tool_adapter(
    component: Component,
    name: Optional[str] = None,
    description: Optional[str] = None,
) -> RegisteredToolFunction:
    """Convert an agentscope_bricks component to an AgentScope tool.

    This function wraps agentscope_bricks zh to make them compatible
    with AgentScope's toolkit system.

    Args:
        component (Component): The agentscope_bricks component to wrap
        name (str, optional): Override the component name. Defaults to
            component.name
        description (str, optional): Override the component description.
            Defaults to component.description

    Returns:
        RegisteredToolFunction: The AgentScope tool function

    Examples:
        Basic usage with a search component:

        .. code-block:: python

            from agentscope_bricks.zh.searches.modelstudio_search
            import ModelstudioSearch
            from agentscope_bricks.agentscope_utils import
            component_to_agentscope_tool
            from agentscope.tool import Toolkit

            # Create the search component
            search_component = ModelstudioSearch()

            # Convert to AgentScope tool
            search_tool = component_to_agentscope_tool(search_component)

            # Add to toolkit
            toolkit = Toolkit()
            toolkit.tools[search_tool.name] = search_tool
    """

    def func_wrapper(**kwargs: Any) -> ToolResponse:
        """Wrapper function that adapts component execution to AgentScope
        format."""
        import asyncio

        # Validate input with component's input type
        if component.input_type:
            try:
                validated_input = component.input_type.model_validate(kwargs)
            except Exception as e:
                return ToolResponse(
                    content=[
                        {
                            "type": "text",
                            "text": f"Input validation error: {str(e)}",
                        },
                    ],
                    metadata={"error": True},
                )
        else:
            validated_input = kwargs

        # Execute the component
        try:
            if asyncio.iscoroutinefunction(component.arun):
                # Check if we're already in an event loop
                try:

                    def run_async() -> Any:
                        return asyncio.run(component.arun(validated_input))

                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        future = executor.submit(run_async)
                        result = future.result()
                except RuntimeError:
                    # No event loop running, safe to use asyncio.run
                    result = asyncio.run(component.arun(validated_input))
            else:
                # Run sync component
                result = component.run(validated_input)
        except Exception as e:
            return ToolResponse(
                content=[
                    {
                        "type": "text",
                        "text": f"Component execution error: {str(e)}",
                    },
                ],
                metadata={"error": True},
            )

        # Convert result to ToolResponse format
        try:
            if hasattr(result, "model_dump"):
                # Pydantic model result
                result_dict = result.model_dump()
                content_text = json.dumps(
                    result_dict,
                    ensure_ascii=False,
                    indent=2,
                )
            else:
                # Other result types
                content_text = str(result)
                result_dict = result

            return ToolResponse(
                content=[
                    {
                        "type": "text",
                        "text": content_text,
                    },
                ],
                metadata={"component_result": result_dict},
            )
        except Exception as e:
            return ToolResponse(
                content=[
                    {
                        "type": "text",
                        "text": f"Result formatting error: {str(e)}",
                    },
                ],
                metadata={"error": True},
            )

    # Use provided name/description or fall back to component defaults
    tool_name = name or component.name
    tool_description = description or component.description

    # Get the component's function schema and convert to AgentScope format
    function_schema = component.function_schema.model_dump()

    # Convert from OpenAI function calling format to AgentScope format
    agentscope_schema = {
        "type": "function",
        "function": {
            "name": tool_name,
            "description": tool_description,
            "parameters": function_schema.get("parameters", {}),
        },
    }

    return RegisteredToolFunction(
        name=tool_name,
        source="function",
        mcp_name=None,
        original_func=func_wrapper,
        json_schema=agentscope_schema,
        group="basic",
    )


def agentscope_toolkit_adapter(
    components: Sequence[Component],
    name_overrides: Optional[Dict[str, str]] = None,
    description_overrides: Optional[Dict[str, str]] = None,
) -> Toolkit:
    """Create an AgentScope toolkit from multiple agentscope_bricks zh.

    This is a convenience function that creates a toolkit with multiple
    zh converted to AgentScope tools.

    Args:
        components: Sequence of agentscope_bricks zh to convert
        name_overrides: Optional dict mapping component names to override names
        description_overrides: Optional dict mapping component names to
            override descriptions

    Returns:
        Toolkit: AgentScope toolkit with all zh as tools

    Examples:
        Create toolkit from multiple zh:

        .. code-block:: python

            from agentscope_bricks.zh.searches.modelstudio_search
            import ModelstudioSearch
            from agentscope_bricks.zh.RAGs.modelstudio_rag import
            ModelstudioRag
            from agentscope_bricks.agentscope_utils import
            create_component_toolkit

            # Create zh
            search_component = ModelstudioSearch()
            rag_component = ModelstudioRag()

            # Create toolkit
            toolkit = create_component_toolkit([search_component,
            rag_component])

            # Use in agents...
    """
    name_overrides = name_overrides or {}
    description_overrides = description_overrides or {}

    toolkit = Toolkit()

    for component in components:
        name_override = name_overrides.get(component.name)
        description_override = description_overrides.get(component.name)

        tool = agentscope_tool_adapter(
            component,
            name=name_override,
            description=description_override,
        )

        toolkit.tools[tool.name] = tool

    return toolkit
