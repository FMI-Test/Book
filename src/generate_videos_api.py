#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mock Video Generation API using Images (16:9 for Desktop/Mobile)
Simulates fetching from a Gemini/Runway/Pika video generation endpoint.
"""

import os
import time
import argparse

def generate_video(image_path, output_dir="media/videos"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract base name
    base_name = os.path.basename(image_path)
    name_without_ext = os.path.splitext(base_name)[0]
    
    # Simulate API call for video generation
    print(f"Generating 16:9 video for {base_name}...")
    time.sleep(0.01) # Simulation delay
    
    output_file = os.path.join(output_dir, f"{name_without_ext}.mp4")
    
    # Create mock MP4 file
    with open(output_file, "w") as f:
        f.write(f"MOCK VIDEO METADATA\nSource Image: {image_path}\nAspect Ratio: 16:9\nPlatform: YouTube/Desktop/Mobile\n")
        
    return output_file

def main():
    parser = argparse.ArgumentParser(description="Generate mock short films from images.")
    parser.add_argument("-i", "--images_dir", default="images", help="Directory containing source images.")
    parser.add_argument("-o", "--output_dir", default="media/videos", help="Output directory for generated videos.")
    args = parser.parse_args()
    
    if not os.path.exists(args.images_dir):
        print(f"Error: {args.images_dir} does not exist.")
        return
        
    images = [f for f in os.listdir(args.images_dir) if f.endswith(".png") or f.endswith(".jpg")]
    print(f"Found {len(images)} images to process.")
    
    for img in images:
        generate_video(os.path.join(args.images_dir, img), args.output_dir)
        
    print(f"Video generation complete! Files saved to {args.output_dir}.")

if __name__ == "__main__":
    main()
