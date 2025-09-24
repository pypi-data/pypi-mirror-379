# CONTRIBUTING.md

This repo hosts the **Civic Transparency CWE Types** under the **MIT License**.
Our goals are clarity, privacy-by-design, and low friction for collaborators.

> tl;dr: open an Issue or Discussion first for anything non-trivial, keep PRs small and focused, and please run the quick local checks below.

---

## Ways to Contribute

- **Docs**: Fix typos, clarify definitions, or improve examples in `docs/en/**`.
- **Code**: Add or refine typed result/error classes and tests in `src/ci/transparency/cwe/types/`.
- **Actions**: Propose changes to project workflow and action files to follow best practices.

---

## Ground Rules

- **Code of Conduct**: Be respectful and constructive. Reports: `info@civicinterconnect.org`.
- **License**: All contributions are accepted under the repo's **MIT License**.
- **Namespaces**: We use standard Python packages with `__init__.py` files in shared dirs like `ci/`, `ci/transparency/`, `ci/transparency/cwe/` (used by mkdocs).
- **Typing**: This package ships `py.typed`. Keep types accurate and Pyright/mypy-friendly.

---

## Before You Start

**Open an Issue or Discussion** for non-trivial changes so we can align early.

---

## Making Changes

- Follow **Semantic Versioning** via git tags (we use `setuptools-scm`):
  - **MAJOR**: breaking changes
  - **MINOR**: backwards-compatible additions
  - **PATCH**: clarifications/typos
- Update related docs, examples, and `CHANGELOG.md` when behavior or APIs change.

---

## Commit & PR guidelines

- **Small PRs**: one focused change per PR.
- **Titles**: start with area, e.g., `code: fix deprecation warning`.
- **Link** the Issue/Discussion when applicable.
- Prefer **squash merging** for a clean history.
- No DCO/CLA required.

---

## Questions / Support

- **Discussion:** For open-ended design questions.
- **Issue:** For concrete bugs or proposed text/schema changes.
- **Private contact:** `info@civicinterconnect.org` (for sensitive reports).

---

## DEV 0. Install Recommended Tools

- Python 3.12+
- Git
- VS Code
- VS Code Extensions
- uv

---

## DEV 1. Start Locally

```bash
uv venv
uv sync --extra dev --extra docs --upgrade
pre-commit install
```

## DEV 2. Validate Changes

1. Pull from the GitHub repo.
2. Clean the cache.
3. Reinstall dev+docs extras.
4. Stage changes with git add.
5. Use ruff to lint and format.
6. Run pre-commit hooks (twice if needed).
7. Run tests.
8. Build docs (sanity check).

## Quick Start

```bash
git pull
uv cache clean
uv sync --extra dev --extra docs --upgrade
git add .
uv run ruff check . --fix && uv run ruff format .
pre-commit run --all-files
uv run -m pytest -q
uv run -m mkdocs build
```

## DEV 3. Build and Verify Package

Mac/Linux (build and inspect wheel)

```bash
uv run python -m build
unzip -l dist/*.whl
```

Windows PowerShell (build, extract, clean up)

```pwsh
uv run python -m build

$TMP = New-Item -ItemType Directory -Path ([System.IO.Path]::GetTempPath()) -Name ("wheel_" + [System.Guid]::NewGuid())
Expand-Archive dist\*.whl -DestinationPath $TMP.FullName

Get-ChildItem -Recurse $TMP.FullName | ForEach-Object { $_.FullName.Replace($TMP.FullName + '\','') }

Remove-Item -Recurse -Force $TMP
```

## DEV 4. Preview Docs

```bash
uv run mkdocs serve
```

Open: <http://127.0.0.1:8000/>

## DEV 5. Release

We use **`setuptools-scm`**; version is derived from git tags (e.g., `v0.0.1`).
Ensure the tag is created **after** your changes are merged.

1. Update `CHANGELOG.md` with notable changes (modify the beginning and the end of the log).
2. Ensure all CI checks pass.
3. Build and verify package locally.
4. Tag and push.

```bash
uv run ruff check . --fix && uv run ruff format .
pre-commit run --all-files # repeat if needed
git add .
git commit -m "Prep vx.y.z"
git push -u origin main

git tag vx.y.z -m "x.y.z"
git push origin vx.y.z
```

> A GitHub Action will **build**, **publish to PyPI** (Trusted Publishing), **create a GitHub Release** with artifacts, and **deploy versioned docs** with `mike`.

> You do **not** need to run `gh release create` or upload files manually.
