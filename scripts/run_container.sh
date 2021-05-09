#!/bin/bash -ex

set -e

CONTAINER_NAME=myapplication
docker run -t -p 5000:5000 ${CONTAINER_NAME}:latest
