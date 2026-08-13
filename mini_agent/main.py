from .llm import ask


def main():
    print("Mini-agent v0.1")
    messages = []
    
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