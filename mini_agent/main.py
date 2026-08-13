from .llm import ask
from .tools import TOOL_REGISTRY
import json
SYSTEM = """
    You are mini_agent, a helpful personal assistant.

    Be concise.
    Be honest.
    Do not claim to have performed actions you did not perform.
    When you are unsure about something, say "I don't know" or "I'm not sure".
"""
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get the current local time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
        {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression such as 12 * 5",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]

def execute_tool(tool_call):
    name = tool_call.function.name

    tool_called = TOOL_REGISTRY.get(name)
    if tool_called is None:
        return f"Unknown tool: {name}"
    try:
        arguments = json.loads(
            tool_call.function.arguments
            )
        return tool_called(**arguments)
    except json.JSONDecodeError:
        return f"Invalid arguments for tool {name}"

def run_agent(user_input: str):
    messages = []
    messages.append({"role": "system", "content": SYSTEM})
    messages.append({"role": "user", "content": user_input})

    while True:
        response = ask(messages, TOOLS)

        message = response.choices[0].message

        # Keep the assistant's response in the conversation.
        messages.append(
            message.model_dump(exclude_none=True)
        )

        # No tool call means we're finished.
        if not message.tool_calls:
            return message.content

        # Execute every requested tool.
        for tool_call in message.tool_calls:
            result = execute_tool(tool_call)
            print(f"Tool called {tool_call.function.name} returned: {result}")
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })


def main():
    while True:
        user_input = input("you > ")

        if user_input in {"quit", "exit"}:
            break

        answer = run_agent(user_input)

        print(f"mini_agent > {answer}")


if __name__ == "__main__":
    main()