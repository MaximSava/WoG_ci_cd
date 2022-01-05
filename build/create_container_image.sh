#!/bin/bash

echo "Creating container image"
docker build -t "$1":"$2" .

echo "Download selenium docker container"
docker run --name selenium-chrome -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.1.1-20211217
