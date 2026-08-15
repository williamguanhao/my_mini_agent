from openai import OpenAI

class LLM:
    def __init__(self, api_key:str, model:str, base_url:str):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model

    def ask(self, messages: list[dict], tools: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools,
            max_tokens=1024
        )
        return response