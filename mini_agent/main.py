from .llm import ask


def main():
    print("Mini-agent v0.1")

    while True:
        try:
            user_input = input("you > ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if user_input.strip() in {"quit", "exit"}:
            break

        answer = ask(user_input)

        print(f"MINI > {answer}")


if __name__ == "__main__":
    main()