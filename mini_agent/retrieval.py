import re


STOP_WORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "do",
    "i",
    "my",
    "you",
    "we",
    "are",
    "was",
    "were",
    "to",
    "of",
    "and",
    "in",
    "on",
    "for",
}


def keywords(text):
    words = re.findall(
        r"\b[a-zA-Z0-9_]+\b",
        text.lower(),
    )

    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]

def clean_message(message):

    return {
        key: value
        for key, value in message.items()
        if key != "_id"
    }
class Retriever:

    def __init__(
            self, 
            memory,
            recent_limit=20,
            relevent_limit=10
    ):
        self.memory = memory
        self.recent_limit = recent_limit
        self.relevent_limit = relevent_limit

    def retrieve(self, 
                 session,
                 query,
    ):
        recent = self.memory.get_recent_messages(
            session_id = session.session_id,
            limit = self.recent_limit
        )

        relevant = []
        for keyword in keywords(query):
            matches = self.memory.search_messages(
                session_id = session.session_id,
                query=keyword,
                limit=self.relevent_limit
            )
            # Filter out tool results - they need their tool_calls to be valid
            # Also filter out assistant messages with tool_calls (will be in recent)
            relevant.extend([
                m for m in matches
                if m.get("role") in ("user", "assistant")
                and not m.get("tool_calls")
            ])
        return [
            clean_message(message)
            for message in self._merge(
                recent,
                relevant
            )
        ]

    def _merge(self, recent, relevant):
        # Recent messages should take priority and maintain order
        # Relevant messages from search should only add context, not reorder
        messages = recent.copy()

        # Add relevant messages that are not already in recent
        recent_ids = {msg["_id"] for msg in recent}
        for msg in relevant:
            if msg["_id"] not in recent_ids:
                messages.append(msg)

        return messages