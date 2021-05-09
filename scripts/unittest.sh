
GIT_BRANCH=$(git branch | grep \* | cut -d ' ' -f2 | tr '[:upper:]' '[:lower:]')
GIT_HASH=$(git log --pretty=format:'%h' -n 1)
LOG_LEVEL='DEBUG'

echo "Docker Build for Unittests"
CONTAINER_NAME=myapplication
CONTAINER_VER=${GIT_BRANCH}
pip install jinja2
python scripts/generate.py -sn ${CONTAINER_NAME} -v ${CONTAINER_VER} -gsha ${GIT_HASH}

echo "Unittests"
poetry install
mkdir -p src
pip install pycodestyle
pip install isort
poetry install
poetry run coverage run -m py.test  tests/
