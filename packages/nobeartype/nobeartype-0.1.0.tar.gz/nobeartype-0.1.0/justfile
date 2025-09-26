## .justfile for managing python dev tasks
# Inspired by this informative article: https://lukasatkinson.de/2025/just-dont-tox/

## Globals/env 
set dotenv-load := true
dotenv-filename := "_local/.env"

PYTHON_RUNTIME := `echo python$(cat .python-version)`
REPO := `basename "$PWD" | tr ' ' '_'`
VENDOR_DIR := "libs/"
DEPRECATED := "deprecated/"

{% if cookiecutter.ff_type != "none" -%}
SERVICE_ACCOUNT := "scheduler-invoker@{%raw%}{{GCP_PROJECT_ID}}{%endraw%}.iam.gserviceaccount.com"
JOB_NAME := "{%raw%}{{REPO}}{%endraw%}-job"
CRON_SCHEDULE := "0 9 * * *"
FUNCTION_URI := `gcloud functions describe {%raw%}{{REPO}}{%endraw%}`
 
TRIGGER_METHOD := {{cookiecutter.cloud_scheduler_method}}
{%- endif %}
default: help
help:
    @echo ""
    @echo "Available commands in this justfile:"
    @echo ""
    @echo "  qa [args]         Run lint, type checks, tests, and coverage"
    @echo "  compose           Start docker compose services (note: the template doesn't include any)"
    @echo "  cov               Generate HTML coverage report"
    @echo "  test [args]       Run pytest with coverage"
    @echo "  lint [args]       Run ruff linter"
    @echo "  type [args]       Run mypy type checks"
    @echo "  type_app         Run mypy on app.py"
    @echo "  type_utils        Run mypy on utils/"
    @echo "  type_src          Run mypy on SRC/"
    @echo "  py312 [args]      Run pytest in isolated Python 3.12 environment with uv"
    @echo "  py311 [args]      Run pytest in isolated Python 3.11 environment with uv"
    @echo "  py310 [args]      ...Guess."
    @echo "  py_requirements   Run tests inside isolated venv with requirements.txt (simulates GCP deployment)."
    @echo "  toml_req          Compile requirements.txt from pyproject.toml (includes `test` group)."
    {%- if cookiecutter.ff_type == "http" -%}
    @echo "  ff                       Run functions-framework locally with _local/.env vars."
    @echo "  deploy_gcloud            Deploy codebase to GCP Cloud Functions."
    @echo "  schedule_gcloud          Create a Cloud Scheduler job to trigger the function."
    @echo "  update_schedule_gcloud   Update the existing Cloud Scheduler job (schedule, URI, OIDC)."
    @echo "  create_cloud_scheduler_sa Create and configure a service account for Cloud Scheduler (OIDC + run.invoker)."    {%- endif -%}
    @echo ""
    @echo "Tip: Use 'just <command> --help' for command-specific flags (if supported)."
    @echo ""

## Commands 
set shell := ['uv', 'run', 'bash', '-euxo', 'pipefail', '-c']
set positional-arguments 

qa *args: deps lint type_src (test) cov

deps: 
    deptry -e .venv/ -e deprecated/ -e libs/ -e docs/ -e tests/ .

compose: 
    docker compose up -d 

cov: 
    coverage html

test *args:
    coverage run -m pytest -q -s \
      --ignore={%raw%}{{VENDOR_DIR}}{%endraw%} \
      tests/ "$@"

lint *args:
    ruff check "$@"

type *args:
    mypy "$@"

type_app: 
    mypy app.py 

type_utils: 
    mypy utils/

type_src: 
    mypy SRC

toml_req: 
    uv pip compile --group test pyproject.toml -o requirements.txt

py312 *args: 
    #!/bin/sh
    uv run --isolated --python=3.12 pytest -q -s \
      --ignore={%raw%}{{VENDOR_DIR}}{%endraw%} \
      tests/ "$@"

py311 *args: 
    #!/bin/sh
    uv run --isolated --python=3.11 pytest -q -s \
      --ignore={%raw%}{{VENDOR_DIR}}{%endraw%} \
      tests/ "$@"

py310 *args: 
    #!/bin/sh
    uv run --isolated --python=3.10 pytest -q -s \
      --ignore={%raw%}{{VENDOR_DIR}}{%endraw%} \
      tests/ "$@"

py_requirements *args: 
    toml_req
    
    #!/usr/bin/env bash
    set -euo pipefail

    PY="{%raw%}{{PYTHON_RUNTIME}}{%endraw%}"

    TMP_DIR="$(mktemp -d -t venvreq.XXXXXX)"
    VENV_DIR="$TMP_DIR/venv"

    "$PY" -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"

    # Use pip from this venv
    python -m pip install --upgrade pip wheel
    python -m pip install -r requirements.txt

    # Run tests
    pytest -q -s \
      --ignore={%raw%}{{VENDOR_DIR}}{%endraw%} \
      tests/ "$@"

    deactivate
    rm -rf "$TMP_DIR"

