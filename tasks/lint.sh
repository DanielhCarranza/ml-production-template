#!/bin/bash
set -uo pipefail
set +e

FAILURE=false

echo "safety"
safety check -r requirements.txt -r requirements-dev.txt || FAILURE=true

echo "pylint"
pylint api model_core training || FAILURE=true

echo "pycodestyle"
pycodestyle api model_core training || FAILURE=true

echo "pydocstyle"
pydocstyle api model_core training || FAILURE=true

echo "mypy"
mypy api model_core training || FAILURE=true

echo "bandit"
bandit -ll -r {api,model_core,training} || FAILURE=true

echo "shellcheck"
shellcheck tasks/*.sh || FAILURE=true

if [ "$FAILURE" = true ]; then
  echo "Linting failed"
  exit 1
fi
echo "Linting passed"
exit 0
