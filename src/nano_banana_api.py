#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import concurrent.futures
import yaml
import os
import time
import re
import uuid

# Load API key from adjacent directory to keep it out of repo path
API_KEY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".NANO_BANANA_KEY")
NANO_BANANA_API_KEY = os.environ.get("NANO_BANANA_KEY")

if os.path.exists(API_KEY_PATH):
    with open(API_KEY_PATH, "r") as f:
        NANO_BANANA_API_KEY = f.read().strip()

def format_filename(title, ext=".png"):
    """
    Format prompt into Capital-Camel-Case with dashes.
    """
    clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    words = clean_title.split()
    capitalized_words = [word.capitalize() for word in words]
    filename_base = "-".join(capitalized_words)

    if not filename_base:
        filename_base = str(uuid.uuid4())

    if len(filename_base) > 50:
        filename_base = filename_base[:50].rsplit('-', 1)[0]

    return f"{filename_base}{ext}"

def generate_image(item, output_dir="images"):
    # Ensure item is a dictionary
    if isinstance(item, str):
        item = {"Title": item, "Prompt": item}
        
    title = item.get("Title", item.get("Prompt", str(uuid.uuid4())))
    prompt = item.get("Prompt", title)
    
    filename = format_filename(title)
    filepath = os.path.join(output_dir, filename)

    print(f"Generating image for: {title}...")
    time.sleep(1)

    with open(filepath, "w") as f:
        f.write(f"Image generated for Prompt: {prompt}\n")
        f.write(f"API Key available: {bool(NANO_BANANA_API_KEY)}\n")

    return title

def process_prompts(prompts, output_dir, max_workers):
    os.makedirs(output_dir, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(generate_image, p, output_dir): p for p in prompts}
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

def parse_yaml_file(filepath):
    prompts = []
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict):
            for group, items in data.items():
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
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-p", "--prompt", type=str)
    parser.add_argument("-f", "--file", type=str)
    parser.add_argument("--format", type=str, choices=["yaml", "delimited"], default="delimited")
    parser.add_argument("-o", "--output", type=str, default="../images")
    parser.add_argument("-w", "--workers", type=int, default=5)

    args = parser.parse_args()
    prompts = []

    if args.prompt:
        prompts.append({"Title": args.prompt, "Prompt": args.prompt})

    if args.file and os.path.exists(args.file):
        if args.format == "yaml" or args.file.endswith((".yaml", ".yml")):
            prompts.extend(parse_yaml_file(args.file))
        else:
            prompts.extend(parse_double_colon_file(args.file))

    if not prompts:
        print("No prompts found.")
        return

    print(f"Loaded {len(prompts)} prompts. Starting generation...")
    process_prompts(prompts, args.output, args.workers)
    print("Done!")

if __name__ == "__main__":
    main()
