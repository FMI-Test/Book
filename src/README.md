# Automation Scripts

This directory contains the repo's local automation tooling for image generation, video generation, metadata extraction, and upload workflows.

## Shared dependencies

Install the common Python dependencies from the repo root:

```bash
pip install -r requirements.txt
```

### Optional secrets / credentials

- `../.GEMINI_KEY` (or `GEMINI_API_KEY`) for Gemini asset generation
- `../client_secret.json` for YouTube OAuth upload

> Secrets stay outside the repo root by design.

## Main scripts

| Script | Purpose |
| --- | --- |
| `nano_banana_api.py` | Bulk or single image generation from prompt text or YAML |
| `nano_banana.sh` | Shell wrapper for `nano_banana_api.py` |
| `generate_yaml.py` | Convert `::` prompt lists into YAML |
| `gemini_yt_creator.py` | Generate 16:9 Gemini/Imagen assets |
| `gemini_yt_creator.sh` | Shell wrapper for Gemini asset generation |
| `generate_videos_api.py` | Generate mock short-form videos from images |
| `youtube_uploader.py` | Upload generated videos to YouTube with metadata |
| `youtube_uploader.sh` | Shell wrapper for YouTube uploads |

## Typical usage

Run these commands from the **repo root**:

### Single prompt generation

```bash
python src/nano_banana_api.py --prompt "Prometheus on the rock"
```

### Batch generation from a `::` markdown file

```bash
./src/nano_banana.sh --file "Nano-Banana-Prompts-CP.md" --format delimited --workers 10
```

### Batch generation from the canonical YAML file

```bash
./src/nano_banana.sh --file "inputs/nano-prompts-full.yml" --format yaml --section Fakhran
```

### Gemini / YouTube helpers

```bash
python src/gemini_yt_creator.py --help
python src/youtube_uploader.py --help
```

## Notes

1. Paths are resolved from the repo root so the commands behave consistently.
2. Existing outputs are skipped unless you pass `--overwrite`.
3. The wrappers expose the most common options for day-to-day runs.

