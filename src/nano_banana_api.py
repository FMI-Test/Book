#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import concurrent.futures
import yaml
import os
import time
import re
import uuid

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
WORKSPACE_PARENT = os.path.abspath(os.path.join(REPO_ROOT, ".."))

# Load API key from the parent workspace directory to keep it out of the repo.
API_KEY_PATH = os.path.join(WORKSPACE_PARENT, ".NANO_BANANA_KEY")
NANO_BANANA_API_KEY = os.environ.get("NANO_BANANA_KEY")

if os.path.exists(API_KEY_PATH):
    with open(API_KEY_PATH, "r") as f:
        NANO_BANANA_API_KEY = f.read().strip()


def resolve_input_path(path_value):
    if not path_value:
        return path_value
    if os.path.isabs(path_value):
        return path_value

    cwd_candidate = os.path.abspath(path_value)
    if os.path.exists(cwd_candidate):
        return cwd_candidate

    return os.path.join(REPO_ROOT, path_value.lstrip("./"))


def resolve_output_path(path_value):
    if os.path.isabs(path_value):
        return path_value
    return os.path.join(REPO_ROOT, path_value.lstrip("./"))


def format_filename(title, ext=".png"):
    """
    Format prompt title into Capital-Camel-Case with dashes.
    If the title already looks like a dash-separated filename (e.g. Ali-Yar-Fakhran-X),
    preserve it as-is (with capitalisation). Otherwise convert spaces to dashes.
    """
    # If title already contains dashes and no spaces, treat each segment as a word
    if '-' in title and ' ' not in title:
        words = title.split('-')
    else:
        # Strip non-alphanumeric except spaces and dashes, then split on spaces/dashes
        clean_title = re.sub(r'[^a-zA-Z0-9\s\-]', '', title)
        words = re.split(r'[\s\-]+', clean_title)

    capitalized_words = [word.capitalize() for word in words if word]
    filename_base = "-".join(capitalized_words)

    if not filename_base:
        filename_base = str(uuid.uuid4())

    if len(filename_base) > 80:
        filename_base = filename_base[:80].rsplit('-', 1)[0]

    return f"{filename_base}{ext}"

def generate_image(item, output_dir="images", overwrite=False):
    # Ensure item is a dictionary
    if isinstance(item, str):
        item = {"Title": item, "Prompt": item}

    title = item.get("Title", item.get("Prompt", str(uuid.uuid4())))
    prompt = item.get("Prompt", title)

    filename = format_filename(title)
    filepath = os.path.join(output_dir, filename)

    if os.path.exists(filepath) and not overwrite:
        print(f"Skipping (exists): {filename}  — use --overwrite to regenerate")
        return title

    print(f"Generating image for: {title}...")
    time.sleep(1)

    with open(filepath, "w") as f:
        f.write(f"Image generated for Prompt: {prompt}\n")
        f.write(f"API Key available: {bool(NANO_BANANA_API_KEY)}\n")

    return title

def process_prompts(prompts, output_dir, max_workers, overwrite=False):
    os.makedirs(output_dir, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(generate_image, p, output_dir, overwrite): p for p in prompts}
        for future in concurrent.futures.as_completed(futures):
            p = futures[future]
            try:
                future.result()
            except Exception as exc:
                print(f"Exception generated for {p}: {exc}")

def parse_double_colon_file(filepath):
    prompts = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if "::" in line:
                parts = line.split("::", 1)
                title = parts[0].strip()
                prompt = parts[1].strip()
                prompts.append({"Title": title, "Prompt": prompt})
    return prompts

def parse_yaml_file(filepath, section=None):
    prompts = []
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict):
            for group, items in data.items():
                if section and group != section:
                    continue
                if isinstance(items, list):
                    for item in items:
                        if isinstance(item, dict) and ("Title" in item or "Prompt" in item):
                            prompts.append(item)
                        elif isinstance(item, str):
                            prompts.append({"Title": item, "Prompt": item})
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    prompts.append(item)
                else:
                    prompts.append({"Title": str(item), "Prompt": str(item)})
    return prompts

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Generate images from nano prompts.\n"
                    "By default, skips images that already exist.\n"
                    "Use --overwrite to regenerate existing images.\n"
                    "Use --section to process only a named YAML section (e.g. --section Fakhran).")
    parser.add_argument("-p", "--prompt", type=str, help="Single prompt string")
    parser.add_argument("-f", "--file", type=str, help="Prompt file (.yml or delimited)")
    parser.add_argument("--format", type=str, choices=["yaml", "delimited"], default="delimited")
    parser.add_argument("-o", "--output", type=str, default="images")
    parser.add_argument("-w", "--workers", type=int, default=5)
    parser.add_argument("--overwrite", action="store_true",
                        help="Overwrite existing images (default: skip if image file exists)")
    parser.add_argument("--section", type=str, default=None,
                        help="Process only this named YAML section (e.g. --section Fakhran)")

    args = parser.parse_args()
    prompts = []
    output_dir = resolve_output_path(args.output)
    prompt_file = resolve_input_path(args.file) if args.file else None

    if args.prompt:
        prompts.append({"Title": args.prompt, "Prompt": args.prompt})

    if prompt_file and os.path.exists(prompt_file):
        if args.format == "yaml" or prompt_file.endswith((".yaml", ".yml")):
            prompts.extend(parse_yaml_file(prompt_file, section=args.section))
        else:
            prompts.extend(parse_double_colon_file(prompt_file))

    if not prompts:
        print("No prompts found.")
        return

    print(f"Loaded {len(prompts)} prompts. Starting generation (overwrite={args.overwrite})...")
    process_prompts(prompts, output_dir, args.workers, overwrite=args.overwrite)
    print("Done!")

if __name__ == "__main__":
    main()
