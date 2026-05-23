# RAG Sample Project

A minimal Retrieval-Augmented Generation (RAG) demo using a local Chroma vector store.

## Project structure

- `SampleRAG.py` — Example script that demonstrates retrieval + generation.
- `Requirements.txt` — Python dependencies.
- `chroma_db/` — Local Chroma database folder (includes `chroma.sqlite3`).
- `cloud.txt` — Optional cloud / API configuration used by the sample.

## Requirements

- Python 3.9+ (recommended)
- Install dependencies from `Requirements.txt`

## Setup

1. Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Or on bash / WSL:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r Requirements.txt
```

3. (Optional) Review or add cloud/API settings in `cloud.txt` before running the sample.

## Running the sample

The project includes a ready-made Chroma DB under `chroma_db/`.

To run the example:

```bash
python SampleRAG.py
```

If the script expects API keys or cloud settings, put them in `cloud.txt` (one-per-line or key=value pairs) or follow the prompts in `SampleRAG.py`.

## Notes

- Existing Chroma DB: `chroma_db/chroma.sqlite3` is included for convenience. If you want a fresh DB, remove or rename the `chroma_db` folder and let the script re-create it.
- If you hit missing-dependency errors, re-run `pip install -r Requirements.txt` inside the activated virtual environment.

## Files of interest

- [SampleRAG.py](SampleRAG.py) — main example
- [Requirements.txt](Requirements.txt) — dependencies
- [cloud.txt](cloud.txt) — cloud/API settings
- [chroma_db/chroma.sqlite3](chroma_db/chroma.sqlite3) — bundled DB file

## Contributing

Small fixes and improvements are welcome. Open an issue or add a PR with a short description.

---
Created for quick local experimentation with retrieval-augmented generation.
