class ToolRegistry:
    def __init__(self, tools=None):
        self._tools = {}

        if tools:
            for tool in tools:
                self.register(tool)

    def register(self, tool):
        self._tools[tool.name] = tool

    def get(self, name:str):
        return self._tools.get(name)
    
    def schemas(self) -> list[dict]:
        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.parameters
                },
            }
            for tool in self._tools.values()
        ]