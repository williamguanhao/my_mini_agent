from openai import OpenAI
from .config import API_KEY, MODEL, BASE_URL

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
def ask(messages: list[dict], tools: list[dict]) ->str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content
