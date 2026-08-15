import json
from .llm import LLM
from .registry import ToolRegistry
from .session import Session
from .runtime import Runtime
SYSTEM = """
    You are mini_agent, a helpful personal assistant.

    Be concise.
    Be honest.
    Do not claim to have performed actions you did not perform.
    When you are unsure about something, say "I don't know" or "I'm not sure".
"""
class Agent:

    def __init__(
            self, 
            llm: LLM,
            registry: ToolRegistry,
            session:Session,
            runtime:Runtime,
            system_prompt:str=SYSTEM
    ):
        self.llm = llm
        self.registry = registry
        self.session = session
        self.runtime = runtime
        self.system_prompt = system_prompt

    def run(self, user_input:str) -> str:
        self.session.add_system_message(self.system_prompt)
        self.session.add_user_message(user_input)
        
        while True:

            messages = [
                *self.session.get_messages()
            ]
            print("Messages sent to LLM:")
            for msg in messages:
                print(msg)
            response = self.llm.ask(
                messages,
                self.registry.schemas()
            )
            message = response.choices[0].message
            self.session.add_assistant_message(message)

            if not message.tool_calls:
                return message.content

            for tool_call in message.tool_calls:
                tool_response = self.runtime.execute(tool_call)
                print(f"mini_agent > {tool_call.function.name}({tool_call.function.arguments}) = {tool_response}")
                print(f"Tool call ID: {tool_call.id}")
                self.session.add_tool_message(
                    tool_call_id = tool_call.id,
                    tool_name = tool_call.function.name,
                    content = tool_response
                )
