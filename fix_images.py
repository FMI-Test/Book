import os

replacements = {
    'Ali-Yar-Fakhran-Dar-Al-Fonun.png': 'Aliyar-Fakhran-Dar-Al-Fonun.png',
    'Ali-Yar-Fakhran-Bujnurd-Governor.png': 'Aliyar-Fakhran-Bujnurd-Governor.png',
    'Ali-Yar-Fakhran-Lion-Sun-Medal.png': 'Aliyar-Fakhran-Lion-Sun-Medal.png',
    'Ali-Yar-Fakhran-Leningrad-Ambassador.png': 'Aliyar-Fakhran-Leningrad-Ambassador.png',
    'Ali-Yar-Fakhran-Petersburg-Embassy.png': 'Aliyar-Fakhran-Petersburg-Embassy.png',
    'Ali-Yar-Fakhran-Genealogy-Tree.png': 'Aliyar-Fakhran-Genealogy-Tree.png',
    'Ali-Yar-Fakhran-Calligraphy-Wall.png': 'Aliyar-Fakhran-Calligraphy-Wall.png',
    'Ali-Yar-Fakhran-Dinner-Protocol.png': 'Aliyar-Fakhran-Dinner-Protocol.png',
    'Ali-Yar-Fakhran-Bamdad-Heritage.png': 'Aliyar-Fakhran-Bamdad-Heritage.png',
    'Ali-Yar-Fakhran-Fakhran-Sara-Villa.png': 'Fakhran-Sara-Villa.png',
    'Ali-Yar-Fakhran-Reza-Shah-Era.png': 'Aliyar-Fakhran-Reze-Shah-Diplomat.png',
}

files = ['Aliyar-Fakhran-EN.md', 'Aliyar-Fakhran-FA.md']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
