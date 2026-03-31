#!/bin/bash

# YouTube Uploader Wrapper Script
# Follows TomWizMaster guidelines: Concise, direct, friendly; actionable guidance.

SCRIPT_DIR=$(dirname "$0")

show_help() {
    cat <<'EOF'
Usage: youtube_uploader.sh [OPTIONS]

Wrapper script for uploading generated short films to the Prince of Persia YouTube channel.
Automatically extracts metadata from prompts.yml and tags videos contextually.

Options:
  -h, --help               Show this help message and exit
  -d, --dir PATH           Directory containing .mp4 files (default: media/videos)
  -y, --yaml PATH          YAML file for metadata extraction (default: inputs/nano-prompts-full.yml)

Examples:
  ./youtube_uploader.sh
  ./youtube_uploader.sh --dir "custom/videos/path"
