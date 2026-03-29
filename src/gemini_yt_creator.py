#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gemini YT Image / Video Asset Creator (16:9)
Automates creation of YouTube assets utilizing Google's Imagen/Gemini endpoints.
"""

import os
import re
import sys
import yaml
import time
import argparse
import google.generativeai as genai

# Try to load API key securely
GEMINI_KEY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".GEMINI_KEY")
API_KEY = os.environ.get("GEMINI_API_KEY")

if os.path.exists(GEMINI_KEY_PATH):
    with open(GEMINI_KEY_PATH, "r") as f:
        API_KEY = f.read().strip()

if not API_KEY:
    print("Warning: No Gemini API Key found in env or ../../.GEMINI_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

def generate_16_9_image(prompt_text, output_path, dry_run=False):
    if dry_run or not API_KEY:
        print(f"[DRY RUN/NO KEY] Would generate using Gemini/Imagen for: {prompt_text}")
        if not os.path.exists(output_path):
            with open(output_path, 'wb') as f:
                f.write(b"Mock Gemini Image Data. Add real API key for actual generation.\n")
        return True

    try:
        print(f"Generating 16:9 Image via Gemini for: {prompt_text}...")
        # Note: Using standard valid model for Google Generative Image API
        result = genai.generate_images(
            model='models/imagen-3.0-generate-001',
            prompt=f"A cinematic, conceptual, highly detailed 16:9 YouTube video thumbnail for: {prompt_text}",
            number_of_images=1,
            aspect_ratio="16:9",
            output_mime_type="image/jpeg"
        )
        
        # Save image
        for generated_image in result.images:
            with open(output_path, "wb") as f:
                f.write(generated_image.image.image_bytes)
            print(f"✅ Success! Saved to {output_path}")
            return True
            
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return False

def standardize_name(title):
    clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    words = clean_title.split()
    filename_base = "-".join([w.capitalize() for w in words])
    if len(filename_base) > 50:
        filename_base = filename_base[:50].rsplit('-', 1)[0]
    return filename_base

def main():
    parser = argparse.ArgumentParser(description="Generate 16:9 assets via Gemini API.")
    parser.add_argument("-y", "--yaml", default="inputs/nano-prompts-full.yml", help="Source prompts")
    parser.add_argument("-o", "--output", default="media/images_16_9", help="Output directory")
    parser.add_argument("--auto-allow", action="store_true", help="Auto process all prompts without asking")
    args = parser.parse_args()
    
    os.makedirs(args.output, exist_ok=True)
    
    if not os.path.exists(args.yaml):
        print(f"File not found: {args.yaml}")
        return
        
    with open(args.yaml, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        
    prompts = []
    if isinstance(data, dict):
        for grp, items in data.items():
            if isinstance(items, list):
                for i in items:
                    prompts.append(i.get("Prompt", i.get("Title", "")))
                    
    print(f"Found {len(prompts)} prompts. Auto-allow is {'ON' if args.auto_allow else 'OFF'}.")
    
    if not args.auto_allow:
        ans = input("Proceed with generation? (y/N): ")
        if ans.lower() != 'y':
            print("Aborted.")
            return

    for p in prompts:
        if not p: continue
        filename = standardize_name(p) + ".jpg"
        out_path = os.path.join(args.output, filename)
        
        # Skip if already exists to save API credits
        if os.path.exists(out_path):
            print(f"Skipping {filename} (Already exists)")
            continue
            
        generate_16_9_image(p, out_path, dry_run=not bool(API_KEY))
        time.sleep(1) # Simple rate limiting

if __name__ == "__main__":
    main()
