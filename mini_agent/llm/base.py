from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class BaseLLM(ABC):

    @abstractmethod
    def ask(self, messages, tools=None):
        pass

@dataclass
class ToolCall:
    id: str
    name: str
    arguments: str


@dataclass
class LLMResponse:
    content: Optional[str]
    tool_calls: list[ToolCall]