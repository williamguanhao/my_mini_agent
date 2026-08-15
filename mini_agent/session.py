class Session:
    def __init__(self, session_id=None, memory=None):
        self.session_id = session_id
        self.memory = memory
        self.memory.create_session(self.session_id)

    def add_user_message(self, content):
        message = {
            "role": "user", 
            "content": content
            }
        
        self.memory.add_message(
            self.session_id,
            message
        )


    def add_tool_message(self, tool_call_id, tool_name, content):

        message = {
            "role": "tool",
            "tool_call_id": tool_call_id,
            "name": tool_name,
            "content": str(content)
        }

        self.memory.add_message(
            self.session_id,
            message
        )


    def add_assistant_message(self, message):
        data = {
            "role": "assistant",
            "content": message.content,
        }

        if message.tool_calls:
            data["tool_calls"] = []
            for tool_call in message.tool_calls:
                data["tool_calls"].append({
                    "id": tool_call.id,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                })

        self.memory.add_message(
            self.session_id,
            data
        )

