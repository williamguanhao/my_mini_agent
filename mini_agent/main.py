from .tools.time import GetTimeTool
from .agent import Agent
from .registry import ToolRegistry
from .llm import LLM
from .session import Session
from .runtime import Runtime
from .memory import SQLiteMemory
from .config import API_KEY, MODEL, BASE_URL
from .retrieval import Retriever
SYSTEM = """
    You are mini_agent, a helpful personal assistant.

    Be concise.
    Be honest.
    Do not claim to have performed actions you did not perform.
    When you are unsure about something, say "I don't know" or "I'm not sure".
"""

def main():

    memory = SQLiteMemory()

    session = Session(session_id="demo_session", memory=memory)

    llm = LLM(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL)

    registry = ToolRegistry()

    registry.register(
        GetTimeTool()
    )

    runtime = Runtime(registry)

    retriever = Retriever(memory=memory, recent_limit=20, relevent_limit=10)

    agent = Agent(
        llm=llm, 
        registry=registry,
        session=session,
        runtime=runtime,
        retriever=retriever,
        system_prompt=SYSTEM
    )

    # -------------------------
    # Chat loop
    # -------------------------
    
    while True:
        user_input = input("you > ")

        if user_input in {"quit", "exit"}:
            break

        answer = agent.run(user_input)

        print(f"mini_agent > {answer}")


if __name__ == "__main__":
    main()