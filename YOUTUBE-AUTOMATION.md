# Prince of Persia: YouTube Automation Guide

This repository now contains a fully automated ingestion path to read images, generate Mock 16:9 MP4 short films, update your markdown documents, and bulk-publish the outputs directly to a newly created YouTube Channel.

## 1. Directory Structure Setup
A top-level `/media` directory is now constructed specifically to handle multi-faceted assets:
- `media/videos/`
- `media/audio/`
- `media/music/`

*(Later audio & music generators can output MP3/WAV files to their respective folders.)*

## 2. Setting Up YouTube
Since Python cannot bypass Google's direct security layer to create a new *Identity*, you must register an App to interface with it:

1. **Create the Channel:** Head to [YouTube Studio](https://studio.youtube.com/) and register a new channel named **"Prince of Persia"**.
2. **Google Cloud Console:** 
   * Navigate to [Google Cloud Console](https://console.cloud.google.com/).
   * Create a New Project ("Prince of Persia Automation").
   * Go to **APIs & Services** > **Library** -> Search and enable **"YouTube Data API v3"**.
3. **OAuth Consent Screen:**
   * Go to **OAuth consent screen** -> set as 'External' -> fill out basic name/emails.
   * Add the scope: `https://www.googleapis.com/auth/youtube.upload`
4. **Create Credentials:**
   * Go to **Credentials** -> **Create Credentials** -> **OAuth client ID**.
   * App Type: **Desktop App**.
   * Download the JSON file. 
5. **Secure the Token:**
   Rename the downloaded JSON file to `client_secret.json` and move it to `../../client_secret.json` (outside your GitHub repo to prevent accidental API key leaks).

## 3. Running the Automation
First, make sure the Python requirements are loaded:
```bash
python -m pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
```

Then, trigger the publisher!
```bash
python src/youtube_uploader.py --dir media/videos
```
When you run it the first time, it will open your web browser so you can log into the Prince of Persia YouTube account and grant "Upload" permissions. The scripts push the files as `Private` initially so you can review them prior to sending them live.

*All systems automated! AAK!*
