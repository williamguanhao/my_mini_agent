from .tools import TOOLS
from .agent import Agent
from .registry import ToolRegistry
from .llm import LLM
from .session import Session
from .runtime import Runtime
from .config import API_KEY, MODEL, BASE_URL

SYSTEM = """
    You are mini_agent, a helpful personal assistant.

    Be concise.
    Be honest.
    Do not claim to have performed actions you did not perform.
    When you are unsure about something, say "I don't know" or "I'm not sure".
"""

def main():

    session = Session(session_id="default_session")

    llm = LLM(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL)

    registry = ToolRegistry(TOOLS)

    runtime = Runtime(registry)

    agent = Agent(
        llm=llm, 
        registry=registry,
        session=session,
        runtime=runtime,
        system_prompt=SYSTEM
    )

    while True:
        user_input = input("you > ")

        if user_input in {"quit", "exit"}:
            break

        answer = agent.run(user_input)

        print(f"mini_agent > {answer}")


if __name__ == "__main__":
    main()