# Learning Changelog

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

my-waku/
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