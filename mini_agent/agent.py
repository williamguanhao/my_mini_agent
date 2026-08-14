import json
from .llm import ask
from .registry import ToolRegistry
SYSTEM = """
    You are mini_agent, a helpful personal assistant.

    Be concise.
    Be honest.
    Do not claim to have performed actions you did not perform.
    When you are unsure about something, say "I don't know" or "I'm not sure".
"""
class Agent:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry
    def run(self, user_input:str) -> str:
        messages = []
        messages.append({"role": "system", "content": SYSTEM})
        messages.append({"role": "user", "content": user_input})

        while True:

            response = ask(
                messages,
                self.registry.schemas()
            )
            message = response.choices[0].message
            messages.append(message.model_dump(exclude_none=True))

            if not message.tool_calls:
                return message.content

            for tool_call in message.tool_calls:
                tool_response = self.execute_tool(tool_call)
                print(f"mini_agent > {tool_call.function.name}({tool_call.function.arguments}) = {tool_response}")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call.function.name,
                    "content": str(tool_response)
                })

    def execute_tool(self, tool_call):
        name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
            )
        tool = self.registry.get(name)

        try:
            return tool.function(**arguments)
        except Exception as e:
            return f"Error executing tool {name}: {str(e)}"
