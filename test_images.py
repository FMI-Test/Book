import re
import os
import glob

# Find all markdown files
md_files = glob.glob('*.md')
md_files += glob.glob('*/*.md')

pattern = re.compile(r'!\[.*?\]\((.*?)\)')
broken = []

for md in md_files:
    with open(md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = pattern.findall(content)
    for link in links:
        path = link.strip()
        # if the path is remote, skip
        if path.startswith('http'):
            continue
        
        # remove fragments/query
        if '?' in path:
            path = path.split('?')[0]
        if '#' in path:
            path = path.split('#')[0]

        # resolve path relative to md file
        dir_path = os.path.dirname(md)
        full_path = os.path.join(dir_path, path)
        
        if not os.path.exists(full_path):
            broken.append((md, link))

for b in broken:
    print(b)
