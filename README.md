 codingtest
============

### Introduction


Preferred language is Python
### Usage

Prerequisites:

1. Docker is installed
3. A linux/nix based Operating system


---------------------------------------------------------------------------------------------
Steps:

2. Run ```git clone https://github.com/coffeecoco/codingtest.git -b main```
3. ```cd codingtest```
5. Run Unittests inside docker ```sh scripts/local_tests.sh```
6. Build Docker ```sh scripts/local_build.sh```
7. Run Docker ```sh scripts/run_container.sh```
8. Open browser http://127.0.0.1:5000/
9. Open browser http://127.0.0.1:5000/status

unittests are available in travisci which only runs unittests.
https://travis-ci.com/github/coffeecoco/codingtest


Simple 404 error handler
Structured logging for SIEM, this is a cut down version of my logger but ver capable and scalable.

Simple app