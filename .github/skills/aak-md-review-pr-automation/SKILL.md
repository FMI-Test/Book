---
name: aak-md-review-pr-automation
description: 'Review and finalize AAK markdown docs: read files, fix typos/grammar, expand logs, and prepare commit/PR. Use when asked to "review md", "fix typo", "grammar", "expand log", "commit", "open PR", or "automate AAK".'
argument-hint: 'Targets, scope, and mode (safe or auto)'
user-invocable: true
---

# AAK Markdown Review To PR Automation

## Outcome
Produce polished AAK markdown updates that are quality-checked and ready for delivery:
- Markdown content reviewed and corrected
- Relevant AAK logs expanded with dated entries
- Git changes staged with a clean commit message
- PR draft text prepared (and optionally opened)

## When To Use
Use this skill when the request includes any of these intents:
- Read/review markdown docs
- Finish incomplete wording in AAK docs
- Fix typos and grammar
- Expand or append AAK operational logs
- Prepare or execute commit + PR flow
- "Auto" run of the whole AAK pipeline

## Inputs
Accept natural language input, then normalize into:
- `targets`: specific files, globs, or `all AAK`
- `scope`: content-only or content + git actions
- `mode`: `safe` (default) or `auto`
- `branch`: branch name (optional)
- `commitMessage`: explicit commit message (optional)

Default behavior when details are omitted:
- `all AAK` resolves to `AAK-*.md` files in the workspace root
- Log expansion targets `AAK-AUDIT-LOG-FINAL.md` first, then `AAK-QUARANTINE-INDEX.md` and `AAK-VISUAL-OPS.md` when relevant
- `auto` mode executes commit, push, and PR creation when git/CLI auth is available

Example invocation:
- `/aak-md-review-pr-automation read md review finish fix typo grammar expand log to automate aak go pr commit auto all go aak`

## Decision Logic
1. File selection:
- If explicit files are provided, use them.
- If `all AAK` is requested, include files matching `AAK-*.md` in the workspace root.

2. Editing strictness:
- Preserve meaning, tone, and structure.
- Fix only correctness and clarity issues unless expansion is explicitly requested.

3. Git execution:
- In `safe` mode, prepare diffs and suggested commands but do not commit/push/open PR automatically.
- In `auto` mode, run the full commit + PR flow after showing a concise action summary.
- If PR creation cannot run due to missing auth/tooling, fall back to a ready-to-run command sequence and PR draft body.

## Procedure
1. Discover targets.
- Resolve explicit files first.
- For `all AAK`, collect candidate docs and confirm none are outside markdown scope.

2. Review and edit content.
- Correct typos, punctuation, and grammar.
- Normalize heading consistency, list punctuation, and spacing.
- Finish incomplete sentences when intent is obvious.
- Keep wording faithful to author intent.

3. Expand AAK logs.
- Update `AAK-AUDIT-LOG-FINAL.md` with dated, concise entries.
- Also update `AAK-QUARANTINE-INDEX.md` and `AAK-VISUAL-OPS.md` when the changes affect quarantine/media-ops tracking.
- Include: what changed, why, and traceability to touched docs.

4. Validate quality.
- Run markdown linting/checks if available.
- Verify no accidental structural breaks (headings, lists, links).

5. Prepare git artifacts.
- Show a compact change summary grouped by file.
- Stage only intended files.
- Generate a focused commit message (docs/AAK scoped).

6. Commit and PR.
- `safe`: provide exact commit + PR commands and proposed PR title/body.
- `auto`: execute commit, push branch, and open PR (or generate URL-ready command if CLI integration is unavailable).

7. Final report.
- Return: files changed, key fixes, log additions, commit hash (if created), PR link/status.

## Completion Checks
- All requested markdown targets were reviewed.
- Typos/grammar fixes are complete and meaning-preserving.
- Requested log expansion exists and is dated.
- No unrelated files were included.
- Commit/PR state matches selected mode (`safe` vs `auto`).

## Safety Rules
- Never rewrite domain claims without explicit instruction.
- Never perform destructive git actions.
- Never auto-push in `safe` mode.
- If ambiguity changes intent, ask one focused question before continuing.
