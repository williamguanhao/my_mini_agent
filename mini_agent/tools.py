from datetime import datetime
from .tool import Tool
from .registry import ToolRegistry

def get_time() -> str:
    return datetime.now().astimezone().isoformat()

def add(a: float, b: float) -> float:
    return a + b

def substract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

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
subtract_tool = Tool(
    name="subtract",
    description="Subtract two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {
                "type": "number",
                "description": "The number to subtract from.",
            },
            "b": {
                "type": "number",
                "description": "The number to subtract.",
            },
        },
        "required": ["a", "b"],
    },
    function=substract
)

multiply_tool = Tool(
    name="multiply",
    description="Multiply two numbers together.",
    parameters={
        "type": "object",
        "properties": {
            "a": {
                "type": "number",
                "description": "First number.",
            },
            "b": {
                "type": "number",
                "description": "Second number.",
            },
        },
        "required": ["a", "b"],
    },
    function=multiply,
)

divide_tool = Tool(
    name="divide",
    description="Divide two numbers.",
    parameters={
        "type": "object",
        "properties": {
            "a": {
                "type": "number",
                "description": "The number to be divided (the dividend).",
            },
            "b": {
                "type": "number",
                "description": "The number to divide by (the divisor).",
            },
        },
        "required": ["a", "b"],
    },
    function=divide,
)

TOOLS = [
    get_time_tool,
    add_tool,
    subtract_tool,
    multiply_tool,
    divide_tool
]
registry = ToolRegistry(TOOLS)