# Quick Start Guide

Welcome to the Book repository quick start guide.

## Working with Nano Banana Prompts

The repository contains extensive lists of "Nano Banana" prompts which can be executed efficiently in parallel using the automation scripts in `src/`.

### Local automation setup

1. **Create or activate a Python environment**
   - Ensure Python 3.8 or higher is installed.
   - Recommended:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. **Install the shared dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional Google integrations**
   - Export `GEMINI_API_KEY`, **or** place `.GEMINI_KEY` one level above the repo root.
   - For YouTube uploads, place `client_secret.json` one level above the repo root.

### Quick single generation

Run from the repo root:

```bash
python src/nano_banana_api.py --prompt "Do unto others"
```

### Generating lists of images in parallel

You can point the automation script directly at markdown files (using the `::` delimiter) or the YAML configuration template in `inputs/`.

```bash
# From a double-colon delimited markdown file:
./src/nano_banana.sh --file "Nano-Banana-Prompts-CP.md" --format "delimited" --workers 10

# Using the canonical YAML file from the inputs directory:
./src/nano_banana.sh --file "inputs/nano-prompts-full.yml" --format "yaml" --section Fakhran
```

Outputs are stored in the repo-level `images/` directory by default.

### Optional 16:9 / YouTube flows

```bash
python src/gemini_yt_creator.py --help
python src/youtube_uploader.py --help
```

> For more detailed script usage, see [src/README.md](src/README.md).
