#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YouTube Prince of Persia Upload Automation script
It requires Google OAuth credentials to be set up.
Now includes YAML parsing to extract rich metadata per video based on the prompt name.
"""

import os
import argparse
import time
import yaml
import re

try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
except ImportError:
    print("Warning: Google API client libraries not installed.")
    print("Please run: pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")

# OAuth 2 Scopes to push video
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    creds = None
    token_path = "token.json"
    client_secrets_path = "../../client_secret.json" # Kept outside repo
    
    if os.path.exists(token_path):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing Google Auth token...")
            creds.refresh(Request())
        else:
            if not os.path.exists(client_secrets_path):
                print(f"ERROR: Cannot find {client_secrets_path}.")
                print("You need to create OAuth 2.0 Credentials in the Google Cloud Console.")
                print("Download the JSON, map it there, and rerun.")
                return None
                
            print("Initiating Authentication Flow (requires browser login)...")
            try:
                flow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                print(f"Auth error: {e}")
                return None
            
        with open(token_path, "w") as token:
            token.write(creds.to_json())
            
    youtube = build("youtube", "v3", credentials=creds)
    return youtube

def load_metadata_map(yaml_path):
    """Parses inputs/nano-prompts-full.yml to extract title and prompt logic."""
    metadata_map = {}
    if not os.path.exists(yaml_path):
        return metadata_map
        
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        
    if isinstance(data, dict):
        for group, items in data.items():
            if isinstance(items, list):
                for item in items:
                    if isinstance(item, dict):
                        title = item.get("Title", "")
                        prompt = item.get("Prompt", "")
                        
                        # Generate normalized name to match mp4 names
                        clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
                        words = clean_title.split()
                        capitalized_words = [word.capitalize() for word in words]
                        filename_base = "-".join(capitalized_words)
                        if len(filename_base) > 50:
                            filename_base = filename_base[:50].rsplit('-', 1)[0]
                            
                        metadata_map[filename_base] = {
                            "original_title": title,
                            "prompt": prompt,
                            "group": group
                        }
    return metadata_map

def upload_video(youtube, file_path, title, description, tags, category_id="24"):
    print(f"Uploading {file_path} to YouTube: '{title}'...")
    
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": "private", # Default to private for review
            "selfDeclaredMadeForKids": False
        }
    }
    
    try:
        insert_request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(file_path, chunksize=-1, resumable=True)
        )
        response = insert_request.execute()
        print(f"✅ Successfully uploaded '{title}'! Video ID: {response['id']}")
        return response['id']
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Upload 'Prince of Persia' batch videos to YouTube")
    parser.add_argument("-d", "--dir", default="media/videos", help="Directory with mp4 files")
    parser.add_argument("-y", "--yaml", default="inputs/nano-prompts-full.yml", help="YAML file for metadata extraction")
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"Error: {args.dir} not found.")
        return
        
    videos = [f for f in os.listdir(args.dir) if f.endswith(".mp4")]
    if not videos:
        print("No videos found to upload.")
        return
        
    print(f"Found {len(videos)} videos. Loading metadata from {args.yaml}...")
    metadata_map = load_metadata_map(args.yaml)
    
    print("Setting up YouTube API...")
    youtube = authenticate_youtube()
    
    if not youtube:
        print("Running in dry-run mode (no youtube auth available). Upload skipped.")
        # Dry-run
        for vid in videos:
            base_name = os.path.splitext(vid)[0]
            meta = metadata_map.get(base_name, {})
            title = meta.get("original_title", base_name.replace('-', ' '))
            prompt = meta.get("prompt", "Generated conceptual visualization.")
            group = meta.get("group", "General")
            
            yt_title = f"Prince of Persia: {title}"[:100] # YT title limit
            
            desc = f"Concept: {title}\nGroup: {group}\n\nPrompt Context:\n{prompt}\n\nPart of the Prince of Persia Tech & Architecture Book.\n\n#PrinceOfPersia #AI #TechArchitecture"
            print(f"-- PREVIEW: {yt_title} --\n{desc}\n")
        return
        
    for vid in videos:
        path = os.path.join(args.dir, vid)
        base_name = os.path.splitext(vid)[0]
        
        meta = metadata_map.get(base_name, {})
        title = meta.get("original_title", base_name.replace('-', ' '))
        prompt = meta.get("prompt", "Generated conceptual visualization.")
        group = meta.get("group", "General")
        
        yt_title = f"Prince of Persia: {title}"[:100]
        desc = f"Concept: {title}\nGroup: {group}\n\nPrompt Context:\n{prompt}\n\nPart of the Prince of Persia Tech & Architecture Book.\n\n#PrinceOfPersia #AI #TechArchitecture"
        tags = ["Prince of Persia", "AI Video", "Conceptual", "Short Film", group.replace(" ", "")]
        
        upload_video(youtube, path, yt_title, desc, tags)
        time.sleep(2) # rate limiting buffer
        
if __name__ == "__main__":
    main()
