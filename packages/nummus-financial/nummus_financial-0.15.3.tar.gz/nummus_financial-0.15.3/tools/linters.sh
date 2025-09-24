#!/bin/sh
# Run every linter
ruff check .
djlint .
codespell . -S node_modules
pyright # No dot cause it gets included files from pyproject.toml
