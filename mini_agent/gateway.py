import time
class Gateway:

    def __init__(self, llm, tracer=None):
        self.llm = llm
        self.tracer = tracer

    def chat(self, messages, tools = None):

        if self.tracer:
            self.tracer.log(
                    "LLM_REQUEST",
                {
                    "model": self.llm.model,
                    "message_count": len(messages),
                    "tool_count": len(tools or []),
                },
            )
        start = time.perf_counter()

        response = self.llm.ask(
            messages=messages,
            tools=tools
        )

        duration = time.perf_counter() - start

        if self.tracer:
            self.tracer.log(
                    "LLM_RESPONSE",
                {
                    "duration_ms": round(duration * 1000, 2),
                    "content": response.content,
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "name": tc.name,
                            "arguments": tc.arguments,
                        }
                        for tc in response.tool_calls
                    ],
                },
            )
        return response