#! /bin/bash
source /app/.venv/bin/activate
export VIRTUAL_ENV="/app/.venv"
unset REQUESTS_CA_BUNDLE
python /app/app.py