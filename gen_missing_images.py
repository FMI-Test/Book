#!/usr/bin/env python3
"""
gen_missing_images.py
Generate the 5 missing images referenced in Aliyar-Fakhran-EN.md.
Uses Gemini Imagen API if available, falls back to labeled PNG placeholders.
Saves both .png and .webp for each image.
"""
import os
import struct
import zlib
import shutil

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
WORKSPACE_PARENT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GEMINI_KEY_PATH = os.path.join(WORKSPACE_PARENT, ".GEMINI_KEY")

API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not API_KEY and os.path.exists(GEMINI_KEY_PATH):
    with open(GEMINI_KEY_PATH) as f:
        API_KEY = f.read().strip()

# --- Nano Banana style prompts for each missing image ---
MISSING_IMAGES = [
    {
        "stem": "Qajar-vs-Pahlavi-Era",
        "prompt": (
            "Historical documentary illustration comparing Qajar and Pahlavi administrative eras in Iran. "
            "Split composition: left side shows ornate Qajar court officials in traditional dress circa 1900; "
            "right side shows modernized Pahlavi bureaucrats in Western suits circa 1935. "
            "Warm sepia tones, archival photographic style, cinematic 16:9 format."
        ),
    },
    {
        "stem": "Ali-Yar-Fakhran-Credentials-in-Tsarist",
        "prompt": (
            "Formal diplomatic ceremony: a Persian envoy presenting credentials to the Tsarist Russian imperial court "
            "circa 1905-1914. Grand hall interior, ornate columns, Persian diplomat in formal dress, "
            "Russian imperial officials, gold and red tones, documentary oil-painting style, 16:9."
        ),
    },
    {
        "stem": "Garmeh-Jajarm-Ivar-Darq",
        "prompt": (
            "North Khorasan landscape, Garmeh and Jajarm region of Iran. Winding mountain road through "
            "dense Golestan forest, hairpin curves, ancient stone caravanserai visible in distance, "
            "golden afternoon light, historical travel route, documentary photography style, 16:9."
        ),
    },
    {
        "stem": "Kargozar-Children",
        "prompt": (
            "Early 20th century Iranian family portrait: four sons of a Qajar-era Kargozar official. "
            "Formal studio setting, the brothers dressed in period clothing, dignified posture, "
            "sepia-toned archival photographic aesthetic, historical documentary style, 16:9."
        ),
    },
    {
        "stem": "Grandmother-Curse",
        "prompt": (
            "Iranian matriarch figure, elderly sharp-tongued grandmother from early 20th century Iran. "
            "Warm domestic interior, traditional dress, knowing expression, storytelling atmosphere, "
            "family memory rendering, warm oil-paint style with soft vignette edges, 16:9."
        ),
    },
]


# ── Placeholder PNG generator ────────────────────────────────────────────────

def _chunk(tag: bytes, data: bytes) -> bytes:
    c = struct.pack(">I", len(data)) + tag + data
    return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)


def make_placeholder_png(label: str, width: int = 160, height: int = 90) -> bytes:
    """Create a minimal grey PNG with the label encoded in a tEXt chunk."""
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    ihdr = _chunk(b"IHDR", ihdr_data)

    # Build raw image data (solid grey #888)
    row = b"\x00" + b"\x88\x88\x88" * width
    raw = row * height
    idat = _chunk(b"IDAT", zlib.compress(raw))

    # Embed label as tEXt metadata
    text_data = b"Comment\x00" + label.encode("latin-1", errors="replace")
    text = _chunk(b"tEXt", text_data)

    iend = _chunk(b"IEND", b"")
    return b"\x89PNG\r\n\x1a\n" + ihdr + idat + text + iend


# ── Gemini generation ─────────────────────────────────────────────────────────

def generate_with_gemini(prompt: str, output_path: str) -> bool:
    try:
        import google.generativeai as genai
        genai.configure(api_key=API_KEY)
        result = genai.generate_images(
            model="models/imagen-3.0-generate-001",
            prompt=prompt,
            number_of_images=1,
            aspect_ratio="16:9",
            output_mime_type="image/png",
        )
        for img in result.images:
            with open(output_path, "wb") as f:
                f.write(img.image.image_bytes)
            return True
    except Exception as e:
        print(f"  [GEMINI ERROR] {e}")
    return False


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    use_gemini = bool(API_KEY)

    if use_gemini:
        print("Gemini API key found — attempting real image generation.")
    else:
        print("No Gemini API key — generating labeled PNG placeholders.")

    generated = []
    skipped = []

    for entry in MISSING_IMAGES:
        stem = entry["stem"]
        prompt = entry["prompt"]
        png_path = os.path.join(IMAGES_DIR, stem + ".png")
        webp_path = os.path.join(IMAGES_DIR, stem + ".webp")

        # Check if both already exist
        if os.path.exists(png_path) and os.path.exists(webp_path):
            print(f"  [SKIP] {stem} — both .png and .webp already exist.")
            skipped.append(stem)
            continue

        print(f"\n  [GEN] {stem}")

        success = False
        if use_gemini and not os.path.exists(png_path):
            success = generate_with_gemini(prompt, png_path)

        if not success and not os.path.exists(png_path):
            print(f"  [PLACEHOLDER] Writing labeled PNG for {stem}")
            with open(png_path, "wb") as f:
                f.write(make_placeholder_png(stem))
            success = True

        # Produce .webp: try Pillow conversion, fall back to copy
        if success and not os.path.exists(webp_path):
            try:
                from PIL import Image
                img = Image.open(png_path)
                img.save(webp_path, "WEBP", quality=85)
                print(f"  [WEBP] Converted via Pillow → {stem}.webp")
            except Exception:
                shutil.copy2(png_path, webp_path)
                print(f"  [WEBP] Copied (no Pillow) → {stem}.webp")

        generated.append(stem)

    print("\n── Summary ─────────────────────────────────────────")
    print(f"  Generated : {len(generated)} image(s)")
    for s in generated:
        print(f"    ✓ {s}.png + .webp")
    if skipped:
        print(f"  Skipped   : {len(skipped)} (already existed)")
    print("────────────────────────────────────────────────────")


if __name__ == "__main__":
    main()
