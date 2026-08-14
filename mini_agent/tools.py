from datetime import datetime
from .tool import Tool
from .registry import ToolRegistry

def get_time() -> str:
    return datetime.now().astimezone().isoformat()

def add(a: float, b: float) -> float:
    return a + b

get_time_tool = Tool(
    name="get_time",
    description="Get the current local time.",
    parameters={
        "type": "object",
        "properties": {},
        "required": [],
    },
    function=get_time
)

add_tool = Tool(
    name="add",
    description="Add two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {
                "type": "number",
                "description": "The first number to add.",
            },
            "b": {
                "type": "number",
                "description": "The second number to add.",
            },
        },
        "required": ["a", "b"],
    },
    function=add
)   

TOOLS = [
    get_time_tool,
    add_tool,
]
registry = ToolRegistry(TOOLS)