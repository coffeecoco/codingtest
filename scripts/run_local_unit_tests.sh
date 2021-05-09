#!/bin/bash

set -e
cd /app
poetry install
mkdir -p src

echo "pip install pycodestyle/isort"
pip install pycodestyle
pip install isort

echo "Poetry Install"
poetry install
poetry run coverage run -m py.test  tests/
#set +e
