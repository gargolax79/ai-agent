# AI Coding Agent

An autonomous AI coding assistant built in Python that uses an OpenAI-compatible tool-calling loop (via OpenRouter) to inspect files, run code, and fix bugs inside a sandboxed working directory.

## Features

- **Iterative Agent Loop**: Runs up to `MAX_ITERS` (20) turns, maintaining conversation history and tool execution results until the task is complete.
- **Built-in Tools**:
  - `get_files_info`: List files and directories with sizes.
  - `get_file_content`: Read file contents (truncated safely at `MAX_CHARS`).
  - `run_python_file`: Execute Python scripts with optional CLI arguments and capture `STDOUT`/`STDERR`.
  - `write_file`: Create or overwrite files within the working directory.
- **Path Security**: Restricts all file and execution operations to the configured `WORKING_DIR` (`./calculator`).

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- An [OpenRouter](https://openrouter.ai/) API key

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd ai-agent
   ```

2. Create a `.env` file from `.env.example` and set your API key:
   ```bash
   cp .env.example .env
   ```

3. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

## Usage

Run the agent with a prompt:

```bash
uv run main.py "how does the calculator render results to the console?"
```

Enable verbose mode to inspect token usage, function arguments, and tool outputs:

```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20." --verbose
```

