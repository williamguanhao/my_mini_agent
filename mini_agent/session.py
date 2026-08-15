class Session:
    def __init__(self, session_id=None):
        self.session_id = session_id
        self.messages = []


    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})


    def add_system_message(self, content):
        self.messages.append({"role": "system", "content": content})


    def add_tool_message(self, tool_call_id, name, content):
        self.messages.append({
            "role": "tool",
            "tool_call_id": tool_call_id,
            "name": name,
            "content": str(content)
        })

    def add_assistant_message(self, message):
        data = {
            "role": "assistant",
            "content": message.content,
        }

        if message.tool_calls:
            data["tool_calls"]= []
            for tool_call in message.tool_calls:
                data["tool_calls"].append({
                    "id": tool_call.id,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                })
        self.messages.append(data)

    def get_messages(self):
        return self.messages