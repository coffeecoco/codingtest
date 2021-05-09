echo "Move unittests Docker file"
cp cicd/unittests/Dockerfile .
echo "Unittests Docker Build"


GIT_BRANCH=$(git branch | grep \* | cut -d ' ' -f2 | tr '[:upper:]' '[:lower:]')
GIT_HASH=$(git log --pretty=format:'%h' -n 1)
SERVICE_PORT="8080"
LOG_LEVEL='DEBUG'

echo "Docker Build for Unittests"
CONTAINER_NAME=myapplication
CONTAINER_VER=${GIT_BRANCH}
pip install jinja2
python scripts/generate.py -sn ${CONTAINER_NAME} -v ${CONTAINER_VER} -gsha ${GIT_HASH}

docker build . -t ${CONTAINER_NAME}:unittest --network=host
echo "Unittests Docker Run tests"
docker run -t --network=host  ${CONTAINER_NAME}:unittest  /app/scripts/run_local_unit_tests.sh
