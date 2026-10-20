#!/usr/bin/env python3
"""List notebooks under notebooks/ that are still raw templates (not yet started).

A notebook is treated as "not started" if any of its code cells is exactly the
scaffold placeholder `# TODO` (nothing else on the line). Filled-in notebooks
replace every `# TODO` cell with real code, so this marker reliably identifies
work that hasn't begun yet without needing a PLAN.md or similar tracking file.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def is_template(notebook_path: Path) -> bool:
    nb = json.loads(notebook_path.read_text())
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", [])).strip()
        if source == "# TODO":
            return True
    return False


def main() -> None:
    notebooks = sorted(NOTEBOOKS_DIR.glob("*/*.ipynb"))
    if not notebooks:
        print("No notebooks found under notebooks/.")
        sys.exit(1)

    not_started = [nb for nb in notebooks if is_template(nb)]
    if not not_started:
        print("Every notebook has been started. Check docs/ROADMAP.md for phases")
        print("with no notebooks yet, or ask the user which milestone they mean.")
        return

    print("Not-started notebooks, in file order (first one is the next milestone):")
    for nb in not_started:
        print(f"  {nb.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
