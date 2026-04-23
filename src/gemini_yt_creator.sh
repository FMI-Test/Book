#!/bin/bash
# Wrapper for Gemini 16:9 Image Generation
# Generates cinematic 16:9 thumbnails/videos directly via Google Gemini API.

SCRIPT_DIR=$(dirname "$0")

show_help() {
    cat <<'HELP_END'
Usage: gemini_yt_creator.sh [OPTIONS]

Wrapper script for generating 16:9 assets using Google Gemini Imagen API.
Reads from prompts in inputs/nano-prompts-full.yml by default.

Options:
  -h, --help               Show this help message
  -y, --yaml PATH          Inputs YAML file
  -o, --output PATH        Output path for 16:9 assets (default: media/images_16_9)
  -a, --auto-allow         Auto-allow execution (skip confirmation prompts)

Examples:
  ./src/gemini_yt_creator.sh --auto-allow
HELP_END
}

YAML="inputs/nano-prompts-full.yml"
OUTPUT="media/images_16_9"
AUTO_ALLOW=""

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h|--help) show_help; exit 0 ;;
        -y|--yaml) YAML="$2"; shift ;;
        -o|--output) OUTPUT="$2"; shift ;;
        -a|--auto-allow) AUTO_ALLOW="--auto-allow" ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

CMD=("$SCRIPT_DIR/gemini_yt_creator.py" "--yaml" "$YAML" "--output" "$OUTPUT")
if [ -n "$AUTO_ALLOW" ]; then
    CMD+=("$AUTO_ALLOW")
fi

echo "Executing: ${CMD[*]}"
"${CMD[@]}"
