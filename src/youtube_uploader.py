#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
YouTube Prince of Persia Upload Automation script
It requires Google OAuth credentials to be set up.
"""

import os
import argparse
import time

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
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(token_path, "w") as token:
            token.write(creds.to_json())
            
    youtube = build("youtube", "v3", credentials=creds)
    return youtube

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
    args = parser.parse_args()
    
    if not os.path.exists(args.dir):
        print(f"Error: {args.dir} not found.")
        return
        
    videos = [f for f in os.listdir(args.dir) if f.endswith(".mp4")]
    if not videos:
        print("No videos found to upload.")
        return
        
    print(f"Found {len(videos)} videos. Setting up YouTube API...")
    youtube = authenticate_youtube()
    
    if not youtube:
        return
        
    for vid in videos:
        path = os.path.join(args.dir, vid)
        title = f"Prince of Persia: {os.path.splitext(vid)[0].replace('-', ' ')}"
        desc = "Generated 16:9 short film / conceptual visualization.\n\n#PrinceOfPersia #AI #Tech #ShortFilm"
        tags = ["Prince of Persia", "AI Video", "Conceptual", "Short Film"]
        
        upload_video(youtube, path, title, desc, tags)
        time.sleep(2) # rate limiting buffer
        
if __name__ == "__main__":
    main()
