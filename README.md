 test
============

### Introduction


Preferred language is Python
### Usage

Prerequisites:

1. Docker is installed
3. A linux/nix based Operating system


---------------------------------------------------------------------------------------------
Steps:

2. Run ```git clone https://.git -b develop```
3. ```cd daniel-sanders```
5. Run Unittests inside docker ```sh scripts/unittest.sh```
6. Build Docker ```sh scripts/build.sh```
7. docker run -it -p 5000:5000 myapplication:latest
8. Open browser http://127.0.0.1:5000/api
9. Optional argument http://127.0.0.1:5000/api?logmessage=blah

If you want to test code locally in an IDE or such:
1. Ensure you have the latest python 3.7.x
2. Poetry is installed. You can install it from: https://python-poetry.org/docs/#installation
3. A linux/nix based Operating system
5. Run the following to setup your development environment and download dependencies: ```poetry install```.


Simple 404 error handler

Structured logging for SIEM, this is a cut down version of my logger but ver capable and scalable.



Simple app