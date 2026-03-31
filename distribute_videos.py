import os
import re

videos = [f for f in os.listdir("media/videos") if f.endswith(".mp4")]
md_files = [f for f in os.listdir(".") if f.endswith(".md") and f not in ["distribute_images.py", "distribute_videos.py", "YOUTUBE-AUTOMATION.md"]]

def norm(x):
    return re.sub(r'[^a-z0-9]', '', x.lower())

for vid in videos:
    vid_name = os.path.splitext(vid)[0]
    n_vid = norm(vid_name)
    best_file = "Nano-Banana-Prompts.md"
    best_score = 0
    
    for md in md_files:
        md_name = os.path.splitext(md)[0]
        n_md = norm(md_name)
        
        score = 0
        if n_vid == n_md:
            score = 100
        elif n_md in n_vid:
            score = len(n_md) * 2
        elif n_vid in n_md:
            score = len(n_vid) * 2
            
        vid_words = set(re.findall(r'[a-zA-Z0-9]+', vid_name.lower()))
        md_words = set(re.findall(r'[a-zA-Z0-9]+', md_name.lower()))
        overlap = len(vid_words.intersection(md_words))
        score += overlap * 5
        
        if score > best_score:
            best_score = score
            best_file = md

    print(f"Adding {vid} to {best_file} (score: {best_score})")
    with open(best_file, "a", encoding="utf-8") as f:
        f.write(f"\n\n<!-- 16:9 Video Generation Match -->\n<video width=\"100%\" controls>\n  <source src=\"./media/videos/{vid}\" type=\"video/mp4\">\n  Your browser does not support the video tag.\n</video>\n*[Generated 16:9 Short Film mapped for {vid_name}]*\n")
