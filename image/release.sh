#!/bin/bash

set -ex
# SET THE FOLLOWING VARIABLES
# docker hub username
USERNAME="${1}"
# image name
IMAGE="${2}"

version=`cat VERSION`
echo "version: $version"
# run build
./build.sh $USERNAME $IMAGE
docker tag $USERNAME/$IMAGE:latest $USERNAME/$IMAGE:$version
# push it
docker push $USERNAME/$IMAGE:latest
docker push $USERNAME/$IMAGE:$version
