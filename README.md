# Agent Code

Small Python CLI that sends a single prompt to Google Gemini (`gemini-2.5-flash`) and prints the model response.

## Requirements

- Python 3.11+
- A Google Gemini API key
- [uv](https://docs.astral.sh/uv/) (recommended)

## Setup

Recommended with uv:

1. Create a project environment and install dependencies from `pyproject.toml`.

```powershell
uv sync
```

2. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Optional: pip + venv setup (if you do not want uv)

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -e .
```

3. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run with a single prompt argument:

```powershell
uv run python main.py "Explain recursion in one paragraph"
```

Run with verbose token output:

```powershell
uv run python main.py "Explain recursion in one paragraph" --verbose
```

If you used pip + venv, you can run with `python main.py ...` instead.

## CLI Behavior

- If no prompt is provided, the script prints `PLS GIVE ME PROMPT` and exits with status code `1`.
- If `--verbose` is provided as the second argument, it prints:
	- the prompt text
	- prompt token count
	- response token count

## Notes

- The script currently sends exactly one user message and prints only `response.text`.
- The model is hardcoded to `gemini-2.5-flash` in `main.py`.

## Troubleshooting

- If you see authentication errors, verify `GEMINI_API_KEY` is set correctly.
- If imports fail, make sure your virtual environment is activated and dependencies are installed.
