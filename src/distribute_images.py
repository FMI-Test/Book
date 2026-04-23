import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

images = [f for f in os.listdir(os.path.join(ROOT, "images")) if f.endswith(".png")]
md_files = [f for f in os.listdir(ROOT) if f.endswith(".md")]

def norm(x):
    return re.sub(r'[^a-z0-9]', '', x.lower())

for img in images:
    img_name = os.path.splitext(img)[0]
    n_img = norm(img_name)
    best_file = "Nano-Banana-Prompts.md"
    best_score = 0
    
    for md in md_files:
        md_name = os.path.splitext(md)[0]
        n_md = norm(md_name)
        
        score = 0
        if n_img == n_md:
            score = 100
        elif n_md in n_img:
            score = len(n_md) * 2
        elif n_img in n_md:
            score = len(n_img) * 2
            
        img_words = set(re.findall(r'[a-zA-Z0-9]+', img_name.lower()))
        md_words = set(re.findall(r'[a-zA-Z0-9]+', md_name.lower()))
        overlap = len(img_words.intersection(md_words))
        score += overlap * 5
        
        if score > best_score:
            best_score = score
            best_file = md

    print(f"Adding {img} to {best_file} (score: {best_score})")
    with open(os.path.join(ROOT, best_file), "a", encoding="utf-8") as f:
        f.write(f"\n\n![{img_name}](./images/{img})\n")
