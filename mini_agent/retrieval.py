class Retriever:

    def __init__(self, limit=20):
        self.limit = limit

    def retrieve(self, session):
        messages = session.get_recent_messages(self.limit)
        return messages