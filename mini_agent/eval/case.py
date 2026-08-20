from dataclasses import dataclass, field


@dataclass
class EvalCase:

    name: str
    user_input: str

    expected_answer: str | None = None

    expected_tools: list[str] = field(
        default_factory=list
    )