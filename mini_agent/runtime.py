import json

class Runtime:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_call):
        name = tool_call.function.name

        try:
            arguments = json.loads(
            tool_call.function.arguments
            )
        except json.JSONDecodeError as e:
            return f"Invalid tool arguments: {str(e)}"
        try:
            tool = self.registry.get(name)
        except KeyError:
            return f"Unknown tool {name}."
        try:
            return tool.function(**arguments)
        except Exception as e:
            return f"Error executing tool {name}: {str(e)}"
