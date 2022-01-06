#!/bin/bash
sudo docker tag wog:build_$BUILD_TAG xamsa/wog_build_$BUILD_TAG
sudo docker push xamsa/wog_build_$BUILD_TAG
sleep 2
sudo docker container rm "$(sudo docker ps -a -q)" -f