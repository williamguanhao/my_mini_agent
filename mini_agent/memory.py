import sqlite3
import json


class SQLiteMemory:

    def __init__(self, db_path="memory.db"):
        self.db_path = db_path
        self._initialize_db()
    def _connect(self):
        return sqlite3.connect(self.db_path)
    def _initialize_db(self):
        with self._connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id TEXT PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            conn.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT,
                    tool_call_id TEXT,
                    tool_name TEXT,
                    tool_calls TEXT,
                    FOREIGN KEY (session_id)
                        REFERENCES sessions(id)
                )
            """)
    def create_session(self, session_id):
        with self._connect() as conn:
            conn.execute("""
            INSERT OR IGNORE INTO sessions (id)
            VALUES (?)
            """,
            (session_id,),
            )
    def add_message(
            self,
            session_id,
            message
    ):
        tool_calls = message.get("tool_calls")
        if tool_calls:
            tool_calls = json.dumps(tool_calls)

        with self._connect() as conn:
            conn.execute("""
            INSERT INTO messages (
                session_id, 
                role, 
                content,
                tool_call_id,
                tool_name,
                tool_calls
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                session_id,
                message["role"],
                message["content"],
                message.get("tool_call_id"),
                message.get("tool_name"),
                tool_calls
            )
        )

    def get_messages(self, session_id):
        with self._connect() as conn:
            rows = conn.execute("""
            SELECT 
                role, 
                content,
                tool_call_id,
                tool_name,
                tool_calls
            FROM messages
            WHERE session_id = ?
            ORDER BY id ASC
            """,
            (session_id,),
            ).fetchall()

        messages = []
        for role, content, tool_call_id, tool_name, tool_calls in rows:
            message = {
                "role": role,
                "content": content
            }
            if tool_call_id:
                message["tool_call_id"] = tool_call_id
            if tool_name:
                message["tool_name"] = tool_name
            if tool_calls:
                message["tool_calls"] = json.loads(tool_calls)
            messages.append(message)

        return messages