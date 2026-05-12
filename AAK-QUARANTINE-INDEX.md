# AAK Quarantine Index

Date: 2026-04-13
Purpose: Hold low-confidence or non-biography assets outside the public-history visual arc until verified.

## Quarantine Rules

- Keep items here if origin is unclear, context is not Aliyar Fakhran, or naming is noise-heavy.
- Do not use quarantined items in public biography pages.
- Promote only after source/provenance is documented.
- Quarantined items may still appear in the full intake index for repository discoverability, but that catch-all listing does not authorize public use.
- Exclude quarantined items from soundtrack selection, narration planning, and video assembly until released.

## Quarantined Assets (Initial Pass)

| Asset | Reason | Status |
| --- | --- | --- |
| `images/000-15-Alissa Foxy - A Hole Lot Of Fun_4.jpg` | Non-biographical unrelated content | Hold |
| `images/000-16-Alissa Foxy - A Hole Lot Of Fun_7.jpg` | Non-biographical unrelated content | Hold |
| `images/000-17-Alissa Foxy - A Hole Lot Of Fun_8.jpg` | Non-biographical unrelated content | Hold |
| `images/000-18-Alissa Foxy - Erotic Spell_9.jpg` | Non-biographical unrelated content | Hold |
| `images/000-19-Alissa Foxy - Erotic Spell_4.jpg` | Non-biographical unrelated content | Hold |
| `images/000-20-Alissa Foxy - A Hole Lot Of Fun_16.jpg` | Non-biographical unrelated content | Hold |
| `images/000-21-Belka - Schools Out_6.jpg` | Non-biographical unrelated content | Hold |
| `images/000-22-Ellie Leen - Climax From Okinawa_3.jpg` | Non-biographical unrelated content | Hold |
| `images/000-23-Emiri Momota - The Japanese Method_17.jpg` | Non-biographical unrelated content | Hold |
| `images/000-24-Elis - Escort In Paris_36.jpg` | Non-biographical unrelated content | Hold |
| `images/1773504368Lucy-and-2B---Set-1---008.jpg.jpg` | Non-biographical unrelated content | Hold |
| `images/1773504382Lucy-and-2B---Set-1---020.jpg.jpg` | Non-biographical unrelated content | Hold |
| `images/1920px-Twin_Peaks_Summer_Bikini_Contest_(6043000035).jpg` | Non-biographical unrelated content | Hold |
| `images/nsfw-2f2b2b37-44a3-4f33-a45d-e63f2f0f6d10.webp` | Non-biographical unrelated content (NSFW) | Hold |
| `images/nsfw-8fd4ef95-377f-4927-8c01-d3be44740ec2.webp` | Non-biographical unrelated content (NSFW) | Hold |
| `images/nsfw-a6c45a85-3103-4eeb-9840-9886f395a380.webp` | Non-biographical unrelated content (NSFW) | Hold |
| `images/nsfw-cf2a6b77-1388-4022-90f5-c6f713e0e667.webp` | Non-biographical unrelated content (NSFW) | Hold |
| `images/thinking-chair-woman-beach-sunset-holiday-vacation-weekend-getaway-sea-relax-sunshine-thinking-chair-445712013.webp` | Non-biographical unrelated content | Hold |

## Release Criteria

Move from quarantine only when all are true:

1. Provenance is documented (source, date, rights).
2. Relation to Aliyar Fakhran narrative is explicit.
3. Confidence tag is assigned in `AAK-VISUAL-OPS.md`.

## 2026-04-14 Automation Sync

Quarantine registry was reviewed during the all-root AAK auto pass.

### Outcome

- Existing hold set remains in place; no assets were promoted in this pass.
- Quarantine policy language remains aligned with the visual evidence tag workflow.
- Catch-all image indexing remains separate from public-use eligibility.

**AAK QUARANTINE AUTO SYNC:** Completed with no promotion changes.

## 2026-04-25 Image-Reference Scan Sync

Quarantine registry reviewed after PR #29 markdown image-reference audit.

### Outcome

- All 16 quarantined assets remain on hold; none appeared in the missing-reference list from the scan.
- Quarantine policy is unaffected by the missing-asset report.
- No promotions or removals made in this pass.

**AAK QUARANTINE IMAGE SCAN SYNC:** Completed with no status changes.

## 2026-05-11 AAK TODO Sync

Quarantine registry was revalidated against the current `images/` tree.

### Current State

- Policy rules remain valid and unchanged.
- Several legacy quarantine references are not present in the current working tree.

### Open TODOs

1. [ ] Rebuild quarantine asset table from currently available files only.
2. [ ] Move absent legacy entries to an archival note section (history) instead of active hold list.
3. [ ] Keep quarantine exclusion rules enforced for soundtrack, narration, and video assembly.

**AAK QUARANTINE TODO SYNC:** Completed for revalidation and cleanup planning.


## 2026-05-12 NSFW Label + UUID Rename Sync

Quarantine naming and labeling pass executed for explicit NSFW assets.

### Outcome

- Explicit NSFW assets were renamed to UUID-safe filenames.
- Markdown references were updated to renamed UUID assets.
- NSFW status was marked directly in the quarantine table for affected entries.

### Renamed NSFW Assets

UUID values were generated with standard UUIDv4 random IDs and reserved under the `images/nsfw-<uuid>.ext` naming convention to avoid collisions.

| Previous name | New UUID-safe name | Status |
| --- | --- | --- |
| `images/fashion-model-girl-long-sexy-legs-yellow-jacket-white-bra-interior-beautiful-young-woman-fashion-model-176616360.webp` | `images/nsfw-2f2b2b37-44a3-4f33-a45d-e63f2f0f6d10.webp` | Hold (NSFW) |
| `images/girl-beautiful-swimsuit-sunbathing-on-260nw-755081506.webp` | `images/nsfw-8fd4ef95-377f-4927-8c01-d3be44740ec2.webp` | Hold (NSFW) |
| `images/seductive-brunette-sunbathing-on-deck-260nw-2292008719.webp` | `images/nsfw-a6c45a85-3103-4eeb-9840-9886f395a380.webp` | Hold (NSFW) |
| `images/2402155-ai-nude-photos-full-body-teddy-set-ai-girls-photo-studio.webp` | `images/nsfw-cf2a6b77-1388-4022-90f5-c6f713e0e667.webp` | Hold (NSFW) |

**AAK NSFW UUID SYNC:** Completed with quarantine hold preserved.
