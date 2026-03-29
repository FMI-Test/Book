#!/bin/bash

# Nano Banana API Wrapper Script
# Follows TomWizMaster guidelines: Concise, direct, friendly; actionable guidance.

SCRIPT_DIR=$(dirname "$0")

show_help() {
    cat <<'EOF'
Usage: nano_banana.sh [OPTIONS]

Wrapper script for generating Nano Banana images via the Python API client.
Supports single prompt execution or batch processing from delimited files.

Options:
  -h, --help               Show this help message and exit
  -p, --prompt TEXT        Generate a single image from this specific text prompt
  -f, --file PATH          Process multiple prompts from this file (.yaml or delimited by ::)
  -t, --format FORMAT      Specify file format: 'yaml' or 'delimited' (default: delimited)
  -o, --output PATH        Target directory for generated outputs (default: ../images)
  -w, --workers NUM        Number of parallel workers for processing (default: 5)

Examples:
  ./nano_banana.sh --prompt "Prometheus on the rock"
  ./nano_banana.sh --file ../Nano-Banana-Prompts-CP.md --workers 10
  ./nano_banana.sh --file inputs.yaml --format yaml
EOF
}

# defaults
PROMPT=""
FILE=""
FORMAT="delimited"
OUTPUT="../images"
WORKERS=5

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
        -p|--prompt)
            PROMPT="$2"
            shift 2
            ;;
        -f|--file)
            FILE="$2"
            shift 2
            ;;
        -t|--format)
            FORMAT="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        -w|--workers)
            WORKERS="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "For usage instructions, run: $0 --help"
            exit 1
            ;;
    esac
done

CMD=("$SCRIPT_DIR/nano_banana_api.py")

if [[ -n "$PROMPT" ]]; then
    CMD+=("--prompt" "$PROMPT")
fi

if [[ -n "$FILE" ]]; then
    CMD+=("--file" "$FILE" "--format" "$FORMAT")
fi

if [[ -n "$OUTPUT" ]]; then
    CMD+=("--output" "$OUTPUT")
fi

if [[ -n "$WORKERS" ]]; then
    CMD+=("--workers" "$WORKERS")
fi

# Execute the constructed python command
echo "Executing: ${CMD[@]}"
"${CMD[@]}"
