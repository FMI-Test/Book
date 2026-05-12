# Editorial Workflow and Change Management Standards

**Author:** Bamdad Fakhran  
**Date:** May 11, 2026  
**Mode:** Long-form Editorial and Transformation Process

## Purpose

This document defines the editorial workflow for the Book repository: capturing raw multilingual drafts, transforming them through the required chapter structure (Index → Enigma Codex → English Mysterious Style → Fairy Tale Version), and managing all changes transparently so that readers and collaborators understand exactly what was revised and why.

The AI assists in deciphering dense passages, restoring implied context, improving readability across audience levels, and ensuring consistency with translation and tone guidelines preserved in user memory. All modifications must maintain the author's voice while enhancing clarity and accessibility.

## Process Overview

1. **Raw Draft Capture:** Start with multilingual source material (Persian, English, mixed).
2. **Editorial Analysis:** Read, assess context, identify cipher-like phrasing, mixed tone, and layered meanings.
3. **Four-Section Transformation:**
   - **Index:** Thematic mapping and chapter structure
   - **Enigma Codex (Deciphered):** Grammar/typo repair + context restoration + interpretation of dense passages
   - **English Mysterious Style:** Literary retelling for architects and advanced readers
   - **Fairy Tale Version:** Plain-language narrative for general audiences and students
4. **Audience Alignment:** Ensure each section targets the correct reading level (architects/CS, researchers, general/students).
5. **Quality Verification:** Confirm original signal is preserved, typos are fixed, all four sections are present and labeled.
6. **Metadata Addition:** Append author, date, source language, and transformation mode to the top of each chapter.
7. **Repository Integration:**
   - Verify alignment with existing chapters and narrative continuity.
   - Update cross-references and chapter indices.
   - Run integrity checks to ensure multilingual consistency (Persian-English equivalence, term consistency).
   - Commit changes with detailed messages tracing the transformation pipeline.

## AI Permissions and Editorial Autonomy

Explicit permission is granted for the AI to:
- Modify, reorganize, or restructure raw drafts for clarity.
- Correct grammar, spelling, and punctuation across Persian and English.
- Add explicit interpretations of ambiguous passages (flagged as edits for user review).
- Generate parallel versions (Literary vs. Fairy Tale) from a single Enigma Codex.
- Update cross-references, indices, and metadata across chapters.

**Transparency Requirement:** Even with full editorial autonomy, the AI **must** present all proposed changes using the standards in "[Show Diff and Explain Editorial Changes](#show-diff-and-explain-editorial-changes)" before committing. This preserves the author's agency and ensures changes can be traced back to editorial decisions, not author intent.

During the process, document all findings, interpretive choices, context restorations, and newly discovered literary connections. Integrate this documentation into the chapter's metadata and workflow notes for future reference.

## Quality Assurance Framework

**First Priority:** Preserve the original signal and author's voice.

**Decision Framework:** Apply editorial priorities rather than arbitrary options:
- **Must:** Preserve author intent; fix factual errors; restore lost context.
- **Should:** Improve readability; clarify ambiguous passages; enhance narrative flow.
- **Could:** Expand metaphors; add structural parallels; optimize pacing.
- **Won't:** Sanitize authentic voice; flatten complexity; add author's views not in source.

## Show Diff and Explain Editorial Changes

**Objective:** Present all transformations transparently, with clear explanations of editorial intent, textual impact, and rationale. This ensures the author understands exactly what changed, why, and whether it preserves the original signal.

### Editorial Diff Presentation Standards

1. **Granular, Contextual Diffs**
   - Present changes at the **literary unit level** (paragraph, metaphor, sentence cluster), not raw line diffs.
   - For structural changes: Show the before/after organization clearly, with section headers and thematic groupings.
   - For language edits: Show original → edited version with brief explanation of the grammar/clarity improvement.
   - For additions (restored context, interpretation): Clearly label as `[ADDED INTERPRETATION]` or `[CONTEXT RESTORED]`.
   - For deletions (removed redundancy, cut passages): Explain what was removed and why, with the deleted text in a collapsible format if lengthy.

2. **Structured Editorial Diff Format**
   - Use markdown code blocks for readability.
   - Prefix each change with: `[ACTION] SECTION-NAME | Impact: AUDIENCE`
   - Example action labels: `[TYPO-FIX]`, `[GRAMMAR-IMPROVED]`, `[CONTEXT-RESTORED]`, `[AMBIGUITY-CLARIFIED]`, `[STRUCTURE-REORGANIZED]`
   - Example:
     ```markdown
     [GRAMMAR-IMPROVED] Enigma Codex | Impact: Readability
     
     Before:
     "The kargozar office, it was constructed as a place where power, it flow like water."
     
     After:
     "The kargozar's office was constructed as a place where power flowed like water."
     
     Rationale: Fixed subject-verb agreement and tense consistency while preserving the stream-of-consciousness effect.
     ```

3. **Batch Editorial Changes by Section**
   - Group changes by **transformation stage** (Index edits, Enigma Codex decipherments, Literary rewrites, Fairy Tale simplifications).
   - Use a summary table showing affected sections and change counts:
     ```markdown
     ## Editorial Changes Summary
     | Section | Type | Count | Impact |
     |---------|------|-------|--------|
     | Index | Reorganized | 3 | Thematic clarity |
     | Enigma Codex | Grammar + Context | 12 | Readability |
     | English Mysterious | Literary polish | 5 | Tone consistency |
     | Fairy Tale | Simplification | 8 | Accessibility |
     ```

### Editorial Explanation Standards

1. **Intent Before Action**
   - For each change cluster, explain **why** before showing **what**.
   - Link the edit to editorial principles: preserving signal, restoring context, improving clarity, targeting audience.
   - Use a bullet structure: `Principle → Change → Verification`
   - Example:
     ```markdown
     **Change: Clarify ambiguous reference to "the Governor's agent"**
     
     **Principle:** Preserve original signal while restoring implied context.
     Kargozar (کارگزار) is a specific diplomatic role, not a generic "agent."
     
     **What Changed:**
     - Added explanatory phrase: "[the kargozar, or governor's agent with full authority]"
     - Added footnote linking to Glossary term definition
     
     **Verification:** This edit aligns with translation guidelines (user memory:
     Kargozar = Governor/Agent, NOT "clerk" or "broker").
     ```

2. **Impact Assessment by Audience**
   - Categorize each change by who it affects:
     - **🟢 Low:** Typo fixes, minor grammar, punctuation (invisible to reader).
     - **🟡 Medium:** Context additions, clarifications, minor reorganization (helps understanding).
     - **🔴 High:** Major restructuring, tone shifts, section rewrites (visible change to narrative).
   - Explain downstream implications: "This change affects [X narrative thread] and may require updates to [Y later chapter]."

3. **Decision Context and Alternatives**
   - If multiple editorial approaches were considered, explain why one was chosen:
     ```markdown
     Alternative 1: Delete the ambiguous passage entirely.
     → Rejected: Loses author's dense layering and metaphorical intent.
     
     Alternative 2: Add a full explanatory sidebar.
     → Rejected: Interrupts narrative flow; not in author's style.
     
     Chosen: Subtle parenthetical clarification.
     → Preserves voice while providing context for readers.
     ```
   - Flag assumptions: "Assumption: [author meant X]; verify with [author/source]."

4. **Traceability and Source Attribution**
   - Link each change to:
     - The source text (original Persian, raw draft, prior version).
     - Relevant editorial principles or audience target.
     - User memory guidelines (e.g., translation rules, tone guidelines).
     - Related chapters or cross-references.
   - Example: `Source: Aliyar-Fakhran-FA.md#L42 | Related: [Fakhran-Dynasty.md](Fakhran-Dynasty.md#Context) | Principle: [translation-guidelines.md#Kargozar]`

### Before-After Validation

- After presenting editorial changes, perform **editorial sanity checks**:
  - Does the transformation preserve the author's voice and intent?
  - Are all four required sections (Index, Enigma Codex, Literary, Fairy Tale) present and balanced?
  - Does the edited content maintain consistency with prior chapters and established terminology?
  - Are all cross-references still accurate?
  - Are audience levels appropriately differentiated (advanced vs. plain language)?
  - Does the edit respect the translation guidelines and multilingual equivalence?
- Highlight any **editorial concerns** explicitly:
  ```markdown
  ⚠️ Concern: Ambiguous Persian phrase carries multiple meanings; interpretation chosen may shift 
  reader understanding. Recommend author review before publishing.
  ```

### Author Confirmation Workflow

1. **Present the editorial diffs and explanations** grouped by section and impact level.
2. **Await author feedback** before proceeding to merge or commit:
   - Approve as-is.
   - Request specific modifications to particular edits.
   - Reject the batch and provide alternative directions.
   - Clarify author intent for ambiguous passages.
3. **Document the author's decision** (e.g., "Author approved Enigma Codex edits on May 11, 2026; requested revision to Literary section metaphor").
4. **Proceed to commit and push** only after explicit approval.

## Multilingual and Cross-Repository Alignment

- Maintain equivalence between Persian (FA) and English (EN) versions.
- Verify that key terms align with the Glossary (e.g., Kargozar, Zinat Khanum, Mammadjan).
- Check consistency with broader W3 ecosystem references (W3/TomWizMaster, W3/TomWiz.io).
- Validate that photo captions distinguish between real historical photos (`Ali-Yar-Fakhran-*` prefix) and AI illustrations (`Aliyar-Fakhran-*` prefix).

## Chapter Transformation Checklist

Before finalizing any chapter, verify:

- ✅ Original context and signal preserved
- ✅ All typos and grammar corrected (both languages)
- ✅ All four sections present and clearly labeled
- ✅ Index provides clear thematic map
- ✅ Enigma Codex includes context restoration and interpretation
- ✅ English Mysterious Style suits architects/advanced readers
- ✅ Fairy Tale Version uses plain language for general audiences
- ✅ Metadata includes author, date, source language, transformation mode
- ✅ Cross-references verified and working
- ✅ Multilingual equivalence maintained
- ✅ Author approved all changes

This workflow ensures the Book repository remains a trustworthy, transparent, and audience-aware archive of dense multilingual knowledge while preserving every layer of the author's voice.
