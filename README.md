# ML Learning Lab

A step-by-step, coding-first machine learning curriculum based on the supplied Machine Learning roadmap.

## Learning loop

1. Concept
2. Mathematical intuition
3. Implement from scratch
4. Test implementation
5. Use the standard library
6. Compare results
7. Experiment
8. Mini project
9. Write a conclusion

## Roadmap phases

- 00 Python Fundamentals
- 01 NumPy & Linear Algebra
- 02 Probability & Statistics
- 03 Data Analysis
- 04 Data Preparation
- 05 Regression
- 06 Classification
- 07 Model Evaluation
- 08 Unsupervised Learning
- 09 Neural Networks
- 10 CNN
- 11 NLP
- 12 Transformers

Deep-learning/NLP dependencies are intentionally added later as those phases begin.

## Python linting and formatting in VS Code

1. Run `poetry install --with dev` to install the project and development tools.
2. Open this repository folder in VS Code. Open Extensions (`Cmd+Shift+X` on
   macOS), search `@recommended`, and install Ruff, Python, and Jupyter.
3. Run **Python: Select Interpreter** from the Command Palette and select `.venv`.
   For notebooks, also select the `.venv` kernel using the kernel picker.
4. Save a Python file or notebook to format code, apply safe Ruff fixes, and sort
   imports. Remaining lint diagnostics appear in the **Problems** panel.

Configuration lives in `pyproject.toml` and `.vscode/settings.json`. Ruff checks
Python files and Jupyter notebooks, targets Python 3.12, and formats to a target
line length of 100. Notebook checkpoints are excluded. Unused imports (`F401`)
are allowed in notebooks because later interactive cells may need them; Python
modules still receive this check. Ruff does not replace a type checker.

Run the same tools from the repository root:

```bash
poetry run ruff check .          # Report lint issues
poetry run ruff check . --fix    # Apply safe fixes, including import sorting
poetry run ruff format .         # Format Python files and notebook code cells
poetry run ruff format . --check # Check formatting without changing files
```

Save actions use explicit saves (`Cmd+S` / `Ctrl+S`). For whole-notebook actions,
the Command Palette also provides **Ruff: Organize Imports** and
**Ruff: Fix all auto-fixable problems**.

See the [official Ruff VS Code setup](https://github.com/astral-sh/ruff-vscode)
for editor behavior and configuration details.
