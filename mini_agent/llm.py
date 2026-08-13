from openai import OpenAI
from .config import API_KEY, MODEL, BASE_URL

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

def ask(promt: str) ->str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": promt}],
    )
    return response.choices[0].message.content
