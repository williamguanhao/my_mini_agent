from .case import EvalCase

CASES = [

    EvalCase(
        name="calculator_basic",
        user_input="What is 123 * 456?",
        expected_answer="56088",
        expected_tools=["calculator"],
    ),

    EvalCase(
        name="save_note",
        user_input="Save a note saying my favorite model is SABR.",
        expected_tools=["save_note"],
    ),

    EvalCase(
        name="no_tool",
        user_input="What is the Black-Scholes model?",
        expected_tools=[],
    ),
]