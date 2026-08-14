from .tool import Tool

class ToolRegistry:
    def __init__(self, tools: list[Tool]):
        self._tools = {
            tool.name: tool
            for tool in tools
        }
    def get(self, name:str) -> Tool | None:
        return self._tools.get(name)
    def schemas(self) -> list[dict]:
        return [
            tool.schema() 
            for tool in self._tools.values()
            ]