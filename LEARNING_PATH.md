# mini_agent — Learning Path

This project recreates an agent architecture from the core upward.

The goal is not just to make an agent work, but to understand
what each layer is doing.

---

## Step 1 — Core

Goal:
Create the smallest runnable Python project.

Architecture:

    CLI
     ↓
    main()

Important concepts:
- pyproject.toml
- Python package
- project entry point
- uv venv
- uv pip install -e . 
- uv run

---

## Step 2 — LLM

Goal:
Make MiniMax callable through the OpenAI SDK.

Architecture:

    Agent code
        ↓
    OpenAI SDK
        ↓
    MiniMax API

Important concepts:
- OpenAI-compatible API
- client
- messages
- response.choices[0].message.content

---

## Step 3 — Conversation

Goal:
Pass message history to the LLM.

Architecture:

    messages
       ↓
    MiniMax
       ↓
    response

Important concepts:
- role
- user
- assistant
- conversation history

---

## Step 4 — One Tool

Goal:
Teach MiniMax that Python functions are available.

Architecture:

    MiniMax
       ↓
    tool call
       ↓
    Python function

First tool:
- get_time

Important concepts:
- tool schema
- function tool
- tool_calls

---

## Step 5 — Agent Loop

Goal:
Execute a tool and send its result back to MiniMax.

Architecture:

    User
      ↓
    LLM
      ↓
    tool call
      ↓
    Python
      ↓
    tool result
      ↓
    LLM
      ↓
    answer

Important concepts:
- tool_call
- tool result
- role=tool
- iterative LLM calls

---

## Step 6 — Tool Arguments

Goal:
Allow tools to receive arguments from the LLM.

Architecture:

    tool_call
       ↓
    name + JSON arguments
       ↓
    json.loads()
       ↓
    Python kwargs
       ↓
    function(**arguments)

Important concepts:
- function.arguments
- JSON
- **kwargs

---

## Step 7 — Tool Abstraction

Goal:
Stop scattering tool information throughout the program.

Architecture:

    Tool
    ├── name
    ├── description
    ├── parameters
    └── function

Then:

    ToolRegistry
         ↓
       Tools

Important concepts:
- Tool
- ToolRegistry
- separation of concerns

---

## Step 8 — Session

Goal:
Persist conversation history across turns.

Architecture:

    Agent
      ↓
    Session
      ↓
    messages

Important concepts:
- session
- conversation state
- persistent history

---

## Future Steps

- [ ] Step 8 — Session
- [ ] Step 9 — Agent state
- [ ] Step 10 — streaming
- [ ] Step 11 — multiple tool calls
- [ ] Step 12 — tool error handling
- [ ] Step 13 — system prompts
- [ ] Step 14 — context management
- [ ] Step 15 — memory
- [ ] Step 16 — gateway/runtime separation
- [ ] Step 17 — MCP
- [ ] Step 18 — skills
- [ ] Step 19 — persistence
- [ ] Step 20 — reproduce larger Waku architecture