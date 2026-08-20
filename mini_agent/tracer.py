import uuid
from datetime import datetime

class Tracer:
    def __init__(self):
        self.run_id = None
        self.events = []

    def start_run(self):
        self.run_id = str(uuid.uuid4())

        self.log(
            "RUN_START",
            {}
        )
        return self.run_id

    def log(self, event, data):

        self.events.append({
            "event": event,
            "data": data,
        })

        print(
            f"[{event}]"
            f"{data}"
        )

    def end_run(self):
        self.log(
            "RUN_END",
            {}
        )

    def get_events(self):

        return self.events