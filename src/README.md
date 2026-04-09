# Nano Banana API - Image Generation Scripts

This directory contains a standalone script `nano_banana_api.py` designed to manage local bulk and parallel generation of Nano Banana images based on `.yaml` or `::` delimited text files.

## Prerequisites

- Python 3.8+
- PyYAML `pip install pyyaml`

## Running the Script

### Single Prompt Generation

Execute a single prompt via the command line:

```bash
python nano_banana_api.py --prompt "Prometheus on the rock" --output "../images"
```

### Multiple Prompts via Text File (`::` Delimited)

```bash
python nano_banana_api.py --file "../Nano-Banana-Prompts-CP.md" --format "delimited"
```

### Multiple Prompts via YAML File

```bash
./nano_banana.sh --file "../inputs/nano-prompts.yml" --format "yaml"
```

## How It Works

1. **Parsing**: It reads the file and grabs the prompts. In `.md` files like `Nano-Banana-Prompts-CP.md`, it grabs the text before the `::` delimiter as the input name/prompt.
2. **Parallel Execution**: Uses Python's `ThreadPoolExecutor` to speed up remote/local AI image generation in parallel.
3. **Storage & Formatting**: The tool saves generated files correctly mapping their filenames to the original prompt, transforming them into Capital-Camel-Case with dashes (e.g. `The-Test-Case.png`). It also handles renaming UUID-generated output files from APIs automatically. They are placed inside your chosen `--output` directory (default: `../images/`).
