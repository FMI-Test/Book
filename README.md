> **Reading Level:** 🟠 Advanced  |  **Grade:** 10  |  **Words:** 397

# Book Writing Style

![Book Writing Style](images/COVER.webp)

This repository preserves raw multilingual drafts that may contain cipher-like phrasing, mixed tone, and layered context. The editorial goal is to preserve the original signal while publishing readable, audience-aware versions.

## Editorial Principles

1. Preserve the source.
2. Improve readability.
3. Clarify context without flattening the author's voice.
4. Deliver multiple narrative layers for different readers.

## Required Chapter Structure

Each transformed chapter should be published in four sections, in this order:

1. `Index`
	- Clear chapter map
	- Logical thematic grouping

2. `Enigma Codex (Deciphered)`
	- Typo and grammar repair
	- Explicit restoration of implied context
	- Short, faithful interpretation of dense passages

3. `English Mysterious Style`
	- Literary, atmospheric retelling
	- Suitable for architects and advanced technical readers

4. `Fairy Tale Version`
	- Plain-language narrative
	- Suitable for general readers, students, and first-time audiences

## Audience Targets

- Architects and CS practitioners
- Applied AI/ML researchers
- General readers and students

## Quality Checklist

- Is the original context preserved?
- Are typos and grammar corrected?
- Are all four required sections present?
- Is each section clearly labeled?
- Is the result understandable across audience levels?

## Tools & Scripts

Install shared Python dependencies before using the automation tooling:

```bash
pip install -r requirements.txt
```

All automation scripts live in the `src/` directory:

| Script | Purpose |
| --- | --- |
| `src/nano_banana_api.py` | Bulk/parallel AI image generation from prompts |
| `src/nano_banana.sh` | Shell wrapper for nano banana batch runs |
| `src/generate_yaml.py` | Convert `::` delimited prompts to YAML |
| `src/distribute_images.py` | Auto-match generated images to markdown files |
| `src/distribute_videos.py` | Auto-match generated videos to markdown files |
| `src/gemini_yt_creator.py` | Generate YouTube video content via Gemini |
| `src/generate_videos_api.py` | API-based video generation |
| `src/youtube_uploader.py` | Bulk upload videos to YouTube |

> See [src/README.md](src/README.md) for detailed usage and [Quick-Start.md](Quick-Start.md) for setup instructions.

## Aliyar Fakhran Research Index

For the diplomatic-history module and archive workflow, see:

- [`Aliyar-Fakhran-FA.md`](Aliyar-Fakhran-FA.md) — Persian biography
- [`Aliyar-Fakhran-EN.md`](Aliyar-Fakhran-EN.md) — English biography
- [`Aliyar-Fakhran-Comparative-Context-FA.md`](Aliyar-Fakhran-Comparative-Context-FA.md) — Persian comparative note on concentrated power, security, and historical memory
- [`Aliyar-Fakhran-Comparative-Context-EN.md`](Aliyar-Fakhran-Comparative-Context-EN.md) — English companion note for the comparative module
- [`Fakhran-Dynasty.md`](Fakhran-Dynasty.md) — structured dynasty, family-tree, and forward/backward research map
- [`Aliyar-Fakhran-Todo.md`](Aliyar-Fakhran-Todo.md) — ongoing research notes
- [`Aliyar-Fakhran-Official-Request-Kit.md`](Aliyar-Fakhran-Official-Request-Kit.md) — official archive request letters
- [`Aliyar-Fakhran-Workflow-Summary.md`](Aliyar-Fakhran-Workflow-Summary.md) — TODO / WIP / DONE tracker and multilingual map
- [`Aliyar-Fakhran-Media-Collateral.md`](Aliyar-Fakhran-Media-Collateral.md) — media usage index, sync rules, tooling notes, and publication plan

## Selected Reflection Modules

- [`Evolution-Sexual-Dimorphism.md`](Evolution-Sexual-Dimorphism.md) — biological variance, reproduction, and evolutionary framing
- [`Parthenogenesis-and-the-Nativity.md`](Parthenogenesis-and-the-Nativity.md) — a personal reflection on miracle narratives, earthly causality, and scientific possibility
- [`Not-Anger.md`](Not-Anger.md) — institutional misnaming, dignity, and refusal
- [`Baede-Az-To.md`](Baede-Az-To.md) — grief, fracture, and survival through art

## Repository Hygiene

- Remove obsolete temporary folders such as `Book.worktrees/` after merge completion.
- Keep chapter files consistent in headings, ordering, and formatting.

---
