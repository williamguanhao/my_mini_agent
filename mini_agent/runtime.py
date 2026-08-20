import json
import time

class Runtime:

    def __init__(self, registry, tracer=None):
        self.registry = registry
        self.tracer = tracer

    def execute(self, tool_call):
        try:
            # Handle both OpenAI format and custom ToolCall format
            if hasattr(tool_call, 'function'):
                name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
            else:
                name = tool_call.name
                arguments = json.loads(tool_call.arguments)

            tool = self.registry.get(name)

            if tool is None:
                raise ValueError(
                    f"Unknown tool: {name}"
                )
            
            self._validate_arguments(
                    tool,
                    arguments,
                )

            if self.tracer:
                self.tracer.log(
                    "TOOL_START",
                    {
                        "tool": tool_call.name,
                        "tool_call_id": tool_call.id,
                        "arguments": tool_call.arguments,
                    },
                )

            start = time.perf_counter() 

            result = tool.execute(arguments)

            duration = time.perf_counter() - start

            if self.tracer:
                self.tracer.log(
                    "TOOL_END",
                    {
                        "duration_ms": round(duration * 1000, 2),
                        "tool": tool_call.name,
                        "success": True,
                        "content": str(result),
                    },
                )

            return {
                "success": True,
                "content": str(result)
            }

        except Exception as e:

            if self.tracer:
                self.tracer.log(
                    "TOOL_END",
                    {
                        "duration_ms": round(duration * 1000, 2),
                        "tool": tool_call.name,
                        "success": False,
                        "content": f"Tool error: {str(e)}",
                    },
                )

            return {
                "success": False,
                "content":  f"Tool error: {str(e)}"
            }


    def _validate_arguments(self, tool, arguments):

        schema = tool.parameters

        required = schema.get(
            "required",
            []
        )

        properties = schema.get(
            "properties",
            {}
        )

        # Required fields
        for field in required:

            if field not in arguments:
                raise ValueError(
                    f"Missing required argument "
                    f"'{field}' for tool '{tool.name}'"
                )

        # Type checking
        for field, value in arguments.items():

            if field not in properties:
                raise ValueError(
                    f"Unexpected argument "
                    f"'{field}' for tool '{tool.name}'"
                )

            expected_type = properties[field].get(
                "type"
            )

            if expected_type == "string":
                if not isinstance(value, str):
                    raise ValueError(
                        f"Argument '{field}' must be a string"
                    )

            elif expected_type == "number":
                if not isinstance(value, (int, float)):
                    raise ValueError(
                        f"Argument '{field}' must be a number"
                    )

            elif expected_type == "integer":
                if not isinstance(value, int):
                    raise ValueError(
                        f"Argument '{field}' must be an integer"
                    )

            elif expected_type == "boolean":
                if not isinstance(value, bool):
                    raise ValueError(
                        f"Argument '{field}' must be a boolean"
                    )
