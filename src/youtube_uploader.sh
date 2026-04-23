#!/bin/bash

# YouTube Uploader Wrapper Script
# Follows TomWizMaster guidelines: concise, direct, friendly, actionable guidance.

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

show_help() {
    cat <<'EOF'
Usage: youtube_uploader.sh [OPTIONS]

Wrapper script for uploading generated short films to YouTube.
Automatically extracts metadata from `inputs/nano-prompts-full.yml`.

Options:
  -h, --help               Show this help message and exit
  -d, --dir PATH           Directory containing .mp4 files (default: media/videos)
  -y, --yaml PATH          YAML file for metadata extraction (default: inputs/nano-prompts-full.yml)

Examples:
  ./src/youtube_uploader.sh
  ./src/youtube_uploader.sh --dir "media/videos"
EOF
}

VIDEOS_DIR="media/videos"
YAML="inputs/nano-prompts-full.yml"

if [[ $# -eq 0 ]]; then
    show_help
    exit 0
fi

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        -d|--dir)
            VIDEOS_DIR="$2"
            shift 2
            ;;
        -y|--yaml)
            YAML="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "For usage instructions, run: $0 --help"
            exit 1
            ;;
    esac
done

CMD=("$SCRIPT_DIR/youtube_uploader.py" "--dir" "$VIDEOS_DIR" "--yaml" "$YAML")

echo "Executing: ${CMD[*]}"
"${CMD[@]}"

