# Learning Changelog

STEP 1  ██████████  Baseline architecture
STEP 2  ██████████  LLM
STEP 3  ██████████  Conversation
STEP 4  ░░░░░░░░░░  One tool
STEP 5  ░░░░░░░░░░  Tool execution
STEP 6  ░░░░░░░░░░  Agent loop
STEP 7  ░░░░░░░░░░  Multiple tools
STEP 8  ░░░░░░░░░░  Session
STEP 9  ░░░░░░░░░░  SQLite memory
STEP 10 ░░░░░░░░░░  Retrieval gate
STEP 11 ░░░░░░░░░░  Real Waku-like tools
STEP 12 ░░░░░░░░░░  Gateway
STEP 13 ░░░░░░░░░░  Tracing
STEP 14 ░░░░░░░░░░  Evals

## Step 3 Converstaion history 

user → LLM → answer

### Added
- Working memory simple messages list 
- System prompt

## Step 1 & 2 make the LLM runnable

### Baseline 

- Config env LLM model and api_key
- The smallest possible LLM wrapper
- Runable CLI

### Learned

Three files to talk to LLM:

1. Config file to setup LLM env
2. LLM file to ask LLM question passing in user query directly
3. Main file to let the dialog with LLM running infinitely.  

### Baseline Architecture

my-mini-agent/
├── pyproject.toml
├── .env
└── waku/
    ├── __init__.py
    ├── config.py
    ├── llm.py
    └── main.py

### To run it
uv venv
uv pip install -e .
uv run mini-agent