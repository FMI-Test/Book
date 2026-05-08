# Automation Scripts

This directory contains the repo's local automation tooling for image generation, video generation, metadata extraction, and upload workflows.

## Shared dependencies

Install the common Python dependencies from the repo root:

```bash
pip install -r requirements.txt
```

### Optional secrets / credentials

- `../.GEMINI_KEY` (or `GEMINI_API_KEY`) for Gemini asset generation and Nano Banana image generation
- `../client_secret.json` for YouTube OAuth upload

> Secrets stay outside the repo root by design.

## Main scripts

| Script | Purpose |
| --- | --- |
| `nano_banana_api.py` | Bulk or single image generation from prompt text or YAML |
| `nano_banana.sh` | Shell wrapper for `nano_banana_api.py` |
| `generate_yaml.py` | Convert `::` prompt lists into YAML |
| `gemini_yt_creator.py` | Generate 16:9 Gemini/Imagen assets |
| `gemini_yt_creator.sh` | Shell wrapper for Gemini asset generation |
| `generate_videos_api.py` | Generate mock short-form videos from images |
| `youtube_uploader.py` | Upload generated videos to YouTube with metadata |
| `youtube_uploader.sh` | Shell wrapper for YouTube uploads |

## Typical usage

Run these commands from the **repo root**:

### Single prompt generation

```bash
python src/nano_banana_api.py --prompt "Prometheus on the rock"
```

### Batch generation from a `::` markdown file

```bash
./src/nano_banana.sh --file "Nano-Banana-Prompts-CP.md" --format delimited --workers 10
```

### Batch generation from the canonical YAML file

```bash
./src/nano_banana.sh --file "inputs/nano-prompts-full.yml" --format yaml --section Fakhran
```

### Gemini / YouTube helpers

```bash
python src/gemini_yt_creator.py --help
python src/youtube_uploader.py --help
```

## Notes

1. Paths are resolved from the repo root so the commands behave consistently.
2. Existing outputs are skipped unless you pass `--overwrite`.
3. The wrappers expose the most common options for day-to-day runs.

## Book Path Image References (Forward)

Copied from AAK intake commit ae88b8d. Paths use forward-slash /Book references.

- [20260415_154231_single_result_4b880bf9-718f-4a88-9180-4d7945cfce58.jpg](/Book/images/20260415_154231_single_result_4b880bf9-718f-4a88-9180-4d7945cfce58.jpg)
- [20260415_154404_single_result_66278e03-3b23-45af-8d17-580417d767b6.jpg](/Book/images/20260415_154404_single_result_66278e03-3b23-45af-8d17-580417d767b6.jpg)
- [20260415_154437_single_result_9c59fab1-5b63-4e64-afee-514203fe4ed8.jpg](/Book/images/20260415_154437_single_result_9c59fab1-5b63-4e64-afee-514203fe4ed8.jpg)
- [20260415_155103_single_result_ed3dbb49-5c7d-45b9-897b-a12a7fa312e7.jpg](/Book/images/20260415_155103_single_result_ed3dbb49-5c7d-45b9-897b-a12a7fa312e7.jpg)
- [20260415_155558_single_result_5fb1dc70-12df-4fdd-808f-3b841c6a1337.jpg](/Book/images/20260415_155558_single_result_5fb1dc70-12df-4fdd-808f-3b841c6a1337.jpg)
- [20260415_160018_single_result_d95da585-9724-45da-87e4-8bbe685bc542.jpg](/Book/images/20260415_160018_single_result_d95da585-9724-45da-87e4-8bbe685bc542.jpg)
- [20260415_160321_single_result_4c5d3cce-7b79-4bac-9d43-20570bfd6f8f.jpg](/Book/images/20260415_160321_single_result_4c5d3cce-7b79-4bac-9d43-20570bfd6f8f.jpg)
- [2ce47ff274edf67a66ea3145d92b94e8.jpg](/Book/images/2ce47ff274edf67a66ea3145d92b94e8.jpg)
- [Ali-Yar-Fakhran-02.png](/Book/images/Ali-Yar-Fakhran-02.png)
- [Ali-Yar-Fakhran-Batumi-Consulate.png](/Book/images/Ali-Yar-Fakhran-Batumi-Consulate.png)
- [Ali-Yar-Fakhran-Credentials-in-Tsarist.png](/Book/images/Ali-Yar-Fakhran-Credentials-in-Tsarist.png)
- [Ali-Yar-Fakhran-Full-France.png](/Book/images/Ali-Yar-Fakhran-Full-France.png)
- [Ali-Yar-Fakhran-Full-Spain.png](/Book/images/Ali-Yar-Fakhran-Full-Spain.png)
- [Ali-Yar-Fakhran-Full.png](/Book/images/Ali-Yar-Fakhran-Full.png)
- [Ali-Yar-Fakhran-Office.png](/Book/images/Ali-Yar-Fakhran-Office.png)
- [Ali-Yar-Fakhran-Russia.png](/Book/images/Ali-Yar-Fakhran-Russia.png)
- [Ali-Yar-Fakhran-Spain.png](/Book/images/Ali-Yar-Fakhran-Spain.png)
- [Ali-Yar-Fakhran-Tbilisi-Consulate.png](/Book/images/Ali-Yar-Fakhran-Tbilisi-Consulate.png)
- [Ali-Yar-Fakhran.png](/Book/images/Ali-Yar-Fakhran.png)
- [Aliyar-Fakhran-Bamdad-Heritage.png](/Book/images/Aliyar-Fakhran-Bamdad-Heritage.png)
- [Aliyar-Fakhran-Batumi-Consulate.png](/Book/images/Aliyar-Fakhran-Batumi-Consulate.png)
- [Aliyar-Fakhran-Bujnurd-Governor.png](/Book/images/Aliyar-Fakhran-Bujnurd-Governor.png)
- [Aliyar-Fakhran-Calligraphy-Wall.png](/Book/images/Aliyar-Fakhran-Calligraphy-Wall.png)
- [Aliyar-Fakhran-Dar-Al-Fonun.png](/Book/images/Aliyar-Fakhran-Dar-Al-Fonun.png)
- [Aliyar-Fakhran-Dinner-Protocol.png](/Book/images/Aliyar-Fakhran-Dinner-Protocol.png)
- [Aliyar-Fakhran-Leningrad-Ambassador.png](/Book/images/Aliyar-Fakhran-Leningrad-Ambassador.png)
- [Aliyar-Fakhran-Lion-Sun-Medal.png](/Book/images/Aliyar-Fakhran-Lion-Sun-Medal.png)
- [Aliyar-Fakhran-Reze-Shah-Diplomat.png](/Book/images/Aliyar-Fakhran-Reze-Shah-Diplomat.png)
- [Aliyar-Fakhran-Tbilisi-Consulate.png](/Book/images/Aliyar-Fakhran-Tbilisi-Consulate.png)
- [BACK-COVER.png](/Book/images/BACK-COVER.png)
- [Bodhi-Tree.png](/Book/images/Bodhi-Tree.png)
- [CHAPTER-7-8.png](/Book/images/CHAPTER-7-8.png)
- [COMPLEMENTARY.png](/Book/images/COMPLEMENTARY.png)
- [COMPLEX.png](/Book/images/COMPLEX.png)
- [COMPLICATED.png](/Book/images/COMPLICATED.png)
- [COVER.png](/Book/images/COVER.png)
- [DR-FAKHRAN-BAHMAN-PARS-MARYAM-FAKHRAN.png](/Book/images/DR-FAKHRAN-BAHMAN-PARS-MARYAM-FAKHRAN.png)
- [ELI-AN-DANIAN-INSIGHT.png](/Book/images/ELI-AN-DANIAN-INSIGHT.png)
- [EXECUTION-GAP.png](/Book/images/EXECUTION-GAP.png)
- [FOUNDATION-MEDICINE.png](/Book/images/FOUNDATION-MEDICINE.png)
- [FRIENDS-N-FAMILY-TREE.png](/Book/images/FRIENDS-N-FAMILY-TREE.png)
- [Fakhran-Sara-Villa.png](/Book/images/Fakhran-Sara-Villa.png)
- [Ghost.jpg](/Book/images/Ghost.jpg)
- [Grandmother-Curse.png](/Book/images/Grandmother-Curse.png)
- [Job-Silence.png](/Book/images/Job-Silence.png)
- [Kargozar-Children.png](/Book/images/Kargozar-Children.png)
- [Kargozar-Titles.png](/Book/images/Kargozar-Titles.png)
- [Qajar-vs-Pahlavi-Era.png](/Book/images/Qajar-vs-Pahlavi-Era.png)
- [REFLECTION-ON-TECHNOLOGY-N-LIFE.png](/Book/images/REFLECTION-ON-TECHNOLOGY-N-LIFE.png)
- [Screenshot 2026-03-31 034049.png](/Book/images/Screenshot 2026-03-31 034049.png)
- [Screenshot 2026-03-31 034154.png](/Book/images/Screenshot 2026-03-31 034154.png)
- [TWM-Watermark.png](/Book/images/TWM-Watermark.png)
- [TWM-Watermark.webp](/Book/images/TWM-Watermark.webp)
- [The-Tower-of-Babel.png](/Book/images/The-Tower-of-Babel.png)
- [agentic-coffee-maker.jpg](/Book/images/agentic-coffee-maker.jpg)
- [ai-guardrails.png](/Book/images/ai-guardrails.png)
- [alliance-empire.png](/Book/images/alliance-empire.png)
- [f530c3d8f802c8b5c73d4014887a264a.jpg](/Book/images/f530c3d8f802c8b5c73d4014887a264a.jpg)
- [faster-better-cheaper.png](/Book/images/faster-better-cheaper.png)
- [hero-bg.png](/Book/images/hero-bg.png)
- [lenovo.jpg](/Book/images/lenovo.jpg)
- [max-studio-creation-1776267881974.jpeg](/Book/images/max-studio-creation-1776267881974.jpeg)
- [max-studio-creation-1776268268466.jpeg](/Book/images/max-studio-creation-1776268268466.jpeg)
- [max-studio-creation-1776268490506.jpeg](/Book/images/max-studio-creation-1776268490506.jpeg)
- [max-studio-creation-1776269398809.jpeg](/Book/images/max-studio-creation-1776269398809.jpeg)
- [max-studio-creation-1776269656364.jpeg](/Book/images/max-studio-creation-1776269656364.jpeg)
- [max-studio-creation-1776269734478.jpeg](/Book/images/max-studio-creation-1776269734478.jpeg)
- [media_0_1776120536388.png](/Book/images/media_0_1776120536388.png)
- [media_0_1776268929116.jpeg](/Book/images/media_0_1776268929116.jpeg)
- [media_0_1776269171347.png](/Book/images/media_0_1776269171347.png)
- [media_0_1776269347702.png](/Book/images/media_0_1776269347702.png)
- [xai-optimus.jpg](/Book/images/xai-optimus.jpg)
