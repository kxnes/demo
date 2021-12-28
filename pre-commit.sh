#!/usr/bin/env bash

set -e

PACKAGE=demo

# ---- formatting
isort .
black .

# ---- linting
flake8 .
pyright .
mypy .
bandit -r ${PACKAGE}

# update stage after formatting
git add .

ln -sf ../../pre-commit.sh .git/hooks/pre-commit
