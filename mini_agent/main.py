from .llm import ask
from .tools import TOOL_REGISTRY
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
    }
]

def execute_tool(tool_call):
    name = tool_call.function.name

    tool = TOOL_REGISTRY[name]

    return tool()

def main():
    print("Mini-agent v0.1")
    messages = []
    messages.append({"role": "system", "content": SYSTEM})
    while True:
        try:
            user_input = input("you > ")
            messages.append({"role": "user", "content": user_input})
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if user_input.strip() in {"quit", "exit"}:
            break

        answer = ask(messages, TOOLS).choices[0].message  # Assuming no tools are used
        messages.append({"role": "assistant", "content": answer.content})
        print(f"MINI > {answer.content}")
        print("TOOLS CALLS:", [execute_tool(tool_call) for tool_call in answer.tool_calls])


if __name__ == "__main__":
    main()