from datetime import datetime

def get_time() -> str:
    return datetime.now().astimezone().isoformat()

def calculate(expression: str) -> str:
    # Temporary simple implementation.
    # We'll make this safer later.
    result = eval(expression)
    return str(result)

TOOL_REGISTRY = {
    "get_time": get_time,
    "calculate": calculate,
}