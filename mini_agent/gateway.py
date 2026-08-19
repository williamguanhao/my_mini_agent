class Gateway:

    def __init__(self, llm):
        self.llm = llm

    def chat(self, messages, tools = None):
        return self.llm.ask(
            messages=messages,
            tools=tools
        )