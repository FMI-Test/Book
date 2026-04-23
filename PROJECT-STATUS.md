# Project Status

Date: April 20, 2026
Repository: Book
Branch: dev

## Progress Bars

- Instructions refactor: `[##########]` 100%
- Public-content boundary: `[##########]` 100%
- AAK safe visualization guidance: `[#########-]` 90%
- Restricted access architecture: `[########--]` 80%
- TomWizMaster platform guide draft: `[########--]` 80%
- README badge baseline: `[##########]` 100%
- Cross-repo propagation: `[#---------]` 10%
- README cleanup and lint follow-up: `[##--------]` 20%

## Analysis Summary

The repo now has a much clearer operating boundary than it did before this pass.

What changed:

1. Shared instructions were rewritten into a shorter and more usable baseline.
2. Cross-platform scripting guidance was added.
3. Public-repo safety was made more explicit.
4. AAK visual ops now contains a reusable safe-visualization rule set for charged topics.
5. A new chapter, `Up-Here-Down-There.md`, now covers the topic analytically without pushing the repo into explicit-content territory.
6. A deployment and IAM planning draft now exists for restricted publication on `tomwiz.io`.
7. A TomWizMaster-facing quick-start platform guide draft now exists for later repo distribution.

What that means in practice:

- GitHub remains the source-of-truth and should stay broadly PG-13.
- Mature or explicit raw material, if retained at all, should remain quarantined, private, or off-platform.
- Public-facing analytical writing can be published outward to more suitable channels without changing the repo's baseline.
- The repo now has a concrete separation model between public GitHub content and future restricted membership content.
- The repo now has a practical one-cloud-first guidance draft for TomWizMaster without turning the project into a pure cloud-strategy repo.

## Publication Channel Analysis

| Channel | Best use | Repo fit | Notes |
| --- | --- | --- | --- |
| GitHub | Canonical docs, code, workflow, public-safe assets | High | Keep PG-13 baseline |
| Medium | Public essays, synthesis, readable longform analysis | High | Good for cleaned public-facing prose |
| DeviantArt | Stylized visual work, concept art, mature-but-platform-compliant presentation | Medium | Better for art than for canonical research/archive control |
| Self-hosted/private storage | Raw intake, explicit or restricted references | High | Best place for material that should not live in a public repo |

## Done

- Replaced the noisy instructions file with a structured baseline.
- Added README badges for real repo tooling.
- Added cross-platform policy and repo divergence guidance.
- Added a non-graphic chapter for the charged-topic analysis.
- Added safe visualization rules into AAK visual ops.
- Logged the AAK work in the audit log.
- Added an explicit public-content boundary and publication-channel guidance.
- Added a draft restricted-membership IAM and deployment architecture plan.
- Added a TomWizMaster quick-start platform and domain setup draft for later porting.

## WIP

- Propagating the new instruction baseline to sibling repos.
- Deciding whether to add repo-level `CHANGELOG.md` and/or `WIP.md` across the portfolio.
- Deciding whether chapter-level publication packaging should be GitHub-only, Medium-first, or split by audience.
- Choosing between AWS-first identity/runtime and a heavier Azure-first identity posture.
- Porting new platform/setup docs into the proper sibling repo once it is available in the workspace.

## TODO

- Mirror the updated instructions into `../TomWizMaster` and `../TomWiz.io`.
- Add a concise changelog entry standard across repos.
- Decide final external publishing path for visual essays and long-form analysis.
- Clean legacy markdownlint issues in `README.md`.
- Link this status file from `README.md` if you want it to be a first-class project surface.
- Convert the architecture draft into environment-by-environment IaC and deployment steps when implementation starts.
- Port `TomWizMaster-Quick-Start-Platform-Guide.md` into the actual TomWizMaster repo.
- Convert the domain/setup checklist into implementation tasks when site work starts.

## Recommendation

Use GitHub as the clean, public, collaborative base.

Use Medium for essays and explainers.

Use DeviantArt only for artwork or stylized image-led publication that does not need to function as the canonical source of record.

Keep anything explicit, unstable, or raw out of the public repo.
