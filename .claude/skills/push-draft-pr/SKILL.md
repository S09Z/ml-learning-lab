---
name: push-draft-pr
description: Use when implementing the next lesson notebook or milestone in this ML learning lab and shipping it for review — identifies the next unfinished notebook from docs/ROADMAP.md and the notebooks/ tree, implements it end-to-end following the project's learning-loop and Thai-lesson house style, validates it (execution + ruff), commits, pushes a feature branch, and opens a Draft PR. Trigger this whenever the user asks to "do the next lesson", "pick up where we left off", "continue the roadmap", "ship this notebook", "open a PR for this", or wants a notebook taken from a blank template to a reviewable pull request — even if they don't say "draft PR" explicitly.
---

# push-draft-pr

## Purpose

Take the next unfinished notebook in this repo's curriculum from template to a reviewable
Draft PR, in one focused, verifiable increment. `PLAN.md` (repo root) is the phase-level map of
every notebook against `docs/ROADMAP.md`'s phases, with a status snapshot of open/merged PRs;
`scripts/find_next_milestone.py` is the file-level source of truth for "is it actually done" (it
checks for the raw `# TODO` scaffold cell, which is more reliable than a manually-updated status
table). This skill's job is to find the next one, fill it in properly, prove it works, hand it
off for review without overreaching into unrelated files, and keep `PLAN.md` honest afterward.

## Safety rules

These hold regardless of how automated the rest of this skill becomes:

- Never force push (no `--force`, no `--force-with-lease`).
- Never commit directly to `main`. Always work on a feature branch.
- Never discard, stash, or overwrite unrelated changes already in the working tree — check
  `git status` before touching anything, and if there's unrelated work in progress, leave it
  alone and tell the user.
- Only ever open a **Draft** PR (`gh pr create --draft`) — never a ready-for-review PR.
- One notebook/milestone per PR. Don't bundle unrelated fixes or a second notebook in.
- Pushing to the remote and opening a PR are both visible, semi-permanent actions on a shared
  repo — confirm the milestone and get a go-ahead from the user before either one, even if the
  implementation and validation steps ran without needing to ask.

## Workflow

### 1. Find the current milestone

Run the bundled helper, which scans every notebook for the literal `# TODO` scaffold cell that
`nb-scaffold`-style templates leave behind (see `scripts/find_next_milestone.py`):

```bash
poetry run python .claude/skills/push-draft-pr/scripts/find_next_milestone.py
```

The first result (file order, which follows `docs/ROADMAP.md`'s phase numbering) is the default
next milestone. If the user names a specific notebook or topic instead, use that — the script
is a default-finder, not an override of explicit instructions.

### 2. Confirm scope before writing anything

State the notebook you're about to fill in and a one-line description of its scope (pull the
topic from `docs/ROADMAP.md`'s phase description and the notebook's own filename). This repo has
no acceptance-criteria file to check against, so this quick confirmation is the cheap substitute
— it's much cheaper to redirect scope now than after a full notebook is written.

### 3. Implement following this repo's conventions

Every filled notebook here follows the 9-step loop from `README.md`: Concept → Mathematical
intuition → Implement from scratch → Test implementation → Use the standard library → Compare
results → Experiment → Mini project → Write a conclusion. Don't treat that as a checklist to
tick mechanically — it's the shape the lesson should take.

For the concrete house style (structure, tone, code conventions), read the most recently
completed notebook in the same phase directory rather than inventing a new format — e.g.
`notebooks/01_numpy_linear_algebra/01_vectors_and_matrices.ipynb` is the reference for Phase 01.
Notable conventions worth matching:

- Thai-language prose, comments, and print output; English identifiers and technical terms.
- Numbered `## N. หัวข้อ` sections, each explaining a concept before its code cell.
- `assert` / `np.testing.assert_allclose` sanity checks in nearly every computed code cell —
  don't let a lesson claim a result without verifying it in the same cell.
- A closing recap table (concept → code → use case), a "แบบฝึกหัด" exercises section with a
  `<details>` collapsible answer key, and a sources section citing whatever the user's original
  request referenced plus the NumPy/library docs actually used for correctness.

Build the notebook programmatically (e.g. with the `nbformat` Python package) rather than
hand-editing the raw JSON — it's far less error-prone for a document with this many cells.
Before writing any numeric value into a markdown explanation or a hardcoded assertion, actually
compute it (a scratch script run through `poetry run python` works well) rather than doing the
arithmetic by hand — a wrong "expected" number in a lesson is worse than no lesson at all.

### 4. Validate before claiming anything is done

Never report a notebook as finished without running these and reading the actual output —
"it should work" is not validation:

```bash
poetry run jupyter nbconvert --to notebook --execute --inplace <notebook path>
poetry run ruff check <notebook path>
poetry run ruff format <notebook path> --check
```

Confirm the executed notebook has zero `error` outputs (parse the `.ipynb` JSON and check every
code cell's `outputs` list rather than eyeballing it). If `ruff format --check` fails, run
`ruff format` without `--check`, then re-execute — reformatting can shift code, and saved
outputs should reflect the code that's actually in the file.

### 5. Commit

Stage only the files this milestone touches (the one notebook, plus anything it genuinely
required) — never a blanket `git add -A` or `git add .`, since the working tree may hold
unrelated in-progress work that isn't yours to sweep in. Match this repo's existing commit
style from `git log` (`type(scope): summary`, e.g. `docs(numpy): add Thai vectors and matrices
ML lesson`).

### 6. Push a feature branch

Branch naming: `claude/<topic-slug>` — matches this repo's existing branches (e.g.
`claude/eigenvalues_and_svd`). Branch from the current base (usually `main`) unless the user is
already mid-work on a relevant branch they want you to continue on. **Confirm with the user
before pushing** — per the safety rules above, this is a visible action on the shared remote.

### 7. Open a Draft PR

```bash
gh pr create --draft --title "<milestone title>" --body "$(cat <<'EOF'
## Milestone
<notebook path and topic, and which docs/ROADMAP.md phase it belongs to>

## What's included
- <bullet per major section covered>

## Validation
- [x] `ruff check` passes
- [x] `ruff format --check` passes
- [x] Notebook executes end-to-end with no error outputs (`jupyter nbconvert --execute`)

## Out of scope
<the next notebooks/milestones deliberately left for a follow-up PR>
EOF
)"
```

**Confirm with the user before creating the PR**, same as the push step. Report the PR URL back
when done.

### 8. Update PLAN.md

Update this notebook's row in `PLAN.md`'s phase table to 🔵 with the new PR number, add a row to
the "Status snapshot" table (branch, base — note if it's stacked on another open PR), and bump
the "Progress" counts at the bottom. Commit this as part of the same PR if `PLAN.md` isn't staged
yet elsewhere, or as a quick separate housekeeping commit on `main` if it is — either way, don't
let `PLAN.md` drift out of sync with reality after a PR merges or opens.

## Preconditions

Check these before starting, not after something fails partway through:

- [ ] `git status` reviewed — any unrelated changes identified and left untouched
- [ ] `git remote -v` shows a configured remote (this repo: `origin` → GitHub)
- [ ] `gh auth status` shows an authenticated account
- [ ] Not currently on `main` when it comes time to commit

## Notes

- This repo has no `MEMORY.md` or `ASSET_SPEC.md` — `PLAN.md` plus each notebook's
  template-vs-filled state (via `scripts/find_next_milestone.py`) is the source of truth for
  "what's next" and "is it done." If `PLAN.md` and the script ever disagree, trust the script
  (it checks the actual file) and fix `PLAN.md` to match.
- If every notebook under `notebooks/` has already been started, the helper script says so —
  at that point, ask the user which specific milestone they mean rather than guessing.
- `notebooks/00_python/01_algorithm_example.ipynb` is a known exception: filled in but
  uncommitted, pre-dating this workflow, and out of the Thai-lesson house style. Leave it alone
  unless the user explicitly asks about it — don't fold it into an unrelated commit.
