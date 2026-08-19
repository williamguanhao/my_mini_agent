import json

class Runtime:

    def __init__(self, registry):
        self.registry = registry

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

            result = tool.execute(arguments)

            return {
                "success": True,
                "content": str(result)
            }

        except Exception as e:
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
