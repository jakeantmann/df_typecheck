#!/bin/sh

python -m venv .
. bin/activate
pip install --upgrade pip
pip install -e ".[dev]"

pre-commit install \
	--hook-type pre-commit \
	--hook-type pre-merge-commit \
	--hook-type pre-push \
	--hook-type prepare-commit-msg \
	--hook-type commit-msg \
	--hook-type post-commit \
	--hook-type post-checkout \
	--hook-type post-merge \
	--hook-type post-rewrite

git config --global core.editor "code --wait"
