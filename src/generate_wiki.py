#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
HOME_MD = WIKI_DIR / "Home.md"


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8", errors="replace")


def unchecked_todos(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^- \[ \] (.+)$", text, re.MULTILINE)]


def build_home() -> str:
    todo = unchecked_todos(read("Aliyar-Fakhran-Todo.md"))
    workflow = unchecked_todos(read("Aliyar-Fakhran-Workflow-Summary.md"))
    quarantine = read("AAK-QUARANTINE-INDEX.md")

    nsfw_rows = []
    for line in quarantine.splitlines():
        if "(NSFW)" in line and line.strip().startswith("|"):
            nsfw_rows.append(line)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Book Wiki Home",
        "",
        f"_Last generated: {ts}_",
        "",
        "## Alignment",
        "",
        "- Aligned with FMI-Test/TomWizMaster issue-template governance and PR review gates.",
        "- TODO/WIP, NSFW quarantine, and wiki sync are managed as pre-merge review controls.",
        "",
        "## Open TODOs (Aliyar-Fakhran-Todo.md)",
        "",
    ]
    lines += [f"- {item}" for item in todo[:15]] or ["- None"]
    lines += ["", "## Open TODOs (Workflow Summary)", ""]
    lines += [f"- {item}" for item in workflow[:15]] or ["- None"]
    lines += ["", "## NSFW Quarantine Entries", ""]
    if nsfw_rows:
        lines += ["| Asset | Reason | Status |", "| --- | --- | --- |"]
        lines += nsfw_rows
    else:
        lines.append("- No NSFW-marked rows found.")

    lines += [
        "",
        "## Source Index",
        "",
        "- `Aliyar-Fakhran-Todo.md`",
        "- `Aliyar-Fakhran-Workflow-Summary.md`",
        "- `AAK-QUARANTINE-INDEX.md`",
        "- `AAK-VISUAL-OPS.md`",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    HOME_MD.write_text(build_home(), encoding="utf-8")
    print(f"Generated {HOME_MD}")


if __name__ == "__main__":
    main()
