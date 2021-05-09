#!/bin/bash -ex
cp cicd/build/Dockerfile .
set -e


GIT_BRANCH=$(git branch | grep \* | cut -d ' ' -f2 | tr '[:upper:]' '[:lower:]')
GIT_HASH=$(git log --pretty=format:'%h' -n 1)
SERVICE_PORT="8080"
LOG_LEVEL='DEBUG'

echo "Docker Build"
CONTAINER_NAME=myapplication
CONTAINER_VER=${GIT_BRANCH}
pip install jinja2
python scripts/generate.py -sn ${CONTAINER_NAME} -v ${CONTAINER_VER} -gsha ${GIT_HASH}
docker build -t ${CONTAINER_NAME}:${CONTAINER_VER} .
docker build -t ${CONTAINER_NAME}:latest .

# if I had a secure pipeline
# storing of unittest coverage
# i would versionn these builds with e.g pycalver
# tag the git repo after builds
# have a the typical develop branch mergingn to master etc.
