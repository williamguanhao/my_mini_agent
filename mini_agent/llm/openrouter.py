from openai import OpenAI

from .base import BaseLLM, LLMResponse, ToolCall


class OpenRouterLLM(BaseLLM):

    def __init__(
        self,
        api_key: str,
        model: str,
    ):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
        )

        self.model = model

    def ask(
        self,
        messages,
        tools=None,
    ) -> LLMResponse:

        kwargs = {
            "model": self.model,
            "messages": messages,
        }

        if tools:
            kwargs["tools"] = tools

        response = self.client.chat.completions.create(
            **kwargs
        )

        message = response.choices[0].message

        tool_calls = []

        if message.tool_calls:

            for call in message.tool_calls:

                tool_calls.append(
                    ToolCall(
                        id=call.id,
                        name=call.function.name,
                        arguments=call.function.arguments,
                    )
                )

        return LLMResponse(
            content=message.content,
            tool_calls=tool_calls,
        )