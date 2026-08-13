from .llm import ask
SYSTEM = """
    You are mini_agent, a helpful personal assistant.

    Be concise.
    Be honest.
    Do not claim to have performed actions you did not perform.
    When you are unsure about something, say "I don't know" or "I'm not sure".
"""

def main():
    print("Mini-agent v0.1")
    messages = []
    messages.append({"role": "system", "content": SYSTEM})
    while True:
        try:
            user_input = input("you > ")
            messages.append({"role": "user", "content": user_input})
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if user_input.strip() in {"quit", "exit"}:
            break

        answer = ask(messages, [])  # Assuming no tools are used
        messages.append({"role": "assistant", "content": answer})
        print(f"MINI > {answer}")


if __name__ == "__main__":
    main()