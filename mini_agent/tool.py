from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Tool:
    name:str
    description:str
    parameters:dict[str, Any]
    function: Callable[..., Any]

    def schema(self) -> dict:
        return {
            "type":"function",
            "function":{
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }
    def execute(self, **kwargs) -> Any:
        return self.function(**kwargs)