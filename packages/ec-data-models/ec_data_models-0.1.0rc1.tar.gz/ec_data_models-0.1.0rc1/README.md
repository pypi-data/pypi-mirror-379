[![PyPI version](https://img.shields.io/pypi/v/EC-Data-Models.svg)](https://pypi.org/project/EC-Data-Models/)
add more when repo is public

## Data-Models

- Repository for managing the shared SQLAlchemy / SQLModel Data Models and Alembic migrations
- This repo gets automatically build, tested and published
- Might be renamed to include other shared backend code later
- The Models are used in:
  - Pipelines & Automations
  - Internal websites API
  - Helpertool

---

- For generel explanation of tooling & setup see our notion page

## Developer Setup

### 1. Prerequisites

This project uses `uv` for package and environment management

**Install `uv`:**

- **macOS / Linux:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows (PowerShell):**
  ```powershell
  irm https://astral.sh/uv/install.ps1 | iex
  ```

### 2. Initial Project Setup

These commands will set up your virtual environment, install dependencies, and enable automated quality checks.

```bash
# 1. Create a virtual environment in a .venv directory
uv venv

# 2. Activate the virtual environment
#    macOS / Linux
source .venv/bin/activate
#    Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 3. Install all dependencies in "editable" mode
uv pip install -e ".[dev]"

# 4. Install the pre-commit hooks for automated quality checks
pre-commit install
```

Your environment is now ready. The **editable install** (`-e`) means that changes you make to the source code are immediately available without reinstalling.

### 3. VSCode Integration

To get the best experience (live error-checking, auto-formatting), configure VSCode to use the project's environment.

1.  **Install Recommended Extensions:**

    - `Python` (by Microsoft)
    - `Ruff` (by Astral)
    - `Mypy Type Checker` (by Microsoft)

2.  **Select the Python Interpreter:**
    - Open the Command Palette: `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac).
    - Run the **`Python: Select Interpreter`** command.
    - Choose the interpreter located in the `./.venv` directory. This is critical for all editor integrations to work.

Once the interpreter is selected, our project's `.vscode/settings.json` file will automatically enable formatting on save, import sorting, and type-checking.

### 4. Running Tests

To run the full test suite, simply use `pytest`:

```bash
pytest
```

If you run into "command not found" for `pytest`, install dev requirements first in your project's virtualenv:

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
uv pip install -e ".[dev]"
pytest -q
```

### 5. Formatting and Linting

- If you want to invoke the pre-commit formatting and type-checking explicitly, activate the environment and run

```bash

pre-commit run --all-files
# For ruff hecks only
ruff check .
ruff format
# For MyPy static type checking only
mypy .
```

---

### Local Development Across Projects

Often, you'll need to test changes from this `data-models` repository in another service (e.g., `Internal-API`) _before_ publishing a new version. Here’s how to link them locally.

**Scenario:** You've made changes in `data-models` and want `Internal-API` to use them instantly.

1.  **Navigate to your other project's directory:**

    ```bash
    cd ../Internal-API
    ```

2.  **Activate its virtual environment:**

    ```bash
    source .venv/bin/activate
    ```

3.  **Uninstall any existing version of `data-models`:** This prevents conflicts with a version installed from the registry.

    ```bash
    uv pip uninstall data-models
    ```

4.  **Install your local `data-models` in editable mode using a relative path:**
    ```bash
    # This command creates a direct link to your local data-models source code
    uv pip install -e ../data-models
    ```

Now, `Internal-API` is linked to your local `data-models` folder. Any code you change in `data-models` will be immediately reflected when you run `Internal-API`.

## Deployment

- This Repo manages all DB migrations to the main DB and applies them on pushes to main
- Best practice would be
  - blue/green testing & only implementing backwards compatible migrations with legacy fields being deprecated later
  - Integration tests on staging version

---

- Trigger rebuilds & deployment of downstream applications on pushes to main

## Docs

- [SQLAlchemy docs](https://www.sqlalchemy.org/)
- [SQLAlchemy unified tutorial (core & ORM)](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [SQLModel docs](https://sqlmodel.tiangolo.com/)
- [alembic docs](https://alembic.sqlalchemy.org/en/latest/)
- [ruff docs](https://docs.astral.sh/ruff/)
