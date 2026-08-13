from datetime import datetime

def get_time() -> str:
    return datetime.now().astimezone().isoformat()


TOOL_REGISTRY = {
    "get_time": get_time,
}