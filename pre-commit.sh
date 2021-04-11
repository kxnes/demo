#!/usr/bin/env bash

isort .
black .

git add .

ln -sf ../../pre-commit.sh .git/hooks/pre-commit
