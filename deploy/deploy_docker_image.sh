#!/bin/bash
set -e
sudo docker container rm $(sudo docker ps -a -q) -f
sudo docker tag wog:build_"$1" xamsa/wog_build_"$1"
sudo docker push xamsa/wog_build_"$1"
sleep 2
