#!/usr/bin/env python3
"""
_fill_missing_webp.py
Scan all .md files for referenced webp images, then create labeled placeholder
webp files for any that are still missing after source conversions.
"""
import os
import re
import struct
import zlib
import urllib.parse
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).parent
IMAGES_DIR = REPO_ROOT / "images"

# ── Minimal PNG builder ───────────────────────────────────────────────────────

def _chunk(tag: bytes, data: bytes) -> bytes:
    c = struct.pack(">I", len(data)) + tag + data
    return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)


def make_placeholder_png(label: str, width: int = 160, height: int = 90) -> bytes:
    ihdr = _chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    row = b"\x00" + b"\x88\x88\x88" * width
    idat = _chunk(b"IDAT", zlib.compress(row * height))
    text = _chunk(b"tEXt", b"Comment\x00" + label.encode("latin-1", errors="replace"))
    iend = _chunk(b"IEND", b"")
    return b"\x89PNG\r\n\x1a\n" + ihdr + idat + text + iend


def png_to_webp(png_path: Path, webp_path: Path):
    """Convert PNG to WEBP using Pillow; fall back to raw copy."""
    try:
        from PIL import Image
        img = Image.open(png_path)
        img.save(webp_path, "WEBP", quality=85)
        return "pillow"
    except Exception:
        shutil.copy2(png_path, webp_path)
        return "copy"


# ── Collect all referenced webp paths ────────────────────────────────────────

def collect_referenced_webps() -> set:
    pattern = re.compile(r'images/[^)"` \n]+\.webp')
    refs = set()
    for md in REPO_ROOT.glob("**/*.md"):
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in pattern.findall(text):
            decoded = urllib.parse.unquote(m)
            refs.add(decoded)
    return refs


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    IMAGES_DIR.mkdir(exist_ok=True)
    refs = collect_referenced_webps()
    print(f"Total unique webp references in markdown: {len(refs)}")

    missing = [r for r in sorted(refs) if not (REPO_ROOT / r).exists()]
    print(f"Still missing after prior conversions: {len(missing)}\n")

    created = []
    for rel in missing:
        webp_path = REPO_ROOT / rel
        stem = webp_path.stem
        png_path = webp_path.with_suffix(".png")

        # Check if a .png source exists (different casing is unlikely on macOS but try)
        if not png_path.exists():
            # Write placeholder PNG
            png_path.write_bytes(make_placeholder_png(stem))
            src = "placeholder"
        else:
            src = "existing-png"

        method = png_to_webp(png_path, webp_path)
        print(f"  [OK] {rel}  ({src} → webp via {method})")
        if src == "placeholder":
            png_path.unlink()  # clean up temp png, webp is all we need
        created.append(rel)

    print(f"\n── Summary ────────────────────────────────")
    print(f"  Created : {len(created)} placeholder webp(s)")
    existing = len(refs) - len(missing)
    print(f"  Already present: {existing}")
    print(f"  Total referenced: {len(refs)}")


if __name__ == "__main__":
    main()
