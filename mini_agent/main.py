from .tools import TOOLS
from .agent import Agent
from .registry import ToolRegistry


def main():

    registry = ToolRegistry(TOOLS)
    agent = Agent(registry)
    while True:
        user_input = input("you > ")

        if user_input in {"quit", "exit"}:
            break

        answer = agent.run(user_input)

        print(f"mini_agent > {answer}")


if __name__ == "__main__":
    main()